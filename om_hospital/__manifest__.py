# -*- coding: utf-8 -*-
{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'category': 'Hospital',
    'author': "Vasyl Kaliuta",
    'sequence': -100,
    'summary': 'Hospital management system',
    'description': """Hospital management system module""",
    'depends': ['mail', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/cancel_appointment_view.xml',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
        'views/patient_tag_view.xml',
    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

