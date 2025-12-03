import logging
from odoo import models, fields, api
from odoo.http import request

_logger = logging.getLogger(__name__)

class ProductTag(models.Model):
    _inherit = 'product.tag'

    public_category_ids = fields.Many2many(
        'product.public.category',
        string="Categorías Permitidas",
    )
    filter_group_id = fields.Many2one(
        'product.tag.group',
        string="Grupo de Filtro"
    )

class ProductTagGroup(models.Model):
    _name = 'product.tag.group'
    _description = 'Grupo de Filtros de Etiquetas'
    _order = 'name'
    name = fields.Char(string="Nombre del Grupo", required=True)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def _search(self, domain, *args, **kwargs):
        """
        Sobrescribimos _search para interceptar el dominio antes de llegar a la BD.
        """
        
        # Verificamos si estamos en la tienda web
        if request and request.httprequest and '/shop' in request.httprequest.path:
            
            # Captura robusta de etiquetas
            raw_tags = request.httprequest.args.getlist('tags')
            tag_ids = []
            for t_val in raw_tags:
                for p in t_val.split(','):
                    if p.isdigit():
                        tag_ids.append(int(p))

            if tag_ids:
                # A. LIMPIEZA
                # Eliminamos las reglas automáticas de Odoo.
                # Buscamos tanto 'all_product_tag_ids' como 'product_tag_ids' por seguridad.
                new_domain = []
                for leaf in domain:
                    if isinstance(leaf, (list, tuple)) and len(leaf) > 0 and leaf[0] in ['all_product_tag_ids', 'product_tag_ids']:
                        continue
                    new_domain.append(leaf)
                
                domain = new_domain

                # B. AGRUPAMIENTO
                tags = self.env['product.tag'].sudo().browse(tag_ids)
                grouped_tags = {}

                for tag in tags:
                    if tag.filter_group_id:
                        key = f"group_{tag.filter_group_id.id}"
                    else:
                        key = f"uncat_{tag.id}"
                    
                    if key not in grouped_tags:
                        grouped_tags[key] = []
                    grouped_tags[key].append(tag.id)

                # C. INYECCIÓN (CORREGIDA)
                # Aquí estaba el error. Usamos 'product_tag_ids' que es el campo real.
                for key, t_ids in grouped_tags.items():
                    domain.append(('product_tag_ids', 'in', t_ids))

        return super(ProductTemplate, self)._search(domain, *args, **kwargs)