{
    "name": "Edita Menú",
    "version": "1.0.1",
    "author": "Maharba",
    "category": "Customization",
    "summary": "Personalizaciones visuales para Odoo (ocultar menús, títulos, etc.)",
    "description": """
        Módulo de personalización para Odoo que ajusta la interfaz visual:
        - Oculta el título "Odoo" en el modal de envío de correo.
        - Permite agregar un título personalizado como "Enviar correo al cliente".
        - Incluye modificaciones visuales adicionales en el backend.
    """,
    "depends": ["web"],
    "assets": {
        "web.assets_backend": [
            "belero_web_custom/static/src/css/hide_menu.css",
        ],
    },

    "installable": True,
    "application": False,
    "license": "LGPL-3",
}
