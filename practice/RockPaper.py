import random

def play():
    user = input("Enter your choice (rock, paper, scissors): ").lower()
    computer = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer}")

    if user == computer:
        return "It's a tie!"
    elif user == "rock":
        if computer == "scissors":
            return "You win!"
        else:
            return "Computer wins!"
    elif user == "paper":
        if computer == "rock":
            return "You win!"
        else:
            return "Computer wins!"
    elif user == "scissors":
        if computer == "paper":
            return "You win!"
        else:
            return "Computer wins!"
    else:
        return "Invalid choice."

print(play())
