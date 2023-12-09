from Model import DictionaryEntry

class DictionaryController:

    def show_dictionary_entries(self):
        return DictionaryEntry().select()

    def remove_dictionary_entry(self, entry):
        dictionary_entry = DictionaryEntry.select().where(DictionaryEntry.id == entry.id).get()
        dictionary_entry.delete_instance()
