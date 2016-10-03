__author__ = 'Rfun'


class Answer:
    instances = []

    def __init__(self, id, parent_id, timestamp, owner):
        self.id = id
        self.parent_id = parent_id
        self.timestamp = timestamp
        self.owner = owner
        self.past_questions = []
        self.instances.append(self)

    def add_past_question(self, question):
        self.past_questions.append(question)

def get_answer_by_id(id):
    for answer in Answer.instances:
        if answer.id == id:
            return answer

    return None