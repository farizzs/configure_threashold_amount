# -*- coding: utf-8 -*-

{
    'name': 'custom_threshold',
    'version': '16.0.0.0',
    'license': 'LGPL-3',
    'author': "Codex/Faris",
    'website': "http://www.codexitns.com",
    'depends': ['base', 'sale', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/custom_treshold.xml',
        'views/sale_order_btn.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': True,
}
