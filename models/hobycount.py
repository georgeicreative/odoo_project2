from odoo import api,fields,models

class HobyCount(models.Model):
    _name='web.hobycount'
    _description='The good hobby list'

    hobyname_id=fields.Many2one('web.hobyx2',string='Hobyname_id')
    hobycount=fields.Integer(string='HobyCount',compute='_compute_hobycount')

    def _compute_hobycount(self):
        for rec in self:
            rec.hobycount=self.env['web.student2'].search_count([('hoby_id','=',rec.id)])
