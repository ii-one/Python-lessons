#__author__ =  'i-0ne';

import sys

if sys.version_info[0] == 2:
    input_function = raw_input
else:
    input_function = input

right_answer_count = 0
question_number = 0

# You can edit q&a file manually, ';' - seperates questions and set final;
# '#' - separate question from answer

question_file  = open(sys.path[0]+"/qanda.txt", "r")
file_content = question_file.read()
q_and_a = file_content.split(";")
question_file.close()

user_name = input_function('Введите Ваше имя: ')
for question_block in q_and_a:
    question_number += 1
    q_len = len(question_block) #getting lengh of whole block
    index = question_block.index('#') #taking seperation between q & a
    question = question_block[1:index] #question is everything before separator
    answer = question_block[-(q_len-index-1):] #answer is the rest

    print('-'*80)
    print('Вопрос №{} из {}.'.format(question_number, len(q_and_a)))
    print('-'*80)
    print(question)

    user_answer = input_function('{}, Ваш ответ: '.format(user_name))
    if str(user_answer) == str(answer):
        right_answer_count += 1
        print("Это правильный ответ! Всего правильных ответов: {}""".format(right_answer_count))
    else:
        print('К сожалению, неверно.')

print('Ваш тест завершен!')
results = str('Имя:{}, Всего вопросов:{}, Правильных ответов:{}\n'.format(user_name,len(q_and_a),right_answer_count))
records_file  = open(sys.path[0]+"/results.txt", "a")
records_file.write(results)
print('Результаты сохранены.')
records_file.close
