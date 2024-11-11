#Problem Statement:Calculating the total bus fare between give stops.


#Program:

import math

busStops=['TH','GA','IC','HA','TE','LU','NI','CA']

Paths=[800,600,750,900,1400,1200,1100,1500]

def getFare(source,destination):
    distance=0
    if source not in busStops and destination not in busStops:
        return -1

    elif busStops.index(source) < busStops.index(destination):
        distance+=sum(Paths[busStops.index(source) : busStops.index(destination)+1])

    elif busStops.index(source) > busStops.index(destination):
        distance+=sum(Paths[:busStops.index(destination)+1])+sum(Paths[busStops.index(source) : ])

    elif source==destination:
        distance=0

    return float(math.ceil(distance*0.005))


source=input()
destination=input()
TotalFare=getFare(source,destination)

if TotalFare==-1 or TotalFare==0:
    print("Invalid input")
else:
    print(TotalFare,"INR")
            
                 
