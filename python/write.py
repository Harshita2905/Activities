# for append use a instead w
#f = open('python/sample.txt', 'w')
f = open('python/sample.txt', 'a')
f.write('please write this to the file')
f.write('please write this also to the file')#replace the first line with this line
#with open
with open('python/sample2.txt', 'r') as f:
    a=f.read()
with open('python/sample2.txt', 'w') as f:
    a = f.write('me')
print(a)

f.close()