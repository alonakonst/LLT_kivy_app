from kivy.uix.screenmanager import Screen
import os
from kivy.lang import Builder

from Model import Quiz

from Controller import PractiseController


class Practise(Screen):
    def __init__(self, **kwargs):
        self.controller = PractiseController()
        super().__init__(**kwargs)

    def on_kv_post(self, base_widget):
        """
        This method is called after the kv file is loaded, this needs to be the case otherwise set_quiz cannot modify
        the screen
        :param base_widget:
        :return:
        """
        quiz = self.controller.generate_quiz()
        self.set_quiz(quiz)

    def set_quiz(self, quiz: Quiz):
        self.ids.question.text = quiz.question

        self.ids.answer0.text = quiz.answers[0]
        self.ids.answer1.text = quiz.answers[1]
        self.ids.answer2.text = quiz.answers[2]
        self.ids.answer3.text = quiz.answers[3]

    def answer(self, instance):

        quiz = self.controller.generate_quiz()

        self.set_quiz(quiz)


Builder.load_file(os.path.join(os.path.dirname(__file__), "practise.kv"))
