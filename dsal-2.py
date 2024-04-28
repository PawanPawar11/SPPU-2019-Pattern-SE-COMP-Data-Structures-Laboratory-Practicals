#Linear Probing

def Insert_LinearProbing(data,size,hashTable):
    key=data[0]%size
    while hashTable[key] != -1:
        key = (key+1)%size
    else:
        hashTable[key]=data

def Search_LinearProbing(data,size,hashTable):
    key=data%size
    probe=1
    while hashTable[key][0] != data:
        key = (key+1)%size
        probe+=1
    else:
        print(data," Found at position ",key)
        print("Number of probes required ",probe)
    
#Double Hashing

def Insert_DoubleHashing(data,size,hashTable,m):
    pos = data[0]%size
    while hashTable[pos] != -1:
        pos = m-(data[0]%m)
    else:
        hashTable[pos] = data

def Search_DoubleHashing(data,size,hashTable,m):
    pos = data%size
    probe=1
    while hashTable[pos][0] != data:
        pos = m-(data%m)
        probe+=1
    else:
        if hashTable[pos][0] == data:
            print(data,"Found at position ",pos)
            print("Number of probes required ",probe)


ht = []
ht_size = 10
for i in range(ht_size):
    ht.append(-1)

#ht = [[25, 'j'],[31, 'a'],[21, 'd'],[3, 'b'],[4, 'c'],[61, 'e'],[6, 'f'],[71, 'g'],[8, 'h'],[9, 'i']]

method = int(input("\n1 Linear Probing, 2 Double Hashing: "))

if method==1:
    while True:
        print("\n1 Insert \n2 Search \n3 Display \n4 Exit")
        ch=int(input("Enter your choice: "))

        if ch == 1:
            num = int(input("Enter Client Number: "))
            name = input("Enter Client Name: ")
            data = [num,name]
            Insert_LinearProbing(data,ht_size,ht)
        elif ch == 2:
            num = int(input("Enter Client Number: "))
            Search_LinearProbing(num,ht_size,ht)
        elif ch == 3:
            for j in range(ht_size):
                print(j,ht[j])
        else:
            print("Thank You! ")
            break

elif method==2:
    while True:
        print("\n1 Insert \n2 Search \n3 Display \n4 Exit")
        ch=int(input("Enter your choice: "))

        if ch == 1:
            num = int(input("Enter Client Number: "))
            name = input("Enter Client Name: ")
            data = [num,name]
            Insert_DoubleHashing(data,ht_size,ht,7)     #using prime number as 7<10(size of ht)
        elif ch == 2:
            num = int(input("Enter Client Number: "))
            Search_DoubleHashing(num,ht_size,ht,7)
        elif ch == 3:
            for j in range(ht_size):
                print(j,ht[j])
        else:
            print("Thank You! ")
            break

else:
    print("Enter a valid Method!")



    

    


