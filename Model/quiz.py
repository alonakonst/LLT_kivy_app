"""
This is a Quiz class, it stores a question and 4 answers
"""
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Quiz:
    question: str
    answers: List[str]
    correct_answer_index: int

    def __post_init__(self):
        if len(self.answers) != 4:
            raise ValueError(f"answer List must be of length 4, not {len(self.answers)}")

        if self.correct_answer_index < 0 or self.correct_answer_index >= 4:
            raise ValueError(f"correct_answer_index must be between 0 and 3, not {self.correct_answer_index}")

    def is_correct_answer(self, answer):
        return self.answers[self.correct_answer_index] == answer
