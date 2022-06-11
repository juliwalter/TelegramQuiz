import os
import helpers
from ctypes import Array
from random import randint
from pandas import read_csv

class quiz:
    # -----------------------------------------------------
    # -------------------- init method --------------------
    # -----------------------------------------------------
    def __init__(self) -> None:
        # Read questions from database/questions.csv
        self.questions = read_csv(
            'database/questions.csv',
            sep=';'
        )

        # Define the number of questions
        self.nb_questions = len(self.questions)

        # Define a random id as well as question, answer, and correct answer accordingly
        self.rand_ques_id = self.__random_id()
        self.question = self.__question()
        self.answers = self.__answers()
        self.correct_answer = self.__correct_answer()

    # ----------------------------------------------------
    # ------------------ public methods ------------------
    # ----------------------------------------------------
    # shuffle new random question from data base
    def shuffle_question(self) -> None:
        self.rand_ques_id = randint(1, self.nb_questions) - 1
        self.question = self.__question()
        self.answers = self.__answers()
        self.correct_answer = self.__correct_answer()
    
    # ----------------------------------------------------
    # ----------------- private methods ------------------
    # ----------------------------------------------------
    # returns a random question id
    def __random_id(self) -> int:
        return randint(1, self.nb_questions) - 1

    # returns the question according to rand_ques_id
    def __question(self) -> str:
        return self.questions.loc[self.rand_ques_id]['Question']

    # returns the answers according to rand_ques_id
    def __answers(self) -> Array:
        return [self.questions.loc[self.rand_ques_id][x] for x in ['A', 'B', 'C', 'D']]
    
    # returns the correct_answer according to rand_ques_id
    def __correct_answer(self) -> int:
        cor_ans = self.questions.loc[self.rand_ques_id]['Answer']
        mapping_ans = {
            'A': 0,
            'B': 1,
            'C': 2,
            'D': 3,
        }
        return mapping_ans[cor_ans]

class config:
    # -----------------------------------------------------
    # -------------------- init method --------------------
    # -----------------------------------------------------
    def __init__(self) -> None:
        self.telegram_token = os.environ.get("TELEGRAM_TOKEN", "")
        self.help_output = '/start - starts a quiz\n/help - outputs all commands and bot interactions\n/config - lets you config quiz parameters\n\nAny other message will be echoed!'
        self.open_period = 10

    # ----------------------------------------------------
    # ------------------ public methods ------------------
    # ----------------------------------------------------
    # setter for period
    def setter_open_period(self, period):
        self.open_period = period