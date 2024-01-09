from modeltranslation.translator import translator, TranslationOptions

from app.models import SportData


class SportDataTranslationOptions(TranslationOptions):
    fields = ('title', 'attr',)


translator.register(SportData, SportDataTranslationOptions)