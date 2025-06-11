file=open('python/demo.txt','r')
counter=0
content = file.read()
colist=content.split()
for i in colist:
    if i == 'is':
        counter += 1
print("this is the number of lines")
print(counter)
file.close()