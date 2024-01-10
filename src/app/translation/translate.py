from modeltranslation.translator import translator, TranslationOptions

from app.models import SportData, LegislativeDocument


class SportDataTranslationOptions(TranslationOptions):
    fields = ('title', 'attr',)


class LegislativeDocumentTranslationOptions(TranslationOptions):
    fields = ('title', 'attr',)


translator.register(SportData, SportDataTranslationOptions)
translator.register(LegislativeDocument, LegislativeDocumentTranslationOptions)
