# Problem Statement:  Finding the color that presents odd number of times.

#Program:

n=int(input())

B=list()

for i in range(n):
    B.append(input().lower())

for i in B:
    if B.count(i)%2!=0:
        print("\n",i)
        break
    
    else:
        print("All are even")
