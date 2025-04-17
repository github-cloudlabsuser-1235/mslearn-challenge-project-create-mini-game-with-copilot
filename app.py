import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "win"
    else:
        return "lose"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    player_score = 0
    computer_score = 0

    while True:
        player_choice = input("Choose rock, paper, or scissors (or type 'quit' to exit): ").lower()
        if player_choice == "quit":
            break
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        if result == "win":
            print("You won this round!")
            player_score += 1
        elif result == "lose":
            print("You lost this round!")
            computer_score += 1
        else:
            print("It's a tie!")

        print(f"Score: You {player_score} - {computer_score} Computer\n")

    print("Thanks for playing!")
    print(f"Final Score: You {player_score} - {computer_score} Computer")

if __name__ == "__main__":
    main()