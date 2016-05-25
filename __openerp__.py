# -*- coding: utf-8 -*-
{
    'name': "moduloPartidos",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Modulo para gestionar la direccion deportiva de un club deportivo
    """,

    'author': "Borja Pastor",
    'website': "http://www.google.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'datos.xml',
        'jugadores_report.xml',
        'informeJugadores.xml',
        'informeDelanteros.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}