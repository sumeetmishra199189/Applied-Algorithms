input=open('/Users/sumeetmishra/Desktop/Applied_Algorithms/Assignment/Programing Assignment-1/input.txt','r+')

input1=input.read()
input2=input1.strip().split()
input2= list(map(int, input2))
l=int(len(input2)/500)
import time
avg_time=[]
d_t1=[]
d_t2=[]
d_t3=[]
d_t_all=[]
for a in range(3):
  for k in range(1,l+1):
      result=input2[0:(k*500)]
      t1=time.clock()
      for j in range(len(result)):
         key=result[j]
         i=j-1
         while i>=0 and result[i]>key:
             result[i+1]=result[i]
             i=i-1
             result[i+1]=key
      t2=time.clock()
      d_t_all.append(t2-t1)
      #print(d_t_all)
import numpy as np
d_t1=np.array(d_t_all[0:20])
d_t2=np.array(d_t_all[20:40])
d_t3=np.array(d_t_all[40:60])
avg_time=(d_t1+d_t2+d_t3)/3
#print(avg_time)
no_of_inputs=[]
for n in range(1,l+1):
   no_of_inputs.append(n*500)
import matplotlib.pyplot as plt
plt.plot(no_of_inputs,avg_time)
plt.xlabel('Number of Inputs')
plt.ylabel('Average Time for Sorting in Seconds')
plt.title('Inputs Vs Average Time')
