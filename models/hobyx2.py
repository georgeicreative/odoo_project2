from odoo import models,fields,api

class WebHobyx(models.Model):
    _name='web.hobyx2'
    _description='The good models'

    name=fields.Char(string="HNAME")
    idh=fields.Char(string='IDH')
    type=fields.Selection([('indoor','indoor'),('outdoor','outdoor')])

