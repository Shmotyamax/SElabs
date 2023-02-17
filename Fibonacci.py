size=int(input("Choose the size of sequence"))
n=[0,1]
for i in range(size):
    print(n[-1])
    n.append(n[-1]+n[-2])