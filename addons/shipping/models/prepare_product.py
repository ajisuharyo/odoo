# -*- coding: utf-8 -*-
from datetime import date #) ini harus di import apabila ada field date & datetime pada tabel model database
from openerp import models, fields, api #) wajib iye mh titik
from openerp.exceptions import ValidationError #) ini harus di import apabila akan memunculkan error message

class prepare_product(models.Model):
	_name = 'shipping.prepare_products' #) nama ini akan menjadi nama tabel, bisa di relasikan dengan model lain. eg: shipping.route
	_rec_name = 'number' #) ini untuk breadcumb
	_description = "Penyiapan Jalur dari Sumbermas"
	_sql_constraints = [('title_uniq', 'unique(title)', "Judul Harus Uniq Bro !!")]
	_defaults = { 'transaction_date': fields.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

	def _get_default_number(self):
		return 1

	def _get_default_boolean(self):
		return False

	def _get_default_name(self):
		return "test"

	number = fields.Char(string='Nomor', required=True, select=1, index=True)
	title = fields.Char(string='Judul', help='buat kolom judul bro..', default="Judul", size=64)
	transaction_date = fields.Datetime()
	user_id = fields.Many2one('res.users', string='Pencatat') #) ini belongs_to
	country_id = fields.Many2one('res.country', string='Negara', default=101)
	lane_id = fields.Integer(string='Jalur ID', default=10)
	html = fields.Html()
	rate = fields.Integer(string='Rate', default=_get_default_number)
	status = fields.Boolean(string='Status Transaksi', default=True, help='true atau false gan ?')
	is_active = fields.Selection([('Ya', 'Ya'), ('Tidak', 'Tidak')], 'Aktif')
	reference = fields.Reference([('model_name', 'Reference I'), ('model_name', 'Reference II')])
	description = fields.Text(string='Keterangan', help='ini buat isi keterangan') #) help bila di hover, akan memunculkan isi message nya
	subtotal = fields.Float(digits=(10, 5))

	@api.depends('title')
	def _search_upper(self, operator, value):
		if operator == 'like':
			operator = 'ilike'
		return [('title', operator, value)]

	@api.constrains('title', 'description')
	def _check_description(self):
		if self.title == self.description:
			raise ValidationError("jangan sama gitu donk!")

	@api.constrains('rate') #) ini tidak tau kenapa harus di nyatakan 2x @api.contrains nya, ataukan memang harus seperti ini logic nya
	def _check_rate(self):
		if self.rate < 100:
			raise ValidationError("Rate Harus lebih dari 100 Bu..")

	@api.onchange('rate')
	def _check_change(self):
		self.lane_id = self.rate



