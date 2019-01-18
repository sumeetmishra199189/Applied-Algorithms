#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 21:43:58 2018

@author: sumeetmishra
"""
import ast 
input=open('/Users/sumeetmishra/Desktop/Applied_Algorithms/Assignment/Programming/Programming_Assignment-6/bipartite2.txt','r+')
input1=input.read()
input2=input1.strip().split()

d_node=int(len(input2))
d_node=int(input2[0])
adj_list={}
#print(d_node)
input3=[]
for i in range(1,len(input2)): # replaces '()' with '[]'
        input3.append(ast.literal_eval(input2[i].replace('(','[').replace(')',']')))
keys=[]
#print(input3)
#input5=[]   
for i in range(1,d_node+1): # puts parent-child into adjacency list
    input4=[]
    for j in input3:
        if i==j[0]:
            input4.append(j[1])
        elif i==j[1]:
            input4.append(j[0])
    adj_list[i]=input4
    #input5.append(adj_list[i])
#print(adj_list) 
#print(input5)    
q={} 
  
for i in range(1,d_node+1): #label parent and child with different colors
    if i not in keys:
       if len(adj_list[i]) != 0: 
           q[i]='r'
           keys.append(i)
           for j in adj_list[i]:
               q[j]='b'
               keys.append(j)
#print(q)
def cycle():  #this function determines if their exists a cycle or not by labeling 
              # different colors to parent and child,if some node(either parent or child) have 2 different colors then cycle exists
    k=[]
    key=[]
    c={}
    
    for i in range(1,d_node+1):
        if i not in key :
           k.append([i,'r'])
           key.append(i)
           for j in adj_list[i]:
               k.append([j,'b'])
               key.append(j)
        elif i in key:
            if [i,'r'] in k:
               for j in adj_list[i]:
                   k.append([j,'b'])
            elif [i,'b'] in k:
               for j in adj_list[i]:
                   k.append([j,'r'])       
               
    for i in range(1,d_node+1):
        ind=[]
        for j in k:
            if i==j[0]:
                ind.append(j[1])
        c[i]=ind
    #print(c)    
    for i in range(1,d_node+1):
        if 'r' in c[i] and 'b' in c[i]:
            #print(c[i])
            return True
    return False



if cycle():
    print('The graph is not bipartite') 
else:       
    b1=[]       
    b2=[]    
    for i in q.keys():
        if q[i]=='r':
            b1.append(i)
        else:
            b2.append(i)
    print('The 2 bipartite groups of vertices are- '+str(b1)+' and '+str(b2))    



    
    
    
    
    
    
    