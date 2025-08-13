import random
from colorama import init, Fore , Style

init(autoreset=True)

def draw (b):
    print("\n" + "\n---+---+---\n".join([" | ".join([b[i] for i in range(r, r+3)]) for r in range(0,9,3)]) + "\n")

def win(b,s):
    return any(b[i]==b[j]==b[k]==s for i,j,k in [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)])

def full(b):
    return all(not x.isdigit() for x in b)

def move(board ,symbol):
    while True:
        m = input(f"Player {symbol}, enter your move (1-9): ")

        if m.isdigit() and board[int(m)-1].isdigit():
            board[int(m)-1] = symbol
            break
        print("Try again.")

def ai (board,ai_s,pl_s):
    for i in range(9):
        if board[i].isdigit():
            for s in (ai_s,pl_s):
                b = board[:];b[i]= s
                if win(b,s):board[i]=ai_s; return
    board[random.choice([i for i,v in enumerate(board) if v.isdigit()])]=ai_s

def game():
    b = [str(i) for i in range(9)]
    p,a =("X","O")if input("Choose your symbol (X or O): ").upper() == "X" else ("O","X")
    t = "P"
    while True:

        draw(b)

        if t == 'P':

            move(b, p)

            if win(b,p): draw(b); print("You win!"); break

        else:

            ai(b, a, p)

            if win(b,a): draw(b); print("AI wins!"); break

        if full(b): draw(b); print("Tie!"); break

        t = 'AI' if t == 'P' else 'P'

while input("Play? (y/n): ").lower() == 'y': game()