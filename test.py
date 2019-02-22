# Python
#
from random import random
import math
import sys

def makeLine(n):
    newLine=[]
    for i in range(n):
        newLine.append((random()>0.5)*1)
    return newLine

def nextLine(l):
    outputList = [None]*(len(l)-1)
    for i in range(len(outputList)):
        outputList[i]=(l[i]+l[i+1]) % 2
    return outputList

def makeOutput(l):
    output = []
    dummy=l
    output.append(dummy[-1])
    for i in range(len(l)-1):
        dummy=nextLine(dummy)
        output.append(dummy[-1])
    output.reverse()
    return output

#n=int(sys.argv[0])

J=24
for n in range(J+1)[1:]:
    count=0
    for k in range(2**n):
        # nyListe=makeLine(10)
        #n=int(math.log(N,2))

        nyListe = [int(i) for i in list(format(k,'0'+str(n)+'b'))]
        # print("k: " +str(k) + "\t" + str(nyListe))
        outputListe = makeOutput(nyListe)
        # print("Output:  " + str(outputListe))

        if (nyListe == outputListe):
#            print("n: " + str(n)+ "\t" + "k: " + str(k) +"\t" + str(outputListe))
            count += 1
    print "n:" + str(n) + "\t " + "count: " + str(count)



# testInput = [1,0,1,1,0]
# print("testInput: "+ str(testInput))
# print("Output:    " + str(makeOutput(testInput)))

