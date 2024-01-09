from modeltranslation.translator import translator, TranslationOptions

from utils.models import State


class StateTranslationOptions(TranslationOptions):
    fields = ('title', 'attr',)


translator.register(State, StateTranslationOptions)