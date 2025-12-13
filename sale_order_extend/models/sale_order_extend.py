from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SaleOrderExtend(models.Model):
    _inherit = 'sale.order'
    _description = "Extend Sale Order as per my requirements"

    custom_b = fields.Text(string="Payment Time Period", readonly=True)
    customer_order_count = fields.Integer(
        string="Total Number of orders this customer",
        compute="_compute_customer_order_count"
    )

    def test(self):
        pass

    @api.onchange('payment_term_id')
    def _onchange_payment_term_customb(self):
        for order in self:
            if order.payment_term_id:
                order.custom_b = f"Payment clearness '{order.payment_term_id.name}' Time."
            else:
                order.custom_b = ""

    @api.depends('partner_id')
    def _compute_customer_order_count(self):
        for order in self:
            if order.partner_id:
                order.customer_order_count = self.env['sale.order'].search_count([
                    ('partner_id', '=', order.partner_id.id)
                ])
            else:
                order.customer_order_count = 0


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    _description = "just wanna to add extra fields and logic"

    ab = fields.Binary(string="Product Image", compute='_compute_ab', store=True)

    @api.depends('product_id')
    def _compute_ab(self):
        for line in self:
            if line.product_id:
                line.ab = line.product_id.image_1920
            else:
                line.ab = False

    @api.constrains('product_uom_qty')
    def _check_qty_positive(self):
        for line in self:
            if line.product_uom_qty < 1:
                raise ValidationError("Quantity must be at least 1!")

    _sql_constraints = [
        ('check_positive_qty',
         'CHECK(product_uom_qty > 0)',
         'Quantity must be greater than zero!')
    ]
# <nnnnnnnn>