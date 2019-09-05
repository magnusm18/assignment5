n = int(input("Enter the length of the sequence: "))
n1 = 1
n2 = 2
n3 = 3
print(n1)
print(n2)
print(n3)
for i in range(1,n-2):
    heild = n1+n2+n3
    n1 = n2
    n2 = n3
    n3 = heild
    print(heild)