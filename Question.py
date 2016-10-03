
class Question:

    instances = []

    def __init__(self, id, timestamp, owner):
        self.id = id
        self.timestamp = timestamp
        self.owner = owner
        self.next_answers = []
        self.instances.append(self)

    def add_next_answer(self, answer):
        self.next_answers.append(answer)


def get_question_by_id(id):
    for question in Question.instances:
        if question.id == id:
            return question

    return None