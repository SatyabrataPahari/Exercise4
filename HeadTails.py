import random

def main():
    name = input("Who are you? ")
    print ("Hello",name)
    i=1
    heads=0
    tails = 0
    while i<=3:
        choice = head_tail()
        print("Round",i, choice)
        if choice == "Heads": heads+=1
        else: tails+=1
        i+=1
    print ("Heads:",heads,", Tails:",tails)


def head_tail():
    return random.choice(["Heads", "Tails"])

main()