file_read=open('python/demo.txt', 'r')
print ("file in read mode")
print(file_read.read())
file_read.close()

file_write=open('python/demo.txt', 'w')
print ("file in write mode")
file_write.write("MY HOBBY IS CODING")
file_write.close()

file_append=open('python/demo.txt', 'a')
print ("file in append mode")
file_append.write("/n my hobby is coding")
file_append.close()