# -*- coding: utf-8 -*-
{
    'name': "Tutor Hak Akses oleh Cak Juice",

    'summary': """Tutorial pengaturan hak akses pada aplikasi Odoo.""",

    'description': """Ini adalah modul untuk contoh pengaturan hak akses pada aplikasi Odoo.\n
Modul ini hanya modul tutorial, bukan modul aplikasi sebenarnya.\n
Silakan gunakan untuk keperluan belajar Odoo.""",

    'author': "Cak Juice",
    'website': "https://cakjuice.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'views/templates.xml',
        'security/new_group.xml',
        'security/ir.model.access.csv',
        'security/new_rule.xml',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}