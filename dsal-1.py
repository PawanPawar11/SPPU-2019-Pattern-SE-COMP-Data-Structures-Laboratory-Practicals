s1 = []
s2 = []

def add(st, e):
    st.append(e)

def rem(st, e):
    st.remove(e)

def size(st):
    n = 0
    for i in range(len(st)):
        n += 1
    return n

def contains(st):
    for i in range(len(st)):
        print(st[i], end=" ")

def union(set1, set2):
    u_set = []
    for e in set1:
        if e not in u_set:
            u_set.append(e)
    for e in set2:
        if e not in u_set:
            u_set.append(e)
    return u_set

def intersect(set1, set2):
    i_set = []
    for e in set1:
        if e in set2:
            i_set.append(e)
    return i_set

def differ(set1, set2):
    d_set = []
    for e in set1:
        if e not in set2:
            d_set.append(e)
    return d_set

def subset(set1, set2):
    for e in set1:
        if e not in set2:
            return False
    return True

def proper(set1, set2):
    for e in set1:
        if e not in set2 and len(set2) < len(set1):
            return False
    return True

n1 = int(input("Number of elements you want to enter in set1: "))
print("Enter set 1 elements: ")
for i in range(n1):
    n = int(input())
    if n not in s1:
        add(s1, n)

n2 = int(input("Number of elements you want to enter in set2: "))
print("Enter set 2 elements: ")
for j in range(n2):
    n = int(input())
    if n not in s2:
        add(s2, n)

while True:
    print("\n1 Add ")
    print("2 Remove ")
    print("3 Size ")
    print("4 Display ")
    print("5 Union ")
    print("6 Intersection ")
    print("7 Difference ")
    print("8 Subset ")
    print("9 Proper Subset")
    print("10 Exit ")
    ch = int(input("Enter Choice: "))
    if ch == 1:
        st = int(input("Enter set "))
        ele = int(input("Enter element "))
        if st == 1:
            print(ele, " added to set 1")
            if ele not in s1:
                add(s1, ele)
        if st == 2:
            print(ele, " added to set 2")
            if ele not in s2:
                add(s2, ele)
        print()
    elif ch == 2:
        st = int(input("Enter set "))
        ele = int(input("Enter element "))
        if st == 1:
            rem(s1, ele)
        if st == 2:
            rem(s2, ele)
        print()
    elif ch == 3:
        st = int(input("Enter set "))
        if st == 1:
            print("Size of set 1: ", size(s1))
        if st == 2:
            print("Size of set 2: ", size(s2))
        print()
    elif ch == 4:
        st = int(input("Enter set "))
        if st == 1:
            print("Set 1 elements: ", end=" ")
            contains(s1)
        if st == 2:
            print("Set 2 elements: ", end=" ")
            contains(s2)
        print()
    elif ch == 5:
        print("Union of sets: ", union(s1, s2))
    elif ch == 6:
        print("Intersection of sets: ", intersect(s1, s2))
    elif ch == 7:
        print("Difference set1-set2: ", differ(s1, s2))
    elif ch == 8:
        if subset(s1, s2):
            print("Set1 is subset of Set2")
        else:
            print("Set1 is not subset of Set2")
    elif ch == 9:
        if proper(s1, s2):
            print("Set1 is proper subset of Set2")
        else:
            print("Set1 is not proper subset of Set2")
    elif ch == 10:
        break
