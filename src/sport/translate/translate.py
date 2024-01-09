from modeltranslation.translator import translator, TranslationOptions

from sport.models import SportType


class SportTypeTranslationOptions(TranslationOptions):
    fields = ('title', 'attr',)


translator.register(SportType, SportTypeTranslationOptions)
