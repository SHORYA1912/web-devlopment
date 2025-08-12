from colorama import Fore, Style, init
from textblob import TextBlob
init(autoreset=True)
history = []

print(f"{Fore.CYAN} Welcome to the Sentiment Spy")
print(f"{Fore.YELLOW}COMMANDS: HISTORY, RESET, EXIT")

while True:
    text = input(f"{Fore.GREEN}Enter your text: {Style.RESET_ALL}").strip()

    if not text:
        continue
    cmd = text.lower()

    if cmd == "exit":
        print(f"{Fore.BLUE} Goodbye! AGENT ")
        break

    elif cmd == "reset":
        history.clear()
        print(f"{Fore.BLUE} History cleared.")
        continue

    elif cmd == "history":
        if not history:
            print(f"{Fore.RED}NO HISTORY YET")
        else:
            print(f"{Fore.CYAN}CONVERSATION")
            for i, (T, P, S) in enumerate(history, 1):
                color = Fore.GREEN if S == "positive" else Fore.RED if S == "negative" else Fore.YELLOW
                print(f"{color} {i}. {T} | {P} | {S}")
        continue

    polarity = TextBlob(text).sentiment.polarity
    sentiment = "positive" if polarity > 0 else "negative" if polarity < 0 else "neutral"
    color = Fore.GREEN if sentiment == "positive" else Fore.RED if sentiment == "negative" else Fore.YELLOW
    print(f"{color}sentiment: {sentiment} (polarity: {polarity})")
    history.append((text, polarity, sentiment))
