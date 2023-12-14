from odoo import models,fields,api
from datetime import date
from dateutil.relativedelta import relativedelta

class WebStudent(models.Model):
    _name='web.student2'
    _description='The good models'


    priority=fields.Selection([('0','Normal'),('1','Low'),('2','High'),('3','Very High')],string='priority')
    name=fields.Char(string="NAME")
    sid=fields.Char(string='SID')
    group=fields.Selection([('a','a'),('b','b')],string='group')
    gender=fields.Selection([('male','MALE'),('female','FEMALE')],string='gender')
    hoby_id=fields.Many2one('web.hobyx2',string='hoby')
    types=fields.Char(string='types')
    dob=fields.Date(string='Date of Birth')
    age=fields.Integer(string='Age',compute='_compute_age')

    @api.depends('dob')
    def _compute_age(self):
        self.age=False
        for rec in self:
            rec.age=relativedelta(date.today(),rec.dob).years


    count_list = fields.Integer(string='count_list',compute='_compute_count_list')

    def _compute_count_list(self):
        self.count_list=10


    @api.onchange('group')
    def _onchange_group(self):
        if self.group=='a':
            self.gender='male'
        else:
            self.gender='female'


    @api.onchange('hoby_id')
    def _onchange_name(self):
        if self.hoby_id:
            self.types=self.hoby_id.type

