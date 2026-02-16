import random
guess = random.randint(1,100)
c = 0
k = 0
while k != 'n':
    your = int(input("Guess the number which is between 0 and 100 :"))
    if your == guess:
        c += 1
        print("CONGRATULATION!!! YOU HAVE GUESSED.")
        print(f"You have guessed {c} times")
        break
    else:
        c += 1
        print("WRONG!!!")
        if your > guess:
            print("Target smaller")
        else:
            print("Target bigger")

    k = input("Want to Continue? (y/n) : ")