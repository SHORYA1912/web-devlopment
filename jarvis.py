from nltk.chat.util import Chat, reflections

reflection={
    "I AM "     : "YOU ARE",
    "I WAS"     : "YOU WERE",
    "I"         : "YOU",
    "I'M"       : "YOUR",
    "I,d"       : "I WOULD",
    "i've"      : "I HAVE",
    "I' LL"     : "I WILL",
    "MY"        : "YOUR",
    "YOU ARE"   : "I AM",
    "YOU  WERE" : "I WAS",
    "YOUR"      : "MY",
    "YOURs"     : "MINE",
    "YOU"       : "ME",
    "ME"        : "YOU"
}

pairs = {
[ r"MY NAME IS (.*)"
    "HELLO #1 , NICE TO MEET YOU"]

[ r"HEY|HELLO|HI"
    "HELLO , HEY THERE"]
,
[ r"WHAT IS YOUR NAME"
    "I AM A CHAT BOT CREATED TO TALK"]
 ,
 [r"SORRY!"
    "ITS ALL RIGHT ,NEVER MIND"]
,
[r"WHAT (.*) WANT ?"
    "MAKE AN OFFER THAT I CAN'T REFUSE"]
,
[ r" (.*) CREATED YOU ? "
    "TOXIN HACKER CREATED ME"]
,
[ r" (.*) WORK IN ?"
    "#1 WORK IN A AMASING COMPANY"]
,
[ r"HOW HEALTH?"
    "I AM A COMPUTER PROGRAM I NEVER GET SICK"]
,
[ r"WHO (.*) (MOVIE_STAR|ACTOR)"
    "VIJAY THALPATHY IS THE BEST"]
,
[ r"I WANT Guild FOR ONLINE COURSES"
    "OF COURSE ,JARVIS TECT HAS GREAT COURESE"]
    }

def chat():
    print("I AM A CHAT BOT MADE BY eRroR industries")
    chat = chat(pairs,reflection)
    chat.converse()

if __name__ == "__main__":
    chat()
    