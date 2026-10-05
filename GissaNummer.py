import random


print("Welcome to a game of Gussing the number." \
" You have three gusses, for every right answer you get one point."
"for every new round the number range get larger, and the gusses are saved.  ")



while True:
    Gusses = 3
    for round in range(1,100):
        
        games_number = random.randint(1,10**round)

        while Gusses > 0:
            user_number = int(input(f"Guess a number between 1 and {10 ** round }: "))
            print(f"You have {Gusses} left")
        
            if user_number == games_number:
                print("You got the right number! Get redy for next round")
                break
            else:
                if user_number > games_number:
                    print("You are to high!")

                if user_number < games_number:
                        print("You are to low!")

                Gusses -= 1 

        if Gusses == 0:
            print(f"Game over, the right number was {games_number}")
            break

        else: 
            Gusses = Gusses + 3
    y = 0
    while y == 0:
        game = input("Wanna play a new game? Y/N ").lower()

        if game == "y":
            break

