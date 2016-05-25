# -*- coding: utf-8 -*-

from openerp import models, fields, api

class equipo(models.Model):
    _name = 'modulo_partidos.equipo'
    name = fields.Char(string="Nombre", size=50)
    presupuesto=fields.Float(string="Presupuesto")
    anio_fundacion=fields.Integer(string="Año")
    jugador=fields.Many2one('modulo_partidos.jugador')
# partido=fields.One2many(comodel_name='modulo_partidos.partido',inverse_name='rival')
# entrenador=fields.Many2one('modulo_partidos.entrenador')
class jugador(models.Model):
    _name = 'modulo_partidos.jugador'
    name = fields.Char(string="Nombre", size=50)
    posicion=fields.Selection([("POR","Portero"),("DEF","Defensa"),("CEN","Centrocampista"),("DEL","Delantero")])
    numero=fields.Integer(string="Numero")
    edad=fields.Integer(string="Edad")
    equipo=fields.One2many(comodel_name='modulo_partidos.equipo',inverse_name='jugador')
 #class entrenador(models.Model):
#  _name = 'modulo_partidos.entrenador'
#	name = fields.Char(string="Nombre", size=50)
#	edad=fields.Integer(string="Edad")
#   partidosGanados=fields.Integer(string="Partidos Ganados")
#   partidosPerdido=fields.Integer(string="Partidos Perdidos")
#equipo=fields.Many2one('modulo_partidos.equipo')



 #class partido(models.Model):
 #	_name = 'modulo_partidos.partido'
 #	rival=fields.Many2one('modulo_partidos.equipo')
 #	fecha=fields.Date(string="Fecha del encuentro")
 #	resultado=fields.Selection([("V","Victoria"),("E","Empate"),("D","Derrota")])
 #	lugar=fields.Selection([("L","Local"),("V","Visitante")])

    
		
		