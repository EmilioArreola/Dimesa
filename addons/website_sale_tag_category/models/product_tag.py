from odoo import models, fields

class ProductTag(models.Model):
    _inherit = 'product.tag'

    public_category_ids = fields.Many2many(
        'product.public.category',
        string="Categorías Permitidas",
    )
    
    # Nuevo campo para agrupar la lógica OR
    filter_group_name = fields.Char(
        string="Nombre del Grupo de Filtro",
        help="Las etiquetas con el mismo nombre de grupo usarán lógica 'O' entre ellas (ej: Escritorio o Silla). Etiquetas de grupos distintos usarán lógica 'Y' (ej: Silla y Descuento)."
    )