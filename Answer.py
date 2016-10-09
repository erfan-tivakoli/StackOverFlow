import traceback

__author__ = 'Rfun'


class Answer:
    instances = []
    ids_index = {}

    def __init__(self, id, parent_id, timestamp, owner):
        self.id = id
        self.parent_id = parent_id
        self.timestamp = timestamp
        self.owner_id = owner.id if (owner is not None) else None
        self.past_questions = []
        self.instances.append(self)
        self.ids_index[self.id] = len(Answer.instances) - 1

    def add_past_question(self, question):
        self.past_questions.append(question.id)


def get_answer_by_id(id):
    try:
        return Answer.instances[Answer.ids_index[id]]
    except:
        return None