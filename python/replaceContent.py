# A FILE CONTAINS A WORD "DONKEY MULTIPLE TIMES YOU NEED TO WRITE A PROGRAM WHICH REPLACE THIS WORD WITH #### BY UPDATING THE SAME FILE
with open("python/replaceContent.txt") as f:
    content = f.read()

content = content.replace("Donkey","#####")

with open("python/replaceContent.txt","w") as f:
    f.write(content)