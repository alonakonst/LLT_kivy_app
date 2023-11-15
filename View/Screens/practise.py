from kivy.uix.screenmanager import Screen
import os
from kivy.lang import Builder

from Model import Quiz

from Controller import PractiseController


class Practise(Screen):

    DEFAULT_BUTTON_COLOR = [1, 1, 1, 1]
    ANSWER_BUTTON_CORRECT_COLOR = [0, 1, 0, 1]
    ANSWER_BUTTON_INCORRECT_COLOR = [1, 0, 0, 1]

    def __init__(self, **kwargs):
        self.next_button = None
        self.controller = PractiseController(self)
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
        """
        Set's the quiz on the screen
        :param quiz: the quiz to be set
        :return:
        """
        self.ids.question.text = f"Which of the following is the best translation for: {quiz.question!r}"

        for answer_button, answer_text in zip(self.ids.answer_button_layout.children, quiz.answers):
            answer_button.background_color = self.DEFAULT_BUTTON_COLOR
            answer_button.text = answer_text

    def enable_next_button(self):
        self.ids.next_button.opacity = 1
        self.ids.next_button.disabled = False

    def disable_next_button(self):
        self.ids.next_button.opacity = 0
        self.ids.next_button.disabled = True

    def on_correct_answer(self, answer_button):
        answer_button.background_color = self.ANSWER_BUTTON_CORRECT_COLOR

    def on_incorrect_answer(self, answer_button):
        answer_button.background_color = self.ANSWER_BUTTON_INCORRECT_COLOR


Builder.load_file(os.path.join(os.path.dirname(__file__), "practise.kv"))
