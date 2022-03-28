{
    'name': "openacademy",

    'summary': """
        Open Academy""",

    'description': """
        Open Academy module
    """,

    'author': "Vasyl Kaliuta",
    'website': "https://borove.top",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0.1.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board'],
    'application': True,

    # always loaded
    'data': [
        'security/openacademy_security.xml',
        'security/ir.model.access.csv',
        'views/course_views.xml',
        'views/session_report.xml',
        'views/report_session.xml',
        'views/dashboard.xml',
        'wizard/create_session_view.xml',
        'data/course_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
