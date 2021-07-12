import random

def dicepy():
    possible_outcomes = ["1", "2", "3", "4", "5", "6"]
    outcome = possible_outcomes[random.randint(0, 5)]
    print(outcome)
    ###
    rer_q = input("Do you want to re-roll?\n")
    ###
    if rer_q == "yes":
        dicepy()
    else:
        print("Thank you for rolling!")

dicepy()
