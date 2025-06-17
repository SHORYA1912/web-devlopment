file1 = open('python/demo.txt', 'r')
file2 = open('python/codingalupdated.txt', 'w')
for line in file1.readlines():
    if not line.startswith('codingal'):
        file2.write(line)
file1.close()
file2.close()