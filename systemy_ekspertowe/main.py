import json


class Menu():
    def __init__(self):
        self.last_questions = []
        self.current_question = "categories"

    def user_input(self, question, max):
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
    
    def show_answers(self, question: str, answer: str):
        self.current_question = question
        f = open('questions/{}.json'.format(question))
        q = json.load(f)
        if(q['answers'][answer]):
            print(q['answers'][answer])

    def show_question(self, question: str):
        self.current_question = question
        f = open('questions/{}.json'.format(question))
        q = json.load(f)
        num = 0
        if(len(self.last_questions) > 0):
            print('\n{}: {}'.format(0, 'wróć'))
        else:
            print('\n{}: {}'.format(0, 'wyjdź'))
        for v in q['options'].values():
            num += 1
            print('{}: {}'.format(num, v))
        val = self.user_input(q['question'], len(q['options']))
        if(val == 0):
            if(len(self.last_questions) > 0):
                question = self.last_questions.pop()
                self.show_question(question)
            else:
                return
        elif(list(q['options'])[val - 1] != 'end' and list(q['options'])[val - 1][0:3] != 'wip'):
            self.last_questions.append(question)
            self.show_question(list(q['options'])[val - 1])
        else:
            self.last_questions.append(question)
            print("\n\n________________________________________")
            for i, a in enumerate(self.last_questions):
                if(i + 1 < len(self.last_questions)):
                    self.show_answers(a, self.last_questions[i+1])



app = Menu()
app.show_question(app.current_question)
