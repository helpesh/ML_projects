

fname=input('Enter file: ')
if len(fname)<1: 
    fname='romeo.txt'

fhand=open(fname)
many = dict()

for line in fhand:
    line=line.rstrip()
    words=line.split()
    
    for w in words:   
        many[w]=many.get(w,0)+1
        
tmp=dict()
newList=list()
print(many)
for k,v in many.items():
    tup = (v,k)
    newList.append(tup)
cool = sorted(newList,reverse=True)
print('counting...')
for v,k in cool:
    print(k,v)  
    

    



        