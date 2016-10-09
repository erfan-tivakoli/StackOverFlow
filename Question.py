class Question:
    instances = []
    ids_index = {}

    def __init__(self, id, timestamp, owner, tag):
        self.id = id
        self.timestamp = timestamp
        self.owner_id = owner.id if (owner is not None) else None
        self.tag = tag
        self.next_answers = []
        self.instances.append(self)
        self.ids_index[self.id] = len(Question.instances) - 1

    def add_next_answer(self, answer):
        self.next_answers.append(answer.id)


def get_question_by_id(id):
    try:
        return Question.instances[Question.ids_index[id]]
    except:
        return None