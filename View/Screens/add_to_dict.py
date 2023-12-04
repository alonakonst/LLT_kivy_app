from kivy.uix.screenmanager import Screen
from Controller import AddToDictController
class AddToDict(Screen):

    selected_translations = []
    def __init__(self, **kwargs):
        self.controller = AddToDictController()
        self.fields_cleared = False
        super().__init__(**kwargs)

    def insert(self):
        #checks the conditions for all the required fields to insert into dictionary
        if AddToDict.check_conditions(self):
            #retrieves word/phrase
            text = self.ids.word.text

            #retriewes and formats list of translations
            AddToDict.translation_selection(self)
            translation = ', '.join(self.selected_translations)

            #retireves notes
            notes = self.ids.notes.text

            #communicaties with the model through controller
            self.controller.add_entry(text, translation, notes)
            AddToDict.clear_fields(self)

    # retrieves user's selection of the translation from bots APIs suggestion and user's input:
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
        self.ids.condition_message.text = ""

        #clearing out notes field
        self.ids.notes.text = ''

        AddToDict().fields_cleared = True

    #checks condition to submit dictionary entry
    def check_conditions(self):

        #checks if word/phrase is inserted
        if self.ids.word.text == '' and not self.fields_cleared:
            self.ids.word.hint_text = 'You should enter a word or a phrase'
            self.ids.word.hint_text_color = "darkred"
            return False


        #handles the case when user's translation field is empty but the checkbox is selected
        elif self.ids.users_checkbox.active and self.ids.users_translation.text=='':
            if self.ids.suggested_checkbox.active:
                self.ids.users_checkbox.active = False
                return True
        else:
            return True

    # set checkbox of user's translation checked when user presses on user's translation TextInput
    def users_checkbox_active(self):
        self.ids.users_checkbox.active=True

    def suggested_translation(self, text):

        self.controller.translate(text)

        self.ids.suggested_translation.text = f'the translation of {text}'