# -*- coding: utf-8 -*-
{
    'name' : 'Fuego Azteca Carga Datos',
    'version' : '1.0',
    'summary': 'Carga de datos para el dashboard de Fuego Azteca',
    'sequence': -1,
    'description': """Carga de datos para el dashboard de Fuego Azteca""",
    'category': 'OWL',
    'depends' : ['base', 'web', 'board'],
    'data': [
        'views/carga_datos.xml',
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'carga_datos/static/src/components/**/*.js',
            'carga_datos/static/src/components/**/*.xml',
            'carga_datos/static/src/components/**/*.scss',
            'carga_datos/static/src/components/**/*.css',
        ],
    },
}
