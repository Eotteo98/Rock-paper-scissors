import random


choices1 = ["rock", "paper", "scissors"]
c_score = 0
p_score = 0


computer = random.choice(choices1)


player = input("Please enter your choice from these options: rock/paper/scissors: ").lower()


if player == computer:
    print("TIE")

elif player == "rock" and computer == "paper":
    print("Computer wins!")
    c_score += 1
elif player == "paper" and computer == "scissors":
    print("Computer wins!")
    c_score += 1
elif player == "scissors" and computer == "rock":
    print("Computer wins!")
    c_score += 1


elif player == "rock" and computer == "scissors":
    print("Player wins!")
    p_score += 1
elif player == "paper" and computer == "rock":
    print("Player wins!")
    p_score += 1
elif player == "scissors" and computer == "paper":
    print("Player wins!")
    p_score += 1


else:
    print("Invalid input. Please choose 'rock', 'paper', or 'scissors'.")


print(f"Score - Player: {p_score}, Computer: {c_score}")