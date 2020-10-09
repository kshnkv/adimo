import random
n=0
fr=0
sc=0
th=0
fr=0

spisok = [int(random.random()*100000) for i in range(1000)]
for j in spisok:
    if (j>n):
        n=j
print (n)

pyat=[0,0,0,0]

perech= [int(random.random()*100000) for i in range(10000)]

for i in perech:
    if (j>fr):
        pyat[1]= pyat[0]
        pyat[0]=j
        
    elif (j>sc):
        pyat[2]= pyat[1]
        pyat[1]=j
        
    elif (j>th):
        pyat[3]= pyat[2]
        pyat[2]=j
        
    elif (j>fr):
        
        pyat[3]=j
        


print(pyat) 