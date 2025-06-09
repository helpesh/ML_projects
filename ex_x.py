num=0
tot=0.0

while True:
    sval = input('Enter the number\n')
    if(sval=='done'):
        break
    try:
        sval = float(sval)
    except:
        print('Invalid Number')
        continue
    num = num +1
    tot = tot +sval
    print(sval)
    
print(tot,num,tot/num)