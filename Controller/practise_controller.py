from Model import Quiz


class PractiseController:

    def __init__(self, view):
        self.view = view
        self.current_quiz: Quiz = None
        self.quiz_in_progress = True

    def generate_quiz(self) -> Quiz:
        """
        Returns a new quiz object
        :return:
        """
        self.current_quiz = Quiz("opgave", ['dinner', 'assignment', 'internship', 'youth card'], 1)

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
