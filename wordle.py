from random import randint
words=["false","cozey","jumps","about","alert","audio","photo","music","maker","heart","guide","daily","coach","craft","black"]

'''def hinter(lista,listb):
    while True:
        generate=randint(0,len(lista)-1)
        if lista[generate]=="*":
            lista[generate]=listb[generate]
            return lista'''
def containing(lista,listb):
    x=[]
    for i in range (0,len(lista)):
        if lista[i] in listb and lista[i]!=listb[i]:
            x.append(lista[i])
    return x
def guessing():
    answer=""
    remp=[]
    perm=[]
    RandomWord=words[randint(0,len(words)-1)]
    revealed=["*"]*len(RandomWord)
    tries=6
    revword=list(RandomWord)
    while answer!=RandomWord and tries!=0:
        l=perm
        tries=tries-1
        print(f"you have this many tries left {tries +1}")
        while True:
            answer=input(f"guess the {len(RandomWord)} letter word: ")
            answer=answer.lower()
            if len(answer)==len(RandomWord):
                revanswer=list(answer)
                perm=remp
                remp=containing(revanswer,revword)
                if len(perm)>len(remp):
                    remp=perm
                else:
                    perm=remp
                for x in range(0,len(revanswer)):
                    if revanswer[x]==revword[x]:
                        revealed[x]=revword[x]
                print("Your Answer is :                "," ".join(revanswer))
                print("The Word You re looking for is :"," ".join(revealed))
                print("cheater word is ", revword)
                tempol = [letter for letter in remp if letter not in revealed]
                print(f"Letters in the word but not in the correct position: {' '.join(tempol)}")
                break
        '''if hints < 3:
            revealed=hinter(revealed,revword)
            hints+=1'''
    if answer==RandomWord:
        print("You Guessed the word correctly good job ")
    else:
        print(f"You failed the word was {RandomWord}")
guessing()
