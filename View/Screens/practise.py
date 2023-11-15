from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
import os
from kivy.lang import Builder

from Model import Quiz

from Controller import PractiseController


class Practise(Screen):
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
            answer_button.text = answer_text

    def answer(self, answer_button):
        self.controller.answer_button_on_press(answer_button)
        quiz = self.controller.generate_quiz()

        self.set_quiz(quiz)

    def create_next_button(self):
        self.next_button = Button(text='Next', size_hint=(0.4, 0.1), pos_hint={'x': 0.3, 'y': 0.6}, on_press=self.controller.on_next_button_press)
        self.add_widget(self.next_button)

    def remove_next_button(self):
        self.remove_widget(self.next_button)


Builder.load_file(os.path.join(os.path.dirname(__file__), "practise.kv"))
