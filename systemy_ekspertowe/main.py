from categories import *


def user_input(max):
    while(True):
        val = input("Wybierz element: ")
        try:
            p = int(val)
            if(p <= max):
                break
            else:
                print("Wartość musi być liczbą całkowitą ≤ {}".format(max-1))
        except ValueError:
            print("Wartość musi być liczbą całkowitą ≤ {}".format(max-1))
    return p


print('\n'.join('{}: {}'.format(k, v.name) for k, v in categories.cat_dict.items()))
cat = user_input(len(categories.cat_dict))
print("Wybrano: '{}'".format(categories.cat_dict[cat].name))

print(categories.cat_dict[cat].question)
print('\n'.join('{}: {}'.format(k, v) for k, v in categories.cat_dict[cat].options.items()))
option = user_input(len(categories.cat_dict[cat].options))
print("Wybrano: '{}'".format(categories.cat_dict[cat].options[option]))