import random

def main():
    i=1
    while i<=3:
        print("Round ",i, head_tail())
        i+=1


def head_tail():
    return random.choice(["Heads", "Tails"])

main()