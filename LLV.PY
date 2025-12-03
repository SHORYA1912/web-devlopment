import re
from colorama import fore ,Style, init 

init(autoreset=True)

def clean_text(text):
    text = text.replace('\n', ' ').replace('\r', ' ')
    return text.strip().lower()

def score_sentence(text):
    words =text.lower().split()
    freq = {}
    for w in words:
        if w not in freq:
            freq [w] = 0 
        freq [w] +=1

    sentences = re.split(r'\.|\!|\?', text)

    sentences_scores = {}
    for sentence in sentences:
        score = 0
        for word in sentence.lower().split():
            score += freq.get(word, 0)
        sentences_scores [sentence] = score
        score == freq.get(word, 0)
        sentence_score [sentence] = score
        return sentences_scores
    
def summarize_text(text, n=3):     
    text = clean_text(text)
    sentences.scores = score_sentence(text)

if len(sentences_scores) == num_sentences:
        return text 
        
ranked_sorted = sorted(sentences_scores.items(), key=lambda x: x[1], reverse=True)
selected = ranked[num_sentences]

return ' '.join(selected)

print(fore.yellow + style.BRIGHT + "HI THERE! WHAT'S YOUR NAME")
name = input(fore.green + style.BRIGHT + "ENTER YOUR NAME: ")
print(fore.yellow + style.BRIGHT + f"HELLO {name.upper()}! WELCOME TO THE TEXT SUMMARIZER") 
user_text = input(fore.green + style.BRIGHT + "PLEASE ENTER THE TEXT YOU WANT TO SUMMARIZE: ")
