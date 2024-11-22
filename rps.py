# rock, paper, scissors
import random

player = input("Rock (r), Paper (p), or Scissors (s)? ")
computer = random.choice(["r", "p", "s"])
if player == computer:
  print(f"Computer played: {computer}")
  print("It's a tie!")
elif (
  player == "r" and computer == "p" or
  player == "p" and computer == "s" or
  player == "s" and computer == "r"
  ):
  print(f"Computer played: {computer}")
  print("You lose :(")
elif (
  player == "r" and computer == "s" or
  player == "p" and computer == "r" or
  player == "s" and computer == "p"
  ):
  print(f"Computer played: {computer}")
  print("You win!")