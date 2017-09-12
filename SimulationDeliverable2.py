# -*- coding: utf-8 -*-
# [CSC 591] IoT Analytics
# Simulation Task 2
import math
import random
import sys
sys.stdout = open("output.txt", "w")

def run_simulation(mean_inter_arr_time,mean_orbitting_time,service_time,q_size,final_MC):
    print("\n")
    print("Sl. No.", "MC", "CLA", "CLS", "BUFFER", "CLR")
    index=1
    MC=0
    cla=2 
    cls=0
    currentBufferSize=0
    maxbufferSize=q_size
    serviceTime=service_time
    eventList=[cla,cls]
    while MC<=final_MC:
        print(index, MC, eventList[0], eventList[1],currentBufferSize, eventList[2:len(eventList)])
        orbittingTime= -mean_orbitting_time * math.log(random.random())
        interArrivalTime= -mean_inter_arr_time * math.log(random.random())
        index = index+1
        if(MC == 0):
            MC = cla
            eventList[0] = eventList[0]+interArrivalTime
            eventList[1] = MC+serviceTime
            currentBufferSize = currentBufferSize+1
        else:
            MC = min(eventList)
            if(len(eventList)>2 and MC == min(eventList[2:len(eventList)])):
                del eventList[2]
                if(currentBufferSize < maxbufferSize):
                    currentBufferSize = currentBufferSize+1
                else:
                    eventList.append(MC+orbittingTime)
            elif(MC == eventList[0]):
                eventList[0] = eventList[0]+interArrivalTime
                if(currentBufferSize < maxbufferSize):
                    currentBufferSize = currentBufferSize+1
                else:
                    eventList.append(MC+orbittingTime)  
            elif(MC == eventList[1]):
                eventList[1] = eventList[1]+serviceTime
                currentBufferSize=currentBufferSize-1
mean_inter_arr_time = int(input("Enter mean inter-arrival time  :"))
mean_orbitting_time = int(input("Enter mean orbiting time  :"))
service_time = int(input("Enter service time  :"))
q_size = int(input("Enter buffer size  :"))
final_MC = int(input("Enter termination value for MC  :"))
run_simulation(mean_inter_arr_time,mean_orbitting_time,service_time,q_size,final_MC)
            
    # -*- coding: utf-8 -*-