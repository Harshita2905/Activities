#Open function to read the content of a file
f = open('python/sample.txt')
data = f.readline()#reads first 5 characters from the file
print(data)
data = f.readline()#reads first 5 characters from the file
print(data)
f.close()
