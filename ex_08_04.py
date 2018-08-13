text = open('romeo.txt')
mylist = []
for line in text:
    line1 = line.rstrip()
    words = line1.split()
    for element in words:
        if element in mylist:
            continue
        else:
            mylist.append(element)

mylist.sort()
print(mylist)
