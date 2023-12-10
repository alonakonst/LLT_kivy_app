from Model import DictionaryEntry
from Model import TranslationService, TranslationServiceError

import os


class AddToDictController:

    def __init__(self, view):
        self.view = view

        api_key = os.environ.get('API_KEY')

        if not api_key:
            api_key = ''

        self.translation_service = TranslationService(api_key=api_key)

    def add_entry(self, text, translation, notes):
        dictionary_entry = DictionaryEntry(text=text, translation=translation, notes=notes)
        dictionary_entry.save()

    def translate(self, text):
        try:
            translation = self.translation_service.translate(text)
            self.view.enable_checkbox()
            return translation
        except TranslationServiceError as e:
            return 'Translation Error'

    def refresh_button_on_press(self):
        word = self.view.get_word()

        if word:
            translation = self.translate(word)
            self.view.set_suggested_translation(translation)

