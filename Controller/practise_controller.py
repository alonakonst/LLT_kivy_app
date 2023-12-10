import random
from peewee import fn

from Model import Quiz
from Model import DictionaryEntry

class PractiseController:

    def __init__(self, view):
        self.view = view
        self.current_quiz: Quiz = None
        self.quiz_in_progress = True
        #self.answer = str

    def generate_quiz(self) -> Quiz:
        """
        Returns a new quiz object
        :return:
        """

        dictionary_entries = []
        # iterate over the dictionary entries that have a translation
        for dictionary_entry in DictionaryEntry.select().where(DictionaryEntry.translation is not None):
            # exclude dictionary entries that have a space in them (i.e. they are composed of multiple words)
            if ' ' not in dictionary_entry.text:
                # ignore empty translation
                if dictionary_entry.translation == '': continue
                dictionary_entries.append(dictionary_entry)

        # shuffle the list
        random.shuffle(dictionary_entries)
        
        if len(dictionary_entries) < 4:
            self.current_quiz = Quiz('frokost', ['lunch', 'dinner', 'breakfast', 'fresh'], 0)
            return self.current_quiz

        # randomly pick the answer among the first 4
        answer_index = random.randint(0, 3)
        question = dictionary_entries[answer_index].text
        # the first 4 words will make the quiz
        answers = [dictionary_entry.translation for dictionary_entry in dictionary_entries[:4]]
        quiz = Quiz(question, answers, answer_index)

        self.current_quiz = quiz

        return self.current_quiz

    def answer_button_on_press(self, answer_button):
        """
        Controls what happens on answer button press
        :param answer_button:
        :return:
        """
        if not self.quiz_in_progress:
            return


        answer_text = answer_button.text
        if self.current_quiz.is_correct_answer(answer_text):
            self.view.on_correct_answer(answer_button)
        else:
            answer = self.current_quiz.correct_answer()
            self.view.on_incorrect_answer(answer_button, answer)

        self.quiz_in_progress = False

        self.view.enable_next_button()

    def next_button_on_press(self):
        self.view.set_quiz(self.current_quiz)
        
        self.view.disable_next_button()

        self.quiz_in_progress = True





