# -*- coding: utf-8 -*-
{
    'name': "om_odoo_inheritence",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'license': 'LGPL-3',
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['sale', 'project', 'stock'],

    'data': [
        'views/sale_order_view.xml',
    ],

    'demo': [],
}
