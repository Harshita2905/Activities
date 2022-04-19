#function game return score if Hi-score file contains score smaller than game function score then update the hi-score in Hi-score.txt
def game():
    return 45

score = game()

with open("python/hiscore.txt") as f:
    hiscore = f.read()
if hiscore =='':
    with open("python/hiscore.txt", "w") as f:
        f.write(str(score))
elif int(hiscore)<score:
    with open("python/hiscore.txt", "w") as f:
        f.write(str(score))