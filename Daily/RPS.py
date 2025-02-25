import random

choices = ["Rock", "Paper", "Scissors"]

def game():
    user_score = 0
    computer_score = 0

    while user_score < 3 and computer_score < 3:
        user_choice = input("Choose Rock, Paper, or Scissors: ").capitalize()

        if user_choice not in choices:
            print("vro there's 3 options, it's not that hard")
            continue

        computer_choice = random.choice(choices)
        print(f"You chose {user_choice}, Computer chose {computer_choice}.")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Scissors" and computer_choice == "Paper") or \
             (user_choice == "Paper" and computer_choice == "Rock"):
            print("You win this round!")
            user_score += 1
        else:
            print("You lose this round...")
            computer_score += 1

        print(f"Score: You {user_score} - {computer_score} Computer\n")

    if user_score > computer_score:
        print("You won!")
    else:
        print("The computer won..")

def main():
    print("Rock Paper Scissors")
    game()

if __name__ == "__main__":
    main()
