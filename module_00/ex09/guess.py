from random import randint

if __name__ == "__main__" :
    print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!\n")

    randNum = randint(1, 99)

    attempts = 1
    while (True) :
        print("What's your guess between 1 and 99?")
        n = input()
        if not n.isnumeric() :
            if (n == "exit") :
                print("Goodbye!")
                exit(0)
            print("That's not a number.")
        elif (int(n) > randNum) :
            print("Too high!")
        elif (int(n) < randNum) :
            print("Too low!")
        else :
            if randNum == 42 :
                print("The answer to the ultimate question of life, the universe and everything is 42.")
            if attempts == 1 :
                print("Congratulations! You got it on your first try!")
            else :
                print(f"Congratulations, you've got it!\nYou won in {attempts} attempts!")
            exit(0)
        attempts += 1

