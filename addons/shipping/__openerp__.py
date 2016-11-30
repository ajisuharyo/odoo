# -*- coding: utf-8 -*-
{
    'name': "Penyiapan Jalur Vol.2",

    'summary': """
        Penyiapan Jalur Warisan dari Sumbermas""", #akan muncul di index apps

    'description': """
        Bisa Kirim2 kemanapun, namanya juga penyiapan jalur""",

    'author': "Sumbermas Team",
    'website': "http://wgs.co.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'apps',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/templates.xml',
        'views/product_views.xml',
        'views/prepare_product_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True, #agar masuk list apps
    'auto_install': False,
}