#Problem Statement : Maximum guests arriving at an hour.



#Proggram:

t=int(input())

e=input()
e=e.split()
e=[int(i) for i in e]

l=input()
l=l.split()
l=[int(i) for i in l]

r=0
guests=list()
for i in range(t):
   r=r+e[i]-l[i] 
   guests.append(r)

print(max(guests))
   
