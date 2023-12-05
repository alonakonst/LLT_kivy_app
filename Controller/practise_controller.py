import random

from kivy.properties import ObjectProperty
from peewee import fn

from Model import Quiz
from Model import DictionaryEntry

class PractiseController:

    question_word = str
    answer_word = str

    def __init__(self, view):
        self.view = view
        self.current_quiz: Quiz = None
        self.quiz_in_progress = True
        self.quiz_set = {}
        self.question_word = str
        self.answer_word = str

    def generate_quiz(self) -> Quiz:
        """
        Returns a new quiz object
        :return:
        """

        PractiseController.generate_quiz_set(self)


        print(PractiseController.quiz_set)
        print(PractiseController.question_word)
        print(PractiseController.answer_word)
        print(f'length of list = {len(list(PractiseController.quiz_set.values()))}')
        thelist = list(PractiseController.quiz_set.values())


        self.current_quiz = Quiz(PractiseController.question_word, thelist, 1)

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
            self.view.on_incorrect_answer(answer_button)

        self.quiz_in_progress = False

        self.view.enable_next_button()

    def next_button_on_press(self):
        self.view.set_quiz(self.current_quiz)
        
        self.view.disable_next_button()

        self.quiz_in_progress = True

    def generate_quiz_set(self):
        quiz_set = {}
        for question in DictionaryEntry.select().order_by(fn.Random()).limit(4):
            quiz_set[question.text] = question.translation
        index = random.randint(0, 3)
        question_word = list(quiz_set)[index]
        answer_word = list(quiz_set.values())[index]

        PractiseController.quiz_set = quiz_set
        PractiseController.question_word = question_word
        PractiseController.answer_word = answer_word



