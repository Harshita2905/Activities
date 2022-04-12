#Open function to read the content of a file
f = open('python/sample.txt')
data = f.read(5)#reads first 5 characters from the file
print(data)
f.close()
