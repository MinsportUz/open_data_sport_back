from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language
from django.utils import timezone
from django.conf import settings

from utils.models import State


class SportType(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("To'liq nomi [title]"))
    attr = models.CharField(max_length=255, verbose_name=_('qisqa nomi [attr]'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('yaratilgan vaqti'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('tahrirlangan vaqti'))

    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name=_('holati'))

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(SportType, self).save(*args, **kwargs)
        return self

    class Meta:
        verbose_name = _('Sport turi')
        verbose_name_plural = _('Sport turlari')
        db_table = 'sport_type'