import logging
from werkzeug.urls import url_encode # <--- Necesario para reconstruir la URL
from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

_logger = logging.getLogger(__name__)

class WebsiteSaleTagFilter(WebsiteSale):

    @http.route()
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        
        # ==========================================================================
        # 1. SANITIZACIÓN Y REDIRECCIONAMIENTO (NUEVO)
        # ==========================================================================
        # Antes de cargar nada, verificamos si las etiquetas actuales son válidas
        # para la categoría a la que estamos entrando.
        
        if category:
            # Capturamos todas las etiquetas de la URL (incluyendo repetidos)
            raw_tags = request.httprequest.args.getlist('tags')
            current_tag_ids = []
            
            # Limpieza básica para obtener IDs enteros
            for t_val in raw_tags:
                for p in t_val.split(','):
                    if p.isdigit():
                        current_tag_ids.append(int(p))
            
            if current_tag_ids:
                # Buscamos estas etiquetas en BD
                tags_objects = request.env['product.tag'].sudo().browse(current_tag_ids)
                valid_tag_ids = []
                dirty = False # Bandera: ¿Encontramos una etiqueta intrusa?
                
                for tag in tags_objects:
                    # ES VÁLIDA SI:
                    # 1. Es Global (no tiene categorías asignadas)
                    # 2. O pertenece explícitamente a la categoría actual
                    if not tag.public_category_ids or category.id in tag.public_category_ids.ids:
                        valid_tag_ids.append(tag.id)
                    else:
                        # Si tiene categorías asignadas pero NO es la actual -> Es inválida
                        dirty = True
                
                # Si la URL está "sucia" con etiquetas inválidas, redirigimos
                if dirty:
                    new_params = post.copy()
                    
                    # Eliminamos el parámetro 'tags' viejo
                    if 'tags' in new_params: del new_params['tags']
                    
                    # Url base de la categoría
                    redirect_url = f"/shop/category/{category.id}"
                    
                    # Agregamos solo las etiquetas que sobrevivieron
                    if valid_tag_ids:
                        new_params['tags'] = ",".join(map(str, valid_tag_ids))
                    
                    # Reconstruimos la URL con los parámetros restantes (search, etc.)
                    if new_params:
                        redirect_url += "?" + url_encode(new_params)
                    
                    return request.redirect(redirect_url)

        # ==========================================================================
        # 2. EJECUCIÓN ORIGINAL
        # ==========================================================================
        response = super(WebsiteSaleTagFilter, self).shop(page=page, category=category, search=search, ppg=ppg, **post)

        # ==========================================================================
        # 3. CORRECCIÓN DE LA BARRA LATERAL (TU CÓDIGO)
        # ==========================================================================
        if response and hasattr(response, 'qcontext'):
            current_category = response.qcontext.get('category')
            
            tags_domain = []

            if current_category:
                # CASO A: Estamos dentro de una Categoría
                # Mostrar etiquetas Globales (vacías) O asignadas a esta categoría.
                tags_domain = [
                    '|', 
                    ('public_category_ids', '=', False),
                    ('public_category_ids', 'in', current_category.id)
                ]
            else:
                # CASO B: Estamos en la raíz "Todas las categorías"
                # Mostrar TODAS las etiquetas
                tags_domain = [] 

            # Forzamos la búsqueda para llenar la barra lateral
            all_tags = request.env['product.tag'].search(tags_domain)
            
            if all_tags:
                response.qcontext['all_tags'] = all_tags

        return response