from Badge import Badge

__author__ = 'Rfun'
import os
import re
from User import *
from Question import *
from Answer import *
from tqdm import tqdm
from matplotlib import pyplot as plt
import pickle
from Badge import *


def read_datas():
    for file_name in tqdm(os.listdir('./Sample_datas')[:12]):
        with open('Sample_datas/' + file_name) as f:
            lines = f.readlines()
            file_infos = re.split('\.|\_', file_name)

            # Creating user, if it's not created already
            user = get_user_by_id(file_infos[0])
            if user is None:
                user = User(file_infos[0])

            if len(file_infos) == 3:
                if file_infos[1] == 'q':
                    for line in lines:
                        question_infos = re.split('\-|\,', line)
                        question = get_question_by_id(question_infos[0])
                        if question is None:
                            question = Question(question_infos[0], question_infos[1], user)
                        user.add_question(question)
                elif file_infos[1] == 'a':
                    for line in lines:
                        answer_infos = re.split('\-', line)
                        answer = get_answer_by_id(answer_infos[0])
                        if answer is None:
                            answer = Answer(answer_infos[0], answer_infos[1], answer_infos[2], user)
                        user.add_answer(answer)

    for file_name in tqdm(os.listdir('./Sample_datas')[:12]):
        with open('Sample_datas/' + file_name) as f:
            lines = f.readlines()
            file_infos = re.split('\.|\_', file_name)

            if len(file_infos) == 4:
                if file_infos[1] == 'q':
                    for line in lines:
                        line_infos = re.split('\:', line)
                        question = get_question_by_id(line_infos[0])
                        for item in re.split('\;', line_infos[1]):
                            answer_infos = re.split('\-', item)
                            # We don't create the user if it's not already exist
                            answer = get_answer_by_id(answer_infos[1])
                            user = get_user_by_id(answer_infos[0])
                            if answer is None:
                                if answer_infos[3] == 'm':
                                    answer = Answer(answer_infos[1], question.id, answer_infos[2], user)
                                else:
                                    answer = Answer(answer_infos[1], None, answer_infos[2], user)
                            question.add_next_answer(answer)
                elif file_infos[1] == 'a':
                    for line in lines:
                        line_infos = re.split('\:', line)
                        answer = get_answer_by_id(line_infos[0])
                        for item in re.split('\;', line_infos[1]):
                            question_infos = re.split('\-', item)
                            question = get_question_by_id(question_infos[0])
                            user = get_user_by_id(question_infos[1])
                            if question is None:
                                question = Question(question_infos[1], question_infos[2], user)
                            answer.add_past_question(question)
    for file_name in os.listdir('./Badge_infos'):
        with open('./Badge_infos/' + file_name, 'r+') as f:
            lines = f.readlines()
            for line in lines:
                user_id = re.split('\:', line)[0]
                user = get_user_by_id(user_id)
                if user is not None:
                    date = re.split('\:', line)[1]
                    badge = Badge(user, date, get_enum_from_string(re.split('\.', file_name)[0]))
                    user.add_badge(badge)


def main():
    read_datas()

    with open('./pickled/users.pkl', 'wb') as f:
        pickle.dump(User.instances, f, protocol=2)
    with open('./pickled/quesions.pkl', 'wb') as f:
        pickle.dump(Question.instances, f, protocol=2)
    with open('./pickled/answers.pkl', 'wb') as f:
        pickle.dump(Answer.instances, f, protocol=2)


if __name__ == '__main__':
    main()