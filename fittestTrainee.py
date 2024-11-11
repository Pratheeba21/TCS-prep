#Problem Statement: finding the fittest trainee among three trainees.


#Program:

t1,t2,t3=list(),list(),list()

for _ in range(3):
    x=int(input())
    if x not in range(1,101):
        print("Invalid input")
        break
    t1.append(x)
    x=int(input())
    if x not in range(1,101):
        print("Invalid input")
        break
    t2.append(x)
    x=int(input())
    if x not in range(1,101):
        print("Invalid input")
        break
    t3.append(x)

m=[sum(t1)//3, sum(t2)//3, sum(t3)//3]
maxFit=max(m)

if maxFit<70 :
    print("All trainees are unfit")
    

for i in range(3):
    if m[i]==maxFit:
        print(f"Trainee number: {i+1} , Average oxygen level: {m[i]}")
