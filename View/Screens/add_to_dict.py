from kivy.uix.screenmanager import Screen
from Controller import AddToDictController
class AddToDict(Screen):

    selected_translations = []
    def __init__(self, **kwargs):
        self.controller = AddToDictController()
        self.fields_cleared = False
        super().__init__(**kwargs)

    def insert(self):

        #checks if word/phrase is typed
        if self.ids.word.text == '' and self.fields_cleared == False:
            self.ids.word.hint_text = 'You should enter a word or a phrase'
            self.ids.word.hint_text_color = "darkred"
        else:
            text = self.ids.word.text

            AddToDict.translation_selection(self)
            translation = ', '.join(self.selected_translations)

            notes = self.ids.notes.text

            self.controller.add_entry(text, translation, notes)
            AddToDict.clear_fields(self)

    # retrieves user's selection of the translation:
    def translation_selection(self):
        if self.ids.suggested_checkbox.active:
            AddToDict.selected_translations.append(self.ids.suggested_translation.text)

        if self.ids.users_checkbox.active:
            AddToDict.selected_translations.append(self.ids.users_translation.text)


    # clearing out all the fields when entry is submitted to the database
    def clear_fields(self):
        # clearing out word/phrase textfield
        self.ids.word.text = ''
        self.ids.word.hint_text = 'Enter a new word or phrase: '
        self.ids.word.hint_text_color = "darkgray"

        #clearing out translation
        AddToDict.selected_translations = []
        self.ids.users_translation.text = ''
        self.ids.suggested_translation.text = 'Suggested'
        self.ids.suggested_checkbox.active = False
        self.ids.users_checkbox.active = False

        #clearing out notes field
        self.ids.notes.text = ''

        AddToDict().fields_cleared = True
