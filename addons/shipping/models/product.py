# -*- coding: utf-8 -*-
from datetime import date #) ini harus di import apabila ada field date & datetime pada tabel model database
from openerp import models, fields, api #) wajib iye mh titik
from openerp.exceptions import ValidationError #) ini harus di import apabila akan memunculkan error message

class product(models.Model):
	_name = 'shipping.products' #) nama ini akan menjadi nama tabel, bisa di relasikan dengan model lain. eg: shipping.route
	_rec_name = 'name' #) ini untuk breadcumb
	_description = "Master data Produk Penyiapan Jalur"
	_sql_constraints = [('code_uniq', 'unique(code)', "Kode Product Musti Beda !!")]

	name = fields.Char(string='Nama Produk', required=True, select=1, index=True)
	code = fields.Char(string='Kode Produk', help='buat kolom kode bro..')
	is_not_ppn = fields.Boolean(string='Bebas PPN', default=True, help='true false juga boleh')
	last_purchase_price = fields.Float(digits=(10, 5))
	default_discount = fields.Float(digits=(10, 5), default='0')
	last_purchase_price = fields.Float(digits=(10, 5))
	point = fields.Integer(string='Poin', default='1')
	type_product = fields.Selection([('Persediaan', 'Persediaan'), ('Aset', 'Aset'), ('Meneketehe', 'Meneketehe')], 'Type Produk', default='Persediaan')
	status = fields.Boolean(string='Status', default=True, help='delete udah di hapus bearti')
	description = fields.Text(string='Keterangan', help='ini buat isi keterangan') #) help bila di hover, akan memunculkan isi message nya
	image = fields.Binary("Image", attachment=True) #) jika attachment true maka tidak akan membuat field image di tabel product, tetapi akan menggunakan relasi tabel sebagai lokasi menyimpan image (default ke tabel ir.attachment --> belum tau kenapa kesini dan cara merubahnya), jika attachment false maka akan membuat field image di tabel product
	image_small = fields.Binary("Small-sized image", attachment=True) #) harus nya ini jadi image ukuran medium & kecil, tapi belum tau caranya, masih pabeulit manggil fungsinya
	image_medium = fields.Binary("Medium-sized image", attachment=True)
	state = fields.Selection([('concept', 'Concept'),  ('started', 'Started'), ('progress', 'In progress'), ('finished', 'Done'), ], default='concept')

	@api.one #) mungkin @api.one harus di tulis di setiap fungsi nya
	def concept_progressbar(self):
		self.write({'state': 'concept'})

	@api.one
	def started_progressbar(self):
		self.write({'state': 'started'})

	@api.one
	def progress_progressbar(self):
		self.write({'state': 'progress'})

	@api.one
	def done_progressbar(self):
		self.write({'state': 'finished'})
