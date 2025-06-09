import re
fname=input('Enter the name of the file')
if len(fname)<1: fname='regex_sum_2220781.txt'
handle= open(fname)
TheSum=0
newList=list()
for line in handle:
        line=line.rstrip()
        words=line.split()
        for w in words: 
            stuff=re.findall('[0-9]+',w)
            if len(stuff)>0:
                num=int(stuff[0])
                newList.append(num)

print(newList)
print(sum(newList))                    

        
#print(len(num))
#print(TheSum)    
#print(numList)    

