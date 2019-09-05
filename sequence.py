n = int(input("Enter the length of the sequence: "))
n1 = 1
n2 = 2
n3 = 3
for i in range(1,n+1):
    heild = n1 + n2 + n3
    print(heild)
    heild = n3
    n2 = n1
    n1 = n1
