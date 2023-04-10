# -*- coding: utf-8 -*-
{
    'name': 'New fields Purchase',
    'version': '15.0.2.0.0',
    'summary': """Nuevos campos para orden de compra""",
    'description': """Nuevos campos para orden de compra""",
    'author': 'Jose Aguilar',
    'company': 'BrainTech',
    'maintainer': 'BrainTech',
    'website': 'https://braintech.odoobt.com',
    'license': 'LGPL-3', 
    'depends': ['base','purchase'],
    'data': [
                'security/ir.model.access.csv',
                'data/datos.xml',
                'views/purchase_view.xml',
             ],
    'installable': True,
    'application': True,
}