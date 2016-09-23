
class Question:

    instances = []

    def __init__(self, id, timestamp):
        self.id = id
        self.timestamp = timestamp
        self.instances.append(self)


def get_question_by_id(id):
    for question in Question.instances:
        if question.id == id:
            return question

    return None