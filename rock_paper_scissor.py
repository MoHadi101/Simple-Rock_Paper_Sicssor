import random
# key -> value
# r -> 🪨
# p -> 📄
# s -> ✂️
emojis ={'r':'🪨', 'p':'📄', 's':'✂️'}
choices =( 'r','p','s')  # tuple is a read only list wir kann nicht verändert werden wie append oder remove
while True:

    user_choice = input("Rock, Paper or Scissors? (r/p/s):").lower()
    # if user_choice != "r" and user_choice !="p" and user_choice != "s":
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue


    computer_choice = random.choice(choices)

    print('You chose: ' + emojis[user_choice])
    print('Computer chose : ' + emojis[computer_choice])

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "r" and computer_choice == "s") or 
        (user_choice == "p" and computer_choice == "r") or 
        (user_choice == "s" and computer_choice == "p")):
        print("You win!")
    else:
        print("Computer wins!")

    should_continue = input("Do you want to play again? (yes/no): ").lower()
    if should_continue == 'no':
        break
# Ask the user to make a choice
# If choice is not valid
#     print an error 
# let computer make a random choice
# printc choisces (emojis)
# Detrmine the winner
# Ask the user if thez want to continue
# if not
#     Terminate the game
