{
    'name': "Group Category Stock",
    'version': '1.0.0',
    'category': 'Inventory',
    'application': False,
    'installable': True,
    'auto_install': False,
    'application': True,

    'depends': ['stock'],

    'website': "https://spoc.com.ua",
    'author': "Spoc, Vasyl Kaliuta",
    'license': 'LGPL-3',
    'summary': """Group By Category Stock quant""",

    'data': [
        'views/stock_quant_views.xml',
    ],

}

