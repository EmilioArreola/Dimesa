{
    'name': 'Tema Nuevo V1',
    'version': '1.0',
    'depends': ['web', 'sale'],  # <--- IMPORTANTE: Añadir 'sale' porque modificas reportes de venta
    
    # 1. Los archivos XML de vistas/reportes van AQUÍ:
    'data': [
        'views/report_sale_custom.xml',
    ], 
    
    # 2. Los archivos CSS/JS van AQUÍ:
    'assets': {
        'web.assets_backend': [
            'tema_nuevo_v1/static/src/css/colores.css',
        ],
    },
    
    'installable': True,
    'license': 'LGPL-3',
}