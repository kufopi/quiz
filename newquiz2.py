import random,time
from string import ascii_lowercase
from fractions import  Fraction
import tomli
import pathlib


BANK = {
    "When Kemta was born?":["1984", "1990","2000","2010"],
    "When is Bimbo's birthday?":["1985", "1990","2000","2010"],
    "Can 00Papi drive?":["yes","No","Maybe","None"]
}
print("""
Answers all questions
""")

NUM_PER_QUIZ=int(input('How many Questions? '))


def prepare(store):
    q_num = min(NUM_PER_QUIZ, len(store))
    return  random.sample(list(store.items()), k=q_num)

def get_answer(q,ans):

    print(f'{q}')



    zip_options = dict(zip(ascii_lowercase, ans))

    for label, x in zip_options.items():
        print(f" \t{label}) {x} ", end='\n')

    while (choice := input(f'\n Choice: ')) not in zip_options.keys():  # used walrus operator here
        print(f" Please pick from the available options {list(zip_options.keys())}")
    return   zip_options[choice.strip(' ').lower()]

def ask_question(q,ans):
    answer = ans[0]
    random.shuffle(ans)

    choice= get_answer(q,ans)
    if answer == choice:
        print(f" \u2713 absolutely correct \u2713")
        time.sleep(1)
        return 1
    else:
        print(f" \u2718 failed \u2718")
        time.sleep(.5)
        return 0

def run_quiz():
    ques= prepare(store=BANK)
    score = 0
    for num, (q, ans) in enumerate(ques, start=1):
        print(f'\nQuestion{num}')
        score += ask_question(q=q,ans=ans)

    print(f'\n Your final score is {Fraction(score, num)} ')


if __name__ == "__main__":
    run_quiz()