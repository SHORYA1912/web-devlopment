with open("python/codingal2.txt","w") as file:
    file.write("/n I am a penguin. I am 1 years old\n")
file.close()

with open("python/codingal2.txt", "r") as file:
    data = file.readlines()
    print("word in this lines are:")
    for line in data:
        word = line.split()
        print(word)
file.close() 