{
    'name': "openacademy",
    'summary': "Open Academy - module odoo-lerning.",
    'version': '1.0.0',
    'description': """Open Academy - module odoo-lerning.""",
    'author': "Vasyl Kaliuta",
    'website': "https://borove.top",
    'category': 'Academy',
    'sequence': -50,
    'depends': ['board', 'mail'],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',

    'data': [
        'security/openacademy_security.xml',
        'security/ir.model.access.csv',
        'data/course_data.xml',
        'wizard/create_session_view.xml',
        'views/course_views.xml',
        'views/session_report.xml',
        'views/report_session.xml',
        'views/dashboard.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
}
