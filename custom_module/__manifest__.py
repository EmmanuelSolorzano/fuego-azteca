# -*- coding: utf-8 -*-
{
    'name' : 'Fuego Azteca Dashboard',
    'version' : '1.0',
    'summary': 'Dashboard for Fuego Azteca',
    'sequence': -1,
    'description': """Dashboard for Fuego Azteca""",
    'category': 'OWL',
    'depends' : ['base', 'web', 'sale', 'board'],
    'data': [
        'views/sales_dashboard.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'custom_module/static/src/components/**/*.js',
            'custom_module/static/src/components/**/*.xml',
            'custom_module/static/src/components/**/*.scss',
        ],
    },
}
