# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from random import randint

from django.db import models

from imagekit.models import ProcessedImageField
from imagekit.processors import SmartResize
from utils.models import BaseModel, CatalogModel


def get_image_path(instance, filename):
    ext = filename.decode('utf-8').split('.')[-1]
    return 'product/{0}/{1}.{2}'.format(instance.code_eyamex, instance.code_eyamex, ext)


# Create your models here.
class Type(CatalogModel):
    pass

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'


class Clasification(CatalogModel):
    pass

    class Meta:
        verbose_name = u'Clasificación'
        verbose_name_plural = u'Clasificaciones'


class Color(CatalogModel):
    pass

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colores'

    def __unicode__(self):
        return u'{}-{}'.format(self.name, self.display_name)


class Family(BaseModel):
    code = models.CharField(verbose_name=u'Código', max_length=5)
    description = models.TextField(verbose_name=u'Descripción')

    class Meta:
        verbose_name = 'Familia'
        verbose_name_plural = 'Familias'

    def __unicode__(self):
        return u'{}'.format(self.code)


class ModelProduct(BaseModel):
    code = models.CharField(verbose_name=u'Código', max_length=5)
    family_product = models.ForeignKey(Family, verbose_name='Familia', related_name='models')

    class Meta:
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'

    def __unicode__(self):
        return u'{}'.format(self.code)


class Product(BaseModel):
    code_eyamex = models.CharField(verbose_name=u'Código EYAMEX', max_length=20)
    image = ProcessedImageField(
        upload_to=get_image_path, format='JPEG',
        processors=[SmartResize(994, 660)], options={'quality': 100},
        verbose_name=u"Imagen", null=True)
    type = models.ForeignKey(Type, verbose_name='Tipo', related_name='t_products')
    clasification = models.ForeignKey(Clasification, verbose_name=u'Clasificación', related_name='c_products')
    model = models.ForeignKey(ModelProduct, verbose_name='Modelo', related_name='m_products')
    code = models.CharField(verbose_name=u'Código', max_length=15)
    color = models.ForeignKey(Color, verbose_name='Color', related_name='cl_products')
    description = models.CharField(verbose_name=u'Descripción', max_length=255)
    meta_description = models.TextField()
    is_new = models.BooleanField(verbose_name='¿Es nuevo?')
    home_is_new = models.BooleanField(verbose_name='¿Es nuevo aparece en banner?', default=False)
    best_seller = models.BooleanField(verbose_name=u'¿Más vendido?')
    home_best_seller = models.BooleanField(verbose_name=u'¿Más vendido aparece en banner?', default=False)
    spent = models.BooleanField(verbose_name='¿Agotado?')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __unicode__(self):
        return u'{}'.format(self.code_eyamex)

    def fill_meta(self):
        meta_description = u'{} {} {} {} {} {} {} {}'.format(
            self.code_eyamex, self.clasification.name, self.model.code,
            self.model.family_product.code, self.code, self.color.name,
            self.description, self.model.family_product.description)
        return meta_description.lower()

    def save(self, *args, **kwargs):
        self.meta_description = self.fill_meta()
        super(Product, self).save(*args, **kwargs)

    def get_products_related(self):
        ids = list()
        size = 0
        related = Product.objects.filter(
            model__family_product=self.model.family_product,
            clasification=self.clasification).exclude(pk=self.pk)
        while size < 5:
            index = randint(0, len(related) - 1)
            prd = related[index]
            if prd.pk not in ids:
                ids.append(prd.pk)
            size = len(ids)
        return related.filter(id__in=ids)
