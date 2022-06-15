import random,time
from string import ascii_lowercase
from fractions import  Fraction
BANK = {
    "When Kemta was born?":["1984", "1990","2000","2010"],
    "When is Bimbo's birthday?":["1985", "1990","2000","2010"],
    "Can 00Papi drive?":["yes","No","Maybe","None"]
}
print("""
Answers all questions
""")
NUM_PER_QUIZ=int(input('How many Questions? '))
q_num= min(NUM_PER_QUIZ,len(BANK))
banker = random.sample(list(BANK.items()),k=q_num)
score = 0
for num, (q,ans) in enumerate(banker,start=1):
    print(f'\nQuestion{num}')
    print(f'{q}')


    answer = ans[0]
    random.shuffle(ans)

    zip_options= dict(zip(ascii_lowercase,ans))

    for label,x in zip_options.items():
        print(f" \t{label}) {x} ", end='\n')

    while (choice := input(f'\n Choice: ')) not in zip_options.keys():   #used walrus operator here
        print(f" Please pick from the available options {list(zip_options.keys())}")
    if answer == zip_options[choice.strip(' ').lower()]:
        print(f" \u2713 absolutely correct \u2713")
        score +=1
    else: print(f" \u2718 failed \u2718")

    time.sleep(1)
print(f'\n Your final score is {Fraction(score,q_num)} ')
