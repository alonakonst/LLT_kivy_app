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

        dictionary_entry_result_set = DictionaryEntry.select()

        # check if there is enough dictionary entries to create a quiz
        if len(dictionary_entry_result_set) < 4:
            self.current_quiz = Quiz('frokost', ['lunch', 'dinner', 'breakfast', 'fresh'], 0)
            return self.current_quiz

        # creates a dictionary of four random words from the database and their translations
        quiz_set = {}
        for question in dictionary_entry_result_set.order_by(fn.Random()).limit(4):
            quiz_set[question.text] = question.translation

        # selects one question word from quiz_set
        index = random.randint(0, 3)
        question = list(quiz_set)[index]

        self.current_quiz = Quiz(question,  list(quiz_set.values()), index)

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





