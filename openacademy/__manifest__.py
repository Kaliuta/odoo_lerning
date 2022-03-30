{
    'name': "openacademy",
    'summary': "Open Academy - навчальний модуль з курсу odoo-lerning.",
    'version': '15.0.1.0.1',
    'description': """Open Academy - навчальний модуль з курсу odoo-lerning.""",
    'author': "Vasyl Kaliuta",
    'website': "https://borove.top",
    'category': 'Uncategorized',
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
