import logging
from werkzeug.urls import url_encode
from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

_logger = logging.getLogger(__name__)

class WebsiteSaleTagFilter(WebsiteSale):

    @http.route()
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        
        # --- CORRECCIÓN IMPORTANTE: BANDERA DE CONTEXTO ---
        # Marcamos que estamos en el catálogo principal.
        # El modelo leerá esto. Si no está esta marca (ej. en página de producto), no filtrará.
        request.is_viewing_shop = True

        # ==========================================================================
        # 1. SANITIZACIÓN (Tus comprobaciones originales)
        # ==========================================================================
        if category:
            raw_tags = request.httprequest.args.getlist('tags')
            current_tag_ids = []
            for t_val in raw_tags:
                for p in t_val.split(','):
                    if p.isdigit():
                        current_tag_ids.append(int(p))
            
            if current_tag_ids:
                tags_objects = request.env['product.tag'].sudo().browse(current_tag_ids)
                valid_tag_ids = []
                dirty = False
                
                for tag in tags_objects:
                    if not tag.public_category_ids or category.id in tag.public_category_ids.ids:
                        valid_tag_ids.append(tag.id)
                    else:
                        dirty = True
                
                if dirty:
                    new_params = post.copy()
                    if 'tags' in new_params: del new_params['tags']
                    redirect_url = f"/shop/category/{category.id}"
                    if valid_tag_ids:
                        new_params['tags'] = ",".join(map(str, valid_tag_ids))
                    if new_params:
                        redirect_url += "?" + url_encode(new_params)
                    return request.redirect(redirect_url)

        # ==========================================================================
        # 2. EJECUCIÓN ORIGINAL
        # ==========================================================================
        response = super(WebsiteSaleTagFilter, self).shop(page=page, category=category, search=search, ppg=ppg, **post)

        # ==========================================================================
        # 3. BARRA LATERAL
        # ==========================================================================
        if response and hasattr(response, 'qcontext'):
            current_category = response.qcontext.get('category')
            tags_domain = []

            if current_category:
                tags_domain = [
                    '|', 
                    ('public_category_ids', '=', False),
                    ('public_category_ids', 'in', current_category.id)
                ]
            else:
                tags_domain = [] 

            all_tags = request.env['product.tag'].search(tags_domain)
            if all_tags:
                response.qcontext['all_tags'] = all_tags

        return response