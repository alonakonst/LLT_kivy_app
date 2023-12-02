from Model import DictionaryEntry
from Model import TranslationService, TranslationServiceError

class AddToDictController:


    def add_entry(self, text, translation, notes):
        dictionary_entry = DictionaryEntry(text=text, translation=translation, notes=notes)
        dictionary_entry.save()

    def translate(self, text):
       # trasnlation = TranslationService().translate(text)
       # print(trasnlation)
        pass