n = int(input('n = '))
numbers = range(1,n+1)
numbers = ''.join(str (e) for e in numbers)


l2 = ''
for i in range(1,n+1):
    l1 = numbers[:i]
    
    index = l1.__len__() -2

    while index >= 0:
        l2 +=  l1[index]
        index -= 1
    l = l1 + l2
    print(l)
    l2 = ''



    



    