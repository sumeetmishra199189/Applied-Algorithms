#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 19:57:51 2018

@author: sumeetmishra
"""
# Initialized X,Y values as given in the test case
#X=['A','B','C','B','D','A','B']
#Y=['B','D','C','A','B','A']
X=[1,0,0,1,0,1,0,1]
Y=[0,1,0,1,1,0,1,1,0]

#lengths of the arrays
m=len(X)
n=len(Y)
A=[] #taken for final array output

def lcs_length(X,Y):            
#    
    b=[[0 for x in range(m+1)] for x in range(n+1)]      #initialized array b with all 0's
    c=[[0 for x in range(m+1)] for x in range(n+1)]      #initialized array c with all 0's

    #for i in range(0,m):
     #   c[i][0]=0
    #for j in range(0,n+1):
    #    c[0][j]=0
 #mathching values of X[i] and Y[j]        
    for i in range(1,m+1):
        for j in range(1,n+1):
        
            if X[i-1]==Y[j-1]:             
              c[i-1][j-1]=c[i-2][j-2]+1
              b[i-1][j-1]=1               #taken 1 for left diagonal position given as arrow symbol in text book
            elif(c[i-2][j-1]>=c[i-1][j-2]):
              c[i-1][j-1]=c[i-1][j-1]
              b[i-1][j-1]=2                  #taken 2 for top row position given as arrow symbol in text book
            else:
              c[i-1][j-1]=c[i-1][j-2]
              b[i-1][j-1]=3            #taken 3 for left column position given as arrow symbol in text book
             
    return (c,b)  
def print_lcs(b,X,i,j):      #this function prints the matching sub sequence of both the arrays
 
 if(i==0 or j==0):
     return
 if(b[i-1][j-1]==1):            #matches 1 then call recursively with left diagonal value
     print_lcs(b,X,i-1,j-1)
     A.append(X[i-1])
 elif(b[i-1][j-1]==2):       #matches 2 then call recursively with top row value
     print_lcs(b,X,i-1,j)
 else:                       #matches 3 then call recursively with left column value
     print_lcs(b,X,i,j-1)
 return(A)
(C,B)=lcs_length(X,Y)
arr=print_lcs(B,X,m,n)
print(arr)






