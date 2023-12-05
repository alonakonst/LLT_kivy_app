from Model import DictionaryEntry
from Model import TranslationService, TranslationServiceError

import os


class AddToDictController:

    def __init__(self):
        api_key = os.environ.get('API_KEY')

        if not api_key:
            api_key = ''

        self.translation_service = TranslationService(api_key=api_key)

    def add_entry(self, text, translation, notes):
        dictionary_entry = DictionaryEntry(text=text, translation=translation, notes=notes)
        dictionary_entry.save()

    def translate(self, text):
        #translation = TranslationService().translate(text)
        #print(translation)
        pass