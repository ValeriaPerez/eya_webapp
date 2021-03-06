# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from utils.models import BaseModel, CatalogModel

# Create your models here.
class Type(CatalogModel):
	pass


class Clasification(CatalogModel):
	pass


class Color(CatalogModel):
	pass

	def __unicode__(self):
		return u'{}-{}'.format(self.name, self.display_name)


class Family(BaseModel):
	code = models.CharField(verbose_name=u'Código', max_length=5)

	def __unicode__(self):
		return u'{}'.format(self.code)


class ModelProduct(BaseModel):
	code = models.CharField(verbose_name=u'Código', max_length=5)
	family_product = models.ForeignKey(Family, verbose_name='Familia', related_name='models')


class Product(BaseModel):
	code_eyamex = models.CharField(verbose_name=u'Código EYAMEX', max_length=20)
	type = models.ForeignKey(Type, verbose_name='Tipo', related_name='t_products')
	clasification = models.ForeignKey(Clasification, verbose_name=u'Clasificación', related_name='c_products')
	model = models.ForeignKey(ModelProduct, verbose_name='Modelo', related_name='m_products')
	code = models.CharField(verbose_name=u'Código', max_length=15)
	color = models.ForeignKey(Color, verbose_name='Color', related_name='cl_products')
	description = models.CharField(verbose_name=u'Descripción', max_length=255)

	def __unicode__(self):
		return u'{}'.format(self.code_eyamex)
