import random,time
from string import ascii_lowercase
from fractions import  Fraction
import tomli
import pathlib

WAY = pathlib.Path(__file__).parent / "Qb.toml"
#Q_BANK = tomli.loads(WAY.read_text())
BANK = {
    "When Kemta was born?":["1984", "1990","2000","2010"],
    "When is Bimbo's birthday?":["1985", "1990","2000","2010"],
    "Can 00Papi drive?":["yes","No","Maybe","None"]
}
print("""
Answers all questions
""")

NUM_PER_QUIZ=int(input('How many Questions? '))


def prepare(path):
    store= tomli.loads(path.read_text())['questions']
    q_num = min(NUM_PER_QUIZ, len(store))
    return  random.sample(store, k=q_num)

def get_answer(q,ans,num_choices=1,hint=None):

    print(f'{q}')



    zip_options = dict(zip(ascii_lowercase, ans))
    if hint:
        zip_options["?"] = "Hint"

    for label, x in zip_options.items():
        print(f" \t{label}) {x} ", end='\n')


    while True:
        plural_s = "" if num_choices ==1 else f"s (choose {num_choices})"
        choice= input(f'\n Choice{plural_s}? ').lower().strip(" ")
        answers = set(choice.replace(",", " ").split())

        #handle hints
        if hint and "?" in answers:
            print(f"Hint: \u260E {hint}")
            continue

        # Handle invalid anwsers

        if len(answers) != num_choices:
            plural_s = "" if num_choices == 1 else "s, separated by comma"
            print(f"{num_choices} answer{plural_s} required ")
            continue

        if any(
                (invalid := choice) not in zip_options for choice in answers
        ):
            print(
                f"{invalid!r} is not a valid choice. "
                f"Please use {', '.join(zip_options)}"
            )
            continue
        return [zip_options[choice.strip(" ").lower()] for choice in answers]

    # while (choice := input(f'\n Choice: ').lower()) not in zip_options.keys():  # used walrus operator here
    #     print(f" Please pick from the available options {list(zip_options.keys())}")
    # return   zip_options[choice.strip(' ').lower()]

def ask_question(q):
    answer = q['answer']
    combine = q['answer']+q['alt']
    random.shuffle(combine)

    choice= get_answer(q['question'],combine, num_choices=len(answer), hint=q.get('hint'))
    if set(answer) == set(choice):
        print(f" \u2713 absolutely correct \u2713")
        time.sleep(1)
        return 1
    else:
        is_or_are = " is" if len(answer) ==1 else "s are"
        print(f" \u2718 failed \u2718")
        print("\n >".join([f"No the answer{is_or_are}:"] + answer))

        time.sleep(.5)
        return 0

def run_quiz():
    ques= prepare(WAY)
    score = 0
    for num, q in enumerate(ques, start=1):
        print(f'\nQuestion{num}')
        score += ask_question(q=q)
    if Fraction(score,num) > 0.5:
        print(f' \n \u265B Congratulations!!! you passed the cut-off mark')
    else: print("\n \U0001F915  Opps try again")
    print(f'\n Your scored {score} out of {num} ')


if __name__ == "__main__":
    run_quiz()