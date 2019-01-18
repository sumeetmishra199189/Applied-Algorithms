#reading inputs and initializing variables
input=open('/Users/sumeetmishra/Desktop/Applied_Algorithms/Assignment/Programing Assignment-2/input.txt','r+')
input1=input.read()
input2=input1.strip().split()
input2= list(map(int, input2))
#test_3=[]

test_1=input2[:60]    #taking 1000 elements from input2 which can be modified
#for i in range(0,len(test_1)):
    #test_3.append(-1*abs(test_1[i]))

#test_1=abs(test_1)
#test_1=-1*(test_1)
#print(test_3)
#test_2=input2[:]
l=int(len(test_1)/2) #taking elements 500 at a time,total 20 iterations
#l1=int(len(test_2)/5000)
#l2=int(len(w)/2)
no_of_inputs = []
#import numpy as np
import matplotlib.pyplot as plt
import time

d_t_all1 = []
d_t_all2 = []
avg_time1=[]
avg_time2=[]
#brute force function
def brute_force(A):
    s=-999999999
    left_index=0
    right_index=0
    for i in range (0,len(A)):
        s1=0
        for j in range(i,len(A)):
            s1=s1+A[j]
            if(s1>s):
                s=s1
                #s1=0
                left_index=i
                right_index=j
#            else:
#                s1=0
    #print("max subarray:A["+str(left_index)+".."+str(right_index)+"]")
    #print("max sum:"+str(s))
    return(left_index,right_index,s)
#function that calls brute force 3 times
def time_and_3_observations_for_brute_force(A):
    for a in range(3):
        for k in range(1, l + 1):
            result = A[0:(k * 2)]
            t1 = time.clock()
            (a,b,c) = brute_force(result)
            t2 = time.clock()

            d_t_all1.append(t2 - t1)
    print("max subarray:A[" + str(a) + ".." + str(b) + "]")
    print("max sum:" + str(c))
    d_t1 = []
    d_t2 = []
    d_t3 = []
    #d_t1 = np.array(d_t_all1[0:20])
    #d_t2 = np.array(d_t_all1[20:40])
    #d_t3 = np.array(d_t_all1[40:60])
    #avg_time1=((d_t1 + d_t2 + d_t3) / 3)
    for i in range(0,len(d_t_all1),3):
        d_t1.append(d_t_all1[i])
    for i in range(1,len(d_t_all1),3):
        d_t2.append(d_t_all1[i])
    for i in range(2,len(d_t_all1),3):
        d_t3.append(d_t_all1[i])    
    for i in range(0,len(d_t1)):
        avg_time1.append((d_t1[i]+d_t2[i]+d_t3[i])/3)
    #print(avg_time1)
    
 # divide and conquer function,logic refered from text book CLRS   
def divide_and_conquer_cross(A,low,mid,high):

    left_sum=-999999999
    right_sum=0
    max_left=0
    max_right=0
    sum1=0
    sum2=0
    for i in range(mid,low,-1):
       sum1=sum1+A[i]
       if sum1>=left_sum:
          left_sum=sum1
          max_left=i
    for j in range(mid+1,high+1):
        sum2 = sum2 + A[j]
        if sum2 >= right_sum:
            right_sum = sum2
            max_right = j
    return (max_left,max_right,left_sum+right_sum)

def maximum_subarray(A,low,high):
    if (high == low):
        #print(low,high,A[low])
        return (low,high,A[low])
    else:

        mid = int((high + low)/2)
        #print 'mid is:',mid
        (left_low,left_high,left_sum) = maximum_subarray(A,low,mid)
        (right_low,right_high,right_sum) = maximum_subarray(A,mid+1,high)
        (cross_low,cross_high,cross_sum) = divide_and_conquer_cross(A,low,mid,high)

    if (left_sum >= right_sum and left_sum >= cross_sum):
        #print(left_low, left_high, left_sum)
        #print("max subarray:A[" + str(left_low) + ".." + str(left_high) + "]")
        #print("max sum:" + str(left_sum))
        return (left_low, left_high, left_sum)
    elif (right_sum >= left_sum and right_sum >= cross_sum):
        
        return (right_low,right_high,right_sum)
    else:
        
        return (cross_low,cross_high,cross_sum)
#function that calls divide and conquer 3 times
def time_and_3_observations_for_divide_and_conquer(A):
        for a in range(3):
            for k in range(1, l + 1):
                result = A[0:(k * 2)]
                t1 = time.clock()
                low = 0
                high = len(result) - 1
                (a, b, c) = maximum_subarray(result, low, high)
                t2 = time.clock()
     
                d_t_all2.append(t2 - t1)

        print("max subarray:A[" + str(a) + ".." + str(b) + "]")
        print("max sum:" + str(c))
        d_t4 = []
        d_t5 = []
        d_t6 = []
    
        for i in range(0,len(d_t_all2),3):
          d_t4.append(d_t_all2[i])
        for i in range(1,len(d_t_all2),3):
          d_t5.append(d_t_all2[i])
        for i in range(2,len(d_t_all2),3):
          d_t6.append(d_t_all2[i])    
        for i in range(0,len(d_t4)):
          avg_time2.append((d_t4[i]+d_t5[i]+d_t6[i])/3)
        
#calling the functions
time_and_3_observations_for_brute_force(test_1)
time_and_3_observations_for_divide_and_conquer(test_1)
#taking input as x
no_of_inputs = []
for n in range(1, l + 1):
    no_of_inputs.append(n * 2)
#plot refered from the below site
#https://stackoverflow.com/questions/22276066/how-to-plot-multiple-functions-on-the-same-figure-in-matplotlib
plt.plot(no_of_inputs, avg_time1, 'r',label='Brute Force') 
plt.plot(no_of_inputs, avg_time2, 'b',label='Divide and Conquer') 

plt.xlabel('Number of Inputs')
plt.ylabel('Average Time in Seconds')
plt.title('Brute Force Vs Divide and Conquer')
plt.legend(loc='upper right')
plt.show()














