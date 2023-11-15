from Model import Quiz


class PractiseController:
    ANSWER_BUTTON_CORRECT_COLOR = (0, 1, 0, 1)
    ANSWER_BUTTON_INCORRECT_COLOR = (1, 0, 0, 1)

    def __init__(self):
        self.current_quiz = None
        self.correct_answer_index = None
        self.quiz_in_progress = True

    def generate_quiz(self) -> Quiz:
        """
        Returns a new quiz object
        :return:
        """
        self.current_quiz = Quiz("opgave", ['dinner', 'assignment', 'internship', 'youth card'])
        self.correct_answer_index = 1

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
        if self.is_answer_correct(answer_text):
            self.answer_button_on_correct(answer_button)
        else:
            self.answer_button_on_incorrect(answer_button)

        self.quiz_in_progress = False



    def is_answer_correct(self, answer_text: str) -> bool:
        """
        Returns True if the answer is correct and False otherwise
        :param answer_text:
        :return:
        """
        return answer_text == self.current_quiz.answers[self.correct_answer_index]

    def answer_button_on_correct(self, answer_button):
        """
        Determines what happens when the correct answer button is pressed
        :param answer_button:
        :return:
        """
        answer_button.background_color = self.ANSWER_BUTTON_CORRECT_COLOR

    def answer_button_on_incorrect(self, answer_button):
        """
        Determines what happens when the incorrect answer button is pressed
        :param answer_button:
        :return:
        """
        answer_button.background_color = self.ANSWER_BUTTON_INCORRECT_COLOR
