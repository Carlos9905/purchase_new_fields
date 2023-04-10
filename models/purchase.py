from odoo import models, fields, api

class Purchase(models.Model):
    _inherit = 'purchase.order'

    uso_cfdi = fields.Many2one("using.cfdi", string="Uso CFDI")
    forma_pago = fields.Many2one("forma.pago", string="Forma de pago")
    metodo_pago = fields.Many2one("metodo.pago", string="Metodo de pago")

class UsingCfdi(models.Model):
    _name = "using.cfdi"
    _rec_name = 'nombre'
    name = fields.Char("Código")
    valor = fields.Char("Valor")
    nombre = fields.Char("Nombre", compute="_get_name")

    @api.depends('name', 'valor')
    def _get_name(self):
        for nombre in self:
            if nombre.name and nombre.valor:
                nombre.nombre = '%s / %s' % (nombre.name, nombre.valor)
            else:
                nombre.nombre = nombre.name

class FormaPago(models.Model):
    _name = "forma.pago"
    _rec_name = 'nombre'
    name = fields.Char("Código")
    valor = fields.Char("Valor")

    nombre = fields.Char("Nombre", compute="_get_name")

    @api.depends('name', 'valor')
    def _get_name(self):
        for nombre in self:
            if nombre.name and nombre.valor:
                nombre.nombre = '%s / %s' % (nombre.name, nombre.valor)
            else:
                nombre.nombre = nombre.name

class MetodoPago(models.Model):
    _name = "metodo.pago"
    _rec_name = 'nombre'
    name = fields.Char("Código")
    valor = fields.Char("Valor")
    
    nombre = fields.Char("Nombre", compute="_get_name")

    @api.depends('name', 'valor')
    def _get_name(self):
        for nombre in self:
            if nombre.name and nombre.valor:
                nombre.nombre = '%s / %s' % (nombre.name, nombre.valor)
            else:
                nombre.nombre = nombre.name
    