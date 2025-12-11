from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HostelAllocation(models.Model):
    _name = 'hostel.allocation'
    _description = 'Room Allocation'

    student_id = fields.Many2one('hostel.student', string='Student', required=True)
    room_id = fields.Many2one('hostel.room', string='Room', required=True)
    check_in_date = fields.Date(string='Check-in Date', required=True)
    check_out_date = fields.Date(string='Check-out Date')
    total_days = fields.Integer(string='Total Days', compute='_compute_total_days')
    total_price = fields.Float(string='Total Price', compute='_compute_total_price')

    @api.depends('check_in_date', 'check_out_date')
    def _compute_total_days(self):
        for rec in self:
            if rec.check_in_date and rec.check_out_date:
                delta = rec.check_out_date - rec.check_in_date
                rec.total_days = delta.days
            else:
                rec.total_days = 0

    @api.depends('total_days', 'room_id.price_per_day')
    def _compute_total_price(self):
        for rec in self:
            rec.total_price = rec.total_days * (rec.room_id.price_per_day or 0)




   # <jis room mai jitna persons ki avalibality hai os sa ziada student put krna pr error dega apko>
    @api.constrains('room_id')
    def _check_room_capacity(self):
        for allocation in self:
            # Count current allocations in this room
            current_allocations = self.search([
                ('room_id', '=', allocation.room_id.id)
            ])
            if allocation.room_id.capacity < len(current_allocations):
                raise ValidationError(
                    f"Room {allocation.room_id.name} cannot have more than {allocation.room_id.capacity} students."
                )
