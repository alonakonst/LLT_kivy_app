"""
This is a Quiz class, it stores a question and 4 answers
"""
from typing import List
from dataclasses import dataclass


@dataclass(frozen=True)
class Quiz:
    question: str
    answers: List[str]

    def __post_init__(self):
        if len(self.answers) != 4:
            raise ValueError(f"answer List must be of length 4, not {len(self.answers)}")
