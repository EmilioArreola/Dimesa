{
    'name': 'Tema Nuevo V1',  # Nombre nuevo
    'version': '1.0',
    'depends': ['web'],
    'data': [], 
    'assets': {
        'web.assets_backend': [
            # NOTA: Aquí debe decir 'tema_nuevo_v1', igual que tu carpeta
            'tema_nuevo_v1/static/src/css/colores.css', 
        ],
    },
    'installable': True,
    'license': 'LGPL-3',
}