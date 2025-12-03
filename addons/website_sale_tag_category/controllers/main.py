import logging
from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

_logger = logging.getLogger(__name__)

class WebsiteSaleTagFilter(WebsiteSale):

    @http.route()
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        # 1. Ejecución original
        response = super(WebsiteSaleTagFilter, self).shop(page=page, category=category, search=search, ppg=ppg, **post)

        # 2. CORRECCIÓN DE LA BARRA LATERAL (SIDEBAR)
        if response and hasattr(response, 'qcontext'):
            current_category = response.qcontext.get('category')
            
            tags_domain = []

            if current_category:
                # CASO A: Estamos dentro de una Categoría (ej: Oficina)
                # Lógica: Mostrar etiquetas Globales (vacías) O asignadas a Oficina.
                tags_domain = [
                    '|', 
                    ('public_category_ids', '=', False),
                    ('public_category_ids', 'in', current_category.id)
                ]
            else:
                # CASO B: Estamos en la raíz "Todas las categorías" (/shop)
                # Lógica: AQUÍ ESTABA EL PROBLEMA.
                # Antes no hacíamos nada aquí, y Odoo ocultaba las etiquetas dinámicamente.
                # Ahora forzamos a que busque TODAS las etiquetas existentes.
                tags_domain = [] 

            # Ejecutamos la búsqueda con el dominio decidido
            # Esto asegura que la lista de filtros ('all_tags') siempre tenga opciones,
            # independientemente de si la búsqueda actual devolvió 0 o 100 productos.
            all_tags = request.env['product.tag'].search(tags_domain)
            
            if all_tags:
                response.qcontext['all_tags'] = all_tags
                # _logger.info(f">>> ETIQUETAS FORZADAS (Modo {'Categoría' if current_category else 'Todas'}): {len(all_tags)}")

        return response