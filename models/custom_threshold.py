from odoo import models, fields


class custom_threshold(models.TransientModel):
    _inherit = ['res.config.settings']

    threshold_amount = fields.Integer(string="Threshold amount", store=True)


class custom(models.Model):
    _inherit = 'sale.order'

    def approve_fn(self):
        print("nothing")

    def reject_fn(self):
        print("nothing")
