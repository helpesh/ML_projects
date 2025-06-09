fh=open('mbox.txt')
count=0
for lx in fh:
    ly=lx.strip()
    print(lx.upper())
    count = count +1
print(count)


#print(count)