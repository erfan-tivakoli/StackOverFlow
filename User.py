__author__ = 'Rfun'

class User:
    instances = []
    ids_index = {}

    def __init__(self, id):
        #TODO : add the interest and experties here
        self.id = id
        self.questions = []
        self.answers = []
        self.badges = []
        User.instances.append(self)
        User.ids_index[self.id] = len(User.instances) - 1
        self.interests = {}
        self.experties = {}

    def add_question(self, question):
        self.questions.append(question)

    def add_answer(self, answer):
        self.answers.append(answer)

    def get_id(self):
        return self.id

    def add_badge(self, badge):
        self.badges.append(badge)


def get_user_by_id(id):
    try:
        return User.instances[User.ids_index[id]]
    except:
        return None