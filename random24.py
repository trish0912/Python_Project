import random
auto_digit = random.randrange(1,100)

game_start = True
while game_start:
        guess = input("enter your guess: ")
        try:
           val = int(guess)
        except ValueError as error:
            print(f"This is not an integer {error}")
            continue
        while val!=auto_digit:
            if val>auto_digit:
                print("This is higher than actual number,try again")
                break
            elif val<auto_digit:
                print("This is lower than actual number,try again")
                break
        if val==auto_digit:
            print("Your guess is right")
            ask = input("wanna play-'y or 'n': ")
            if ask=='n':
                print("Thank you for playing!")
                game_start=False
                break
            else:
                auto_digit = random.randrange(1,100)
                continue