l=[]
print('''Options:
          1.Insert
          2.Delete
          3.Search
          4.Sort
          5.exit''')
ch=int(input())
while(ch!=5):
    if ch==1:
        x=int(input())
        if x not in l:
            l.append(x)
            print(l)
        else:
            print(f"{x} is already in list")
        ch=int(input())
    elif ch==2:
        y=int(input())
        if y in l:
            l.remove(y)
            print(l)
        else:
            print(f"{y} is not in list")
        ch=int(input())
    elif ch==3:
        x=int(input())
        if x in l:
            print(l.index(x)+1)
        else:
            print(f"{x} is not in list")
        ch=int(input())       
    elif ch==4:
        l.sort()
        print(l)
        ch=int(input())
    else:
        break
