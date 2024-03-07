# -*- coding: utf-8 -*-
{
    'name': "Drag_and_Drop",

    'summary': "Carga de archivos para procesar en Odoo",

    'description': """
Carga de archivos para procesar en Odoo
    """,

    'author': "Equipo 6",
    'website': "https://faztecaerp.site",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customizations',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    
    'application': True,

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/drag_and_drop_view.xml',
    ],
}

