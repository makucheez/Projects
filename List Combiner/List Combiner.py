list1 = [1,2,3] 
list2 = ['a','b','c']
listnumfirst = []
listletterfirst = []
finallist = []

for n in range(len(list1)):
    for x in range(len(list2)):
        
        listnumfirst.append(str(list1[n]) + str(list2[x])) 
        listletterfirst.append(str(list2[x]) + str(list1[n])) 
        finallist.append (str(list1[n]) + str(list2[x])) 
        finallist.append (str(list2[x]) + str(list1[n])) 

print(f"\n{listnumfirst}, \n\nOr\n \n{listletterfirst}, \n\nFinal List\n\n{finallist}") 