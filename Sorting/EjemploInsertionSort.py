def insertionSort(nlist)->list:
    for index in range(1,len(nlist)):

     currentvalue = nlist[index]
     print (nlist[index])
     input("clic")
     position = index
     original = nlist[index]

     while position>0 and nlist[position-1]>currentvalue:
         nlist[position]=nlist[position-1]
         position = position-1

     nlist[position]=original
    return nlist

nlist = [14,46,43,27,57,41,45,21,70]
print(nlist)
new=[]
new=insertionSort(nlist)
print (new)


m=[[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [2, 2, 2, 2, 2], 
[3, 3, 3, 3, 3], [4, 4, 4, 4, 4]]
print (m)
print ("******************")
m[0]=m[4]
print (m)


