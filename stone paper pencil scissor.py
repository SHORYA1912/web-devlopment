import random

choices = ["Stone", "Paper", "Pencil", "Scissor"]

win_map = {
    "Stone": ["Scissor", "Pencil"],
    "Paper": ["Stone", "Pencil"],
    "Pencil": ["Paper", "Scissor"],
    "Scissor": ["Paper", "Pencil"]
}

def get_winner(player, ai):
    if player == ai:
        return "Tie"
    elif ai in win_map[player]:
        return "Player"
    else:
        return "AI"

def game():
    print("Choices: 1.Stone 2.Paper 3.Pencil 4.Scissor")
    player_choice = input("Enter your choice (1-4): ")
    if player_choice not in ["1", "2", "3", "4"]:
        print("Invalid choice.")
        return
    player = choices[int(player_choice)-1]
    ai = random.choice(choices)
    print(f"You chose: {player}")
    print(f"AI chose: {ai}")
    winner = get_winner(player, ai)
    if winner == "Tie":
        print("It's a tie!")
    elif winner == "Player":
        print("You win!")
    else:
        print("AI wins!")

while input("Play? (y/n): ").lower() == 'y':
    game()
