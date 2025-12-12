{
    'name' : 'Sale order Extend',
    'version': '1.0',
    'category': 'Hidden',
    'description': "i want to add some extra features in sale order",
    'depends': ['base','sale'],
    'data': [
        'views/sale_order_extend.view.xml',
    ],
    'installable': True,
    'auto_install': True,
    'assets': {
        'web.assets_backend': [
        ],
        'web.assets_frontend': [
        ],
    },
    'author': 'Adnan',
    'license': 'LGPL-3',
}
