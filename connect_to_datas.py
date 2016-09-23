__author__ = 'Rfun'
import os
import re
from User import *
from Question import *
from Answer import *
from tqdm import tqdm

def read_datas():

    for file_name in tqdm(os.listdir('./Sample_datas')):
        with open('Sample_datas/' + file_name) as f:
            lines = f.readlines()
            file_infos = re.split('\.|\_', file_name)

            #Creating user, if it's not created already
            user = get_user_by_id(file_infos[0])
            if user is None:
                user = User(file_infos[0])

            if len(file_infos) == 3:
                if file_infos[1] == 'q':
                    for line in lines:
                        question_infos = re.split('\-|\,', line)
                        question = get_question_by_id(question_infos[0])
                        if question is None:
                            question = Question(question_infos[0], question_infos[1])
                        user.add_question(question)
                elif file_infos[1] == 'a':
                    for line in lines:
                        answer_infos = re.split('\-', line)
                        answer = get_answer_by_id(answer_infos[0])
                        if answer is None:
                            answer = Answer(answer_infos[0], answer_infos[1], answer_infos[2])
                        user.add_answer(answer)

def main():
    read_datas()
    user = get_user_by_id('4639')
    print(len(user.questions))
    print(len(user.answers))
    print(user.answers[0].parent_id)
    print(user.questions[0].timestamp)


if __name__ == '__main__':
    main()