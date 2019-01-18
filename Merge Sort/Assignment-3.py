#declaring variables
input=open('/Users/sumeetmishra/Desktop/Applied_Algorithms/Assignment/Programing Assignment-3/input.txt','r+')
input1=input.read()
input2=input1.strip().split()
input2= list(map(int, input2))#file with 100000 inputs
n = len(input2)
l=int(len(input2)/5000)
no_of_inputs = []
import matplotlib.pyplot as plt
import time
d_t_all = []
avg_time=[]

#merge function defintion
def Merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r- q

    L = [0] * (n1)
    R = [0] * (n2)


    for i in range(0 , n1):
        L[i] = A[p + i]
    for j in range(0 , n2):
        R[j] = A[q + 1 + j]

    i = 0
    j = 0
    k = p

    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1


    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1


    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1

#recursively calling merge function to sort and merge after dividing it into 2 sub arrays
def Merge_Sort(A,p,r):
    if p < r:
        q = int((p+(r-1))/2)
        Merge_Sort(A, p, q)
        Merge_Sort(A, q+1, r)
        Merge(A, p, q, r)

#function that calls merge sort 3 times
def time_and_3_observations_for_Merge_Sort(A):
        for a in range(3):
          for k in range(1, l + 1):
             result = A[0:(k * 5000)]
             low = 0
             high = len(result)-1
             t1 = time.clock()
             Merge_Sort(result, low, high)
             t2 = time.clock()
             d_t_all.append(t2 - t1)


        d_t1 = []
        d_t2 = []
        d_t3 = []

        for i in range(0,20):
          d_t1.append(d_t_all[i])
        for i in range(20,40):
          d_t2.append(d_t_all[i])
        for i in range(40,60):
          d_t3.append(d_t_all[i])
        for i in range(0,len(d_t1)):
          avg_time.append((d_t1[i]+d_t2[i]+d_t3[i])/3)
          #print(avg_time)

no_of_inputs = []
for n in range(1, l + 1):
    no_of_inputs.append(n * 5000)
time_and_3_observations_for_Merge_Sort(input2)

#plot refered from the below site
#https://stackoverflow.com/questions/22276066/how-to-plot-multiple-functions-on-the-same-figure-in-matplotlib
plt.plot(no_of_inputs, avg_time)
plt.xlabel('Number of Inputs')
plt.ylabel('Average Time in Seconds')
plt.title('Merge Sort')
plt.show()

####Question2#######
def divide_into_five_groups(A):

    # looping till length A
    for i in range(0, len(A), 5):
        yield A[i:i + 5]

def insertionSort(A):
    # Traverse through 1 to len(A)
    for i in range(1, len(A)):

        key = A[i]
        #print('in insertion sort')
        # Move elements of A[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < A[j]:
            A[j + 1] = A[j]
            j =j-1
        A[j + 1] = key


def findMedian(A, n):#median function to find median of an array
    insertionSort(A)
    return A[int(n / 2)]



def MedianOfMedian(A, l, r, k): #finding medians of all the medians found with the above function
        B=list(divide_into_five_groups(A))
        median=[0]*len(B)
        for i in range(0,len(B)):
          if len(B[i])==1:
            median[i]=B[i][0]
          else:
           median[i]=findMedian(B[i], len(B[i]))

        # Find median of all medians using recursive call.
        # If median[] has only one element, then no need
        # of recursive call
        #medOfMed =[]
        if len(median) == 1:
            medOfMed=median[0]
        else:
            medOfMed=MedianOfMedian(median, 0, len(median), int((len(median)-1) / 2))
        return medOfMed

Median_of_Medians=MedianOfMedian(input2,0,n-1,k)
print(Median_of_Medians)
