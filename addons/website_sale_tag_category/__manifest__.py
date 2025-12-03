{
    'name': 'Filtro para etiquetas en categorías',
    'version': '1.0',
    'category': 'Website/eCommerce',
    'summary': 'Filtra etiquetas de productos según la categoría pública actual',
    'description': """
        Este módulo permite asignar categorías de e-commerce a las etiquetas de productos.
        Cuando un cliente navega por una categoría específica, solo verá las etiquetas
        asignadas a esa categoría (o etiquetas globales sin asignación).
    """,
    'author': 'Maharbaa',
    'depends': ['website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_tag_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}