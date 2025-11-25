{
    'name': 'cambia color',
    'version': '1.0',
    'category': 'Theme',
    'description': 'Cambia los colores del backend de Odoo',
    'author': 'Maharba',
    'depends': ['web'],
    'data': [
    ],
    'assets': {
        'web.assets_backend': [
            'cambia_color/static/src/css/colores.css',
        ],
    },
    'installable': True,
    'application': False,
}
