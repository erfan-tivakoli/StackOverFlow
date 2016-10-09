__author__ = 'Rfun'

import os
import re
from User import *
from Question import *
from Answer import *
from tqdm import tqdm
import pickle
from Badge import *


def read_datas():

    for file_name in tqdm(os.listdir('./Sample_datas')):
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
                            question = Question(question_infos[0], question_infos[1], user, question_infos[2])
                        user.add_question(question)
                elif file_infos[1] == 'a':
                    for line in lines:
                        answer_infos = re.split('\-', line)
                        answer = get_answer_by_id(answer_infos[0])
                        if answer is None:
                            answer = Answer(answer_infos[0], answer_infos[1], answer_infos[2], user)
                        user.add_answer(answer)

    print(Answer.ids_index)

    for file_name in tqdm(os.listdir('./Sample_datas')):
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
                            question_infos = re.split('\-|\,', item)
                            question = get_question_by_id(question_infos[0])
                            user = get_user_by_id(question_infos[1])
                            if question is None:
                                question =  (question_infos[1], question_infos[2], user, question_infos[3])
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

    for i in tqdm(range(10)):
        with open('./pickled/users_'+str(i)+'.pkl', 'wb') as f:
            temp = len(User.instances)
            pickle.dump(User.instances[int(temp*i/10) : int(temp*(i+1)/10)], f)
        with open('./pickled/questions_'+str(i)+'.pkl', 'wb') as f:
            temp = len(Question.instances)
            pickle.dump(Question.instances[int(temp*i/10) : int(temp*(i+1)/10)], f)
        with open('./pickled/answers_'+str(i)+'.pkl', 'wb') as f:
            temp = len(Answer.instances)
            pickle.dump(Answer.instances[int(temp*i/10) : int(temp*(i+1)/10)], f)


if __name__ == '__main__':
    main()