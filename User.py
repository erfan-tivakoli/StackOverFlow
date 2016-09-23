__author__ = 'Rfun'

class User:
    instances = []

    def __init__(self, id):
        self.id = id
        self.questions = []
        self.answers = []
        User.instances.append(self)

    def add_question(self, question):
        self.questions.append(question)

    def add_answer(self, answer):
        self.answers.append(answer)

    def get_id(self):
        return self.id


def get_user_by_id(id):
    for user in User.instances:
        if user.get_id() == id:
            return user
    return None
