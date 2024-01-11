from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language
from django.utils import timezone
from django.conf import settings

from utils.models import State
from sport.models import SportType


class SportData(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("To'liq nomi [title]"))
    attr = models.CharField(max_length=255, verbose_name=_('Qisqa nomi [attr]'))

    url = models.CharField(max_length=255, verbose_name=_('Youtube url'))
    file = models.FileField(upload_to='files/', verbose_name=_('file'))

    views = models.IntegerField(default=0, verbose_name=_('Ko\'rishlar soni'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Yaratilgan vaqti'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Tahrirlangan vaqti'))

    image = models.ImageField(upload_to='images/', verbose_name=_('Rasm'), null=True, blank=True)
    author = models.CharField(max_length=255, verbose_name=_('Muallif'), null=True, blank=True)
    published_at = models.DateField(verbose_name=_('Chop etilgan vaqti'), null=True, blank=True)
    publisher = models.CharField(max_length=255, verbose_name=_('Nashriyot'), null=True, blank=True)

    state = models.ForeignKey(State, on_delete=models.SET_NULL, verbose_name=_('Holati'), null=True)
    sport_type = models.ForeignKey(SportType, on_delete=models.SET_NULL, verbose_name=_('Sport turi'), null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        if self.url:
            self.url = self.url.replace('watch?v=', 'embed/')
        super(SportData, self).save(*args, **kwargs)
        return self

    def get_file_url(self):
        return settings.HOST + self.file.url

    def get_image_url(self):
        return settings.HOST + self.image.url

    def get_file_name(self):
        return self.file.name.split('/')[-1]

    def increase_views(self):
        self.views += 1
        self.save()
        return self

    class Meta:
        verbose_name = _('Sport ma\'lumotlari')
        verbose_name_plural = _('Sport ma\'lumotlari')
        db_table = 'sport_data'
        indexes = [
            models.Index(fields=['sport_type', 'state', 'created_at']),
        ]


class LegislativeDocument(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("To'liq nomi [title]"))
    attr = models.CharField(max_length=255, verbose_name=_('Qisqa nomi [attr]'))

    url = models.CharField(max_length=255, verbose_name=_('Lex url'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Yaratilgan vaqti'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Tahrirlangan vaqti'))

    state = models.ForeignKey(State, on_delete=models.SET_NULL, verbose_name=_('Holati'), null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(LegislativeDocument, self).save(*args, **kwargs)
        return self

    class Meta:
        verbose_name = _('Qonun hujjatlari')
        verbose_name_plural = _('Qonun hujjatlari')
        db_table = 'legislative_document'
