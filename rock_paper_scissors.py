import random

print("======================================")
print("      ROCK PAPER SCISSORS GAME")
print("======================================")

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0
round_number = 1

while True:
    print(f"\nRound {round_number}")

    user_choice = input("Choose Rock, Paper, or Scissors: ").strip().lower()

    if user_choice not in choices:
        print("Invalid choice! Please enter Rock, Paper, or Scissors.")
        continue

    computer_choice = random.choice(choices)

    print(f"\nYou selected      : {user_choice.capitalize()}")
    print(f"Computer selected : {computer_choice.capitalize()}")

    if user_choice == computer_choice:
        print("Result: It's a Tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("Result: You Win!")
        user_score += 1

    else:
        print("Result: Computer Wins!")
        computer_score += 1

    print("\nCurrent Score")
    print(f"You      : {user_score}")
    print(f"Computer : {computer_score}")

    play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()

    if play_again != "yes":
        print("\n========== FINAL SCORE ==========")
        print(f"You      : {user_score}")
        print(f"Computer : {computer_score}")

        if user_score > computer_score:
            print("Congratulations! You are the overall winner.")
        elif computer_score > user_score:
            print("Computer is the overall winner.")
        else:
            print("The game ends in a draw.")

        print("\nThank you for playing!")
        break

    round_number += 1