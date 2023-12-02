from Model import DictionaryEntry

class AddToDictController:


    def add_entry(self, text, translation, notes):
        dictionary_entry = DictionaryEntry(text=text, translation=translation, notes=notes)
        dictionary_entry.save()
