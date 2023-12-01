from Model import DictionaryEntry

class DictionaryController:

    def __init__(self,view):
        self.view = view

     #doesn't do anything
    def remove_dictionary_entry(view):
        DictionaryEntry().delete()
        print("entry deleted")
