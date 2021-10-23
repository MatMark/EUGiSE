from categories import *


def user_input(max, question):
    while(True):
        val = input(question)
        try:
            p = int(val)
            if(p <= max and p >= 0):
                break
            else:
                print("Wartość musi być liczbą całkowitą ≥ 0 i ≤ {}".format(max-1))
        except ValueError:
            print("Wartość musi być liczbą całkowitą ≥ 0 i ≤ {}".format(max-1))
    return p


current_question = categories

while(current_question.end == False):
    print('\n'.join('{}: {}'.format(k, v.name)
                    for k, v in current_question.options.items()))
    val = user_input(len(current_question.options), current_question.question)
    current_question = current_question.options[val]
    print("Wybrano: '{}'\n".format(current_question.name))


print('\n'.join('{}: {}'.format(k, v)
                for k, v in current_question.options.items()))
val = user_input(len(current_question.options), current_question.question)
current_question = current_question.options[val]
print("Wybrano: '{}'\n".format(current_question))
