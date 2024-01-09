from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language
from django.utils import timezone
from django.conf import settings

from utils.models import State


class SportData(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("To'liq nomi [title]"))
    attr = models.CharField(max_length=255, verbose_name=_('qisqa nomi [attr]'))

    url = models.CharField(max_length=255, verbose_name=_('youtube url'))
    file = models.FileField(upload_to='files/', verbose_name=_('file'))

    views = models.IntegerField(default=0, verbose_name=_('ko\'rishlar soni'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('yaratilgan vaqti'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('tahrirlangan vaqti'))

    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name=_('holati'))

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(SportData, self).save(*args, **kwargs)
        return self

    def get_file_url(self):
        return settings.HOST + self.file.url

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
