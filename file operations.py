file = open("python/demo.txt", "r")
print(file.read())
file.close()

file = open("python/demo.txt", "r")
print("/n read in parts /n")
print(file.read(8))
file.close()

file = open("python/demo.txt", "a")
file.write("/n i am a penguin .I am 5 years old")
file.close()