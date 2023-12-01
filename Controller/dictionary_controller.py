from Model import DictionaryEntry

class DictionaryController:

    def __init__(self,view):
        self.view = view
        #self.count = DictionaryEntry().select().count()

    #TODO write show dictionary entries method here
    def show_dictionary_entries(self):
        pass

    def remove_dictionary_entry(self, entry):
        dictionary_entry = DictionaryEntry.select().where(DictionaryEntry.id == entry.id).get()
        dictionary_entry.delete_instance()
