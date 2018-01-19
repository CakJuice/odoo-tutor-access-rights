# -*- coding: utf-8 -*-

"""
# Model untuk tutorial hak akses,
# author @CakJuice <hd.brandoz@gmail.com>
"""

from odoo import models, fields, api

class CJTutorAccessRight(models.Model):
	_name = 'cj_tutor.access_right'

	name = fields.Char(string="Nama", size=128, required=True)
	description = fields.Text(string="Description")
	state = fields.Selection([
		('draft', "Draft"),
		('valid', "Valid"),
		('refuse', "Refuse"),
	], string="Status", default='draft')

	@api.multi
	def action_draft(self):
		self.state = 'draft'

	@api.multi
	def action_valid(self):
		self.state = 'valid'

	@api.multi
	def action_refuse(self):
		self.state = 'refuse'