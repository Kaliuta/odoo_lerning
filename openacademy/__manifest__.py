{
    'name': "openacademy",
    'summary': "Open Academy - module odoo-lerning.",
    'version': '1.0.0',
    'description': """Open Academy - module odoo-lerning.""",
    'author': "Vasyl Kaliuta",
    'website': "https://borove.top",
    'category': 'Academy',
    'sequence': -50,
    'depends': ['base', 'board'],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',

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
