from odoo import models, fields, api


class Team(models.Model):
    _name = 'volleyball.team'

    name = fields.Char(string='Name')
    division = fields.Many2one('volleyball.division')
    players = fields.One2many('res.partner', 'id')

class Division(models.Model):
    _name ='volleyball.division'

    name = fields.Char(string='Name')
    cost = fields.Float(string='Cost')


