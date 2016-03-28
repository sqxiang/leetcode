n = int(raw_input())
while(n>0):
    sstr = raw_input()
    a = sstr[0]
    l = list()
    count = 0

    for s in sstr:
        if(ord(s) not in range(ord('A'),ord('Z')+1)):
            print 'input error!' \
                  ''
            break
        else:
            if(s==a):
                count+=1
            if(s!=a):
                if(count==1):
                    l.append(a)

                else:
                    l.append(str(count)+a)
                    count =1
            a =s
    if(count==1):
        l.append(a)
    if(count>1):
        l.append(str(count)+a)
    print ''.join(l)
    n = n-1




