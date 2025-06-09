fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    word_split=line.split() 
    for word in word_split:
        if  word not in lst:
            lst.append(word)
        else:
            continue
            

print(lst.sort())