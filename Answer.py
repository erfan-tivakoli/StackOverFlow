__author__ = 'Rfun'


class Answer:
    instances = []

    def __init__(self, id, parent_id, timestamp):
        self.id = id
        self.parent_id = parent_id
        self.timestamp = timestamp
        self.instances.append(self)


def get_answer_by_id(id):
    for answer in Answer.instances:
        if answer.id == id:
            return answer

    return None