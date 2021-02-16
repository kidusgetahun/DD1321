import sys
from linkedQFile import LinkedQ

if len(sys.argv) < 3:
   print("parametrar saknas")
   sys.exit()
else:
   print("parameter 1 är",  sys.argv[1], " och parameter 2 är", sys.argv[2])

def makechildren(ord,barn):
    giltiga=word3()
    barn.store(ord,ord) #lägg in ordet
    alfabeta = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','å','ä','ö']
    komb=[]
    for i, x in enumerate(ord):
        for a in alfabeta:
            word=list(ord) #gör ordet till vektor & nollställer
            if x!=a: #lägg inte in samma ord
                word[i]=a #ändra bokstav
                word1="".join(word) #lägg ihop till string
                if giltiga.search(word1)!=None and not word1 in barn:#.__contains__(word1): #om giltigt och ej finns
                    komb.append(word1) #lägg in i kombinationer-outputen
                    barn.store(word1,word1) #lägg in i DictHash
    return komb, barn #returna barnen som pythonlista (=komb) och hashlista (=barn)

class DictHash: #från d1
    def __init__(self):
        self._htab={}
    def __contains__(self,key): #anropas via "in"
        try:
            self._htab[key]
            return True
        except KeyError:
            return False
    def store(self,key,data):
        self._htab[key] = data
    def search(self,key):
        if key in self:
            return self._htab[key]

def word3(): #hämtar alla giltiga ord
    word3 = open('word3.txt','r').readlines() #hämta innehållet från word3.txt
    giltiga=DictHash()
    for line in word3:
        line=line.split('\n')
        giltiga.store(line[0],line[0]) #lägg in i hashtabellen
    return giltiga

class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

def writechain(ParentNode): #skriver ut vägen
    if ParentNode==None: # om tom från början
        print('Det finns ingen väg')
    elif ParentNode.parent!=None: #om den har föräldrar - iterera ett steg upp
        Parent = ParentNode.parent
        return (writechain(Parent) +'->'+ ParentNode.word)
    else: #om stamfader -> skriv ut ordet
        return ParentNode.word

def sok(startord,slutord): #söker om det finns en väg eller inte
    queueOfWords=LinkedQ()
    barn=DictHash()
    P=ParentNode(startord)
    queueOfWords.enqueue(P)
    while not queueOfWords.isEmpty():
        nextWord = queueOfWords.dequeue()
        if nextWord.word == slutord: #om hittad
            break
        else:
            komb,barn=makechildren(nextWord.word,barn)
            for ord in komb:
                tmp=ParentNode(ord,nextWord)
                queueOfWords.enqueue(tmp)
    if queueOfWords.isEmpty(): #om ej hittad
        return None
    else:             #om hittad
        return nextWord

import sys

if len(sys.argv) < 3:
    print("Start- och slutord saknas")
    print("Använd programmet så här: \n\t python3", sys.argv[0], " [startord] [slutord]")
    sys.exit()
else:
    P=sok(sys.argv[1],sys.argv[2])
    print(writechain(P))

