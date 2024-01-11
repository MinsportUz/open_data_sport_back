from modeltranslation.translator import translator, TranslationOptions

from app.models import SportData, LegislativeDocument, About


class SportDataTranslationOptions(TranslationOptions):
    fields = ('title', 'attr',)


class LegislativeDocumentTranslationOptions(TranslationOptions):
    fields = ('title', 'attr',)


class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


translator.register(SportData, SportDataTranslationOptions)
translator.register(LegislativeDocument, LegislativeDocumentTranslationOptions)
translator.register(About, AboutTranslationOptions)