from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

class WebsiteSaleTagFilter(WebsiteSale):

    def _get_search_domain(self, search, category, attrib_values, search_in_description=True):
        domain = super(WebsiteSaleTagFilter, self)._get_search_domain(search, category, attrib_values, search_in_description)
        
        tags_param = request.params.get('tags')
        if tags_param:
            tag_ids = [int(tag_id) for tag_id in tags_param.split(',')]
            
            # Buscamos los objetos etiqueta para saber su grupo
            tags = request.env['product.tag'].sudo().browse(tag_ids)
            
            # Diccionario para agrupar: {'Tipo de Mueble': [1, 2], 'Estado': [5]}
            grouped_tags = {}
            
            for tag in tags:
                # Si tiene nombre de grupo, usamos ese nombre como clave.
                # Si NO tiene grupo, usamos su ID único como clave (para forzar AND estricto en etiquetas sueltas)
                key = tag.filter_group_name or f"uncategorized_{tag.id}"
                
                if key not in grouped_tags:
                    grouped_tags[key] = []
                grouped_tags[key].append(tag.id)
            
            # Construimos el dominio
            # Cada vuelta del bucle agrega una condición AND al dominio general
            # Pero dentro de la lista 'in', Odoo aplica OR.
            for key, t_ids in grouped_tags.items():
                domain.append(('all_product_tag_ids', 'in', t_ids))
                
        return domain

    # Mantenemos el filtrado visual (shop) igual que antes
    @http.route()
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        response = super(WebsiteSaleTagFilter, self).shop(page=page, category=category, search=search, ppg=ppg, **post)

        if response and hasattr(response, 'qcontext'):
            tags = response.qcontext.get('all_tags')
            current_category = response.qcontext.get('category')

            if tags:
                if current_category:
                    tags = tags.filtered(lambda t: 
                        not t.public_category_ids 
                        or current_category.id in t.public_category_ids.ids
                    )
                else:
                    tags = tags.filtered(lambda t: not t.public_category_ids)
                response.qcontext['all_tags'] = tags
        
        return response