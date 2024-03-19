from odoo import models, fields, api
from odoo.exceptions import UserError


class custom_threshold(models.TransientModel):
    _inherit = ['res.config.settings']

    threshold_amount = fields.Float(string="Threshold amount",
                                    config_parameter='sale.threshold_amount')


class CustomSaleOrder(models.Model):
    _inherit = 'sale.order'

    approve_bool = fields.Boolean(string="approve bool")
    check_bool = fields.Boolean(string="check_bool", compute="_compute_total_amount")

    def approve_fn(self):
        self.approve_bool = True

    def reject_fn(self):
        self.approve_bool = False
        print(self.approve_bool)
        raise UserError("Rejected")

    def action_confirm(self):
        res = super(CustomSaleOrder, self).action_confirm()
        custom = float(self.env['ir.config_parameter'].sudo().get_param
                       ('sale.threshold_amount'))

        if self.amount_total < custom and self.approve_bool == True:
            self.action_confirm()
        elif self.amount_total > custom and self.approve_bool == False:
            raise UserError("Approve needed for confirmation")
        elif self.amount_total < custom:
            self.check_bool = True
        elif self.amount_total > custom:
            self.check_bool = False

    @api.depends('check_bool', 'amount_total')
    def _compute_total_amount(self):
        threshold = float(self.env['ir.config_parameter'].sudo().get_param
                       ('sale.threshold_amount'))
        if self.amount_total < threshold:
            self.check_bool = True
        else:
            self.check_bool = False

        # elif self.approve_bool == False:
        #     res = super(CustomSaleOrder, self).action_cancel()
        #     self.action_cancel()
