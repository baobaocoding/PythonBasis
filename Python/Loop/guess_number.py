import random
hide_number = random.randint(1, 100)

win = False
guess_times = 7
while guess_times > 0:
    guess = int(
        input("Please guess the number from 1 to 100 (%d times left):" % guess_times))
    if guess == hide_number:
        win = True
        break
    else:
        if guess > hide_number:
            print("It should be smaller")
        else:
            print("It should be bigger")
        guess_times -= 1

if not win:
    print("You fail")
else:
    print("Congradulations! You are right!")
