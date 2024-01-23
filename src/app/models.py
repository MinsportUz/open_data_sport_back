from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language
from django.utils import timezone
from django.conf import settings
from django.db.models import F
import uuid

from utils.models import State
from sport.models import SportType

Languages = (
    ('uz', _('O\'zbek tili')),
    ('en', _('English')),
    ('ru', _('Russian')),
)


class SportData(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("To'liq nomi [title]"))
    attr = models.CharField(max_length=255, verbose_name=_('Qisqa nomi [attr]'))

    url = models.CharField(max_length=255, verbose_name=_('Youtube url'), null=True, blank=True)
    file = models.FileField(upload_to='files/', verbose_name=_('file'))

    views = models.IntegerField(default=0, verbose_name=_('Ko\'rishlar soni'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Yaratilgan vaqti'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Tahrirlangan vaqti'))

    image = models.ImageField(upload_to='images/', verbose_name=_('Rasm'), null=True, blank=True)
    author = models.CharField(max_length=255, verbose_name=_('Muallif'), null=True, blank=True)
    published_at = models.DateField(verbose_name=_('Chop etilgan vaqti'), null=True, blank=True)
    publisher = models.CharField(max_length=255, verbose_name=_('Nashriyot'), null=True, blank=True)

    language = models.CharField(max_length=2, choices=Languages, default=get_language, verbose_name=_('Til'), null=True,
                                blank=True)

    state = models.ForeignKey(State, on_delete=models.SET_NULL, verbose_name=_('Holati'), null=True)
    sport_type = models.ForeignKey(SportType, on_delete=models.SET_NULL, verbose_name=_('Sport turi'), null=True)

    uuid = models.UUIDField(default=uuid.uuid4, unique=True, verbose_name=_('UUID'))

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        if self.url:
            if 'watch?v=' in self.url:
                self.url = self.url.replace('watch?v=', 'embed/')
            elif 'youtu.be' in self.url:
                self.url = self.url.replace('youtu.be', 'youtube.com/embed')
        super(SportData, self).save(*args, **kwargs)
        return self

    def get_file_url(self):
        return settings.HOST + self.file.url

    def get_image_url(self):
        return settings.HOST + self.image.url

    def get_file_name(self):
        return self.file.name.split('/')[-1]

    def get_language_display(self):
        return dict(Languages)[self.language]

    def increase_views(self):
        self.views = F('views') + 1
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


class About(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("To'liq nomi [title]"))
    content = models.TextField(verbose_name=_('Ma\'lumot'))

    image = models.ImageField(upload_to='images/', verbose_name=_('Rasm'), null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Yaratilgan vaqti'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Tahrirlangan vaqti'))

    state = models.ForeignKey(State, on_delete=models.SET_NULL, verbose_name=_('Holati'), null=True)

    def __str__(self):
        return self.title

    def get_image_url(self):
        return settings.HOST + self.image.url

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(About, self).save(*args, **kwargs)
        return self

    class Meta:
        verbose_name = _('Tizim haqida')
        verbose_name_plural = _('Tizim haqida')
        db_table = 'about'


class Footer(models.Model):
    email = models.EmailField(verbose_name=_('Email'))
    phone = models.CharField(max_length=255, verbose_name=_('Telefon raqamlar'))
    address = models.CharField(max_length=255, verbose_name=_('Manzil'))
    logo = models.ImageField(upload_to='images/', verbose_name=_('Logo'), null=True, blank=True)
    facebook = models.URLField(verbose_name=_('Facebook manzili'), null=True, blank=True)
    instagram = models.URLField(verbose_name=_('Instagram manzili'), null=True, blank=True)
    telegram = models.URLField(verbose_name=_('Telegram manzili'), null=True, blank=True)
    youtube = models.URLField(verbose_name=_('Youtube manzili'), null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Yaratilgan vaqti'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Tahrirlangan vaqti'))

    state = models.ForeignKey(State, on_delete=models.SET_NULL, verbose_name=_('Holati'), null=True)

    def __str__(self):
        return self.email

    def get_logo_url(self):
        return settings.HOST + self.logo.url

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(Footer, self).save(*args, **kwargs)
        return self

    class Meta:
        verbose_name = _('Footer [saytni pastgi qismi]')
        verbose_name_plural = _('Footer [saytni pastgi qismi]')
        db_table = 'footer'