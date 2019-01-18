#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 14:43:43 2018

@author: sumeetmishra
"""
import re
import heapq
import collections
input=open('/Users/sumeetmishra/Desktop/Applied_Algorithms/Assignment/Programming/Programming_Assignment-5/book.txt','r+')
'''
The book used for this program is-
'The Project Gutenberg eBook, Allen's West London Street Directory', 1868,
by Samuel Allen

The name of the book is changed to just book for simplicity.
'''
#input1='lorem ipsum dolor sit amet, consectetur adipiscing elit. sed et tortor metus. sed at luctus lorem. vivamus faucibus ipsum in diam aliquet, at suscipit augue posuere!'
input1=input.read().lower() #converting all the upper case characters to lowe case characters
#input2=input1.strip().split()
input3=re.sub('[^a-z|"\'"|"."|"!"|"?"|" "|","]+', '', input1) #replacing extra characters with ''
#print(input3)
freq_count = collections.Counter()
C = (" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
"p","q","r","s","t","u","v","w","x","y","z",".",",","?","!","\'")       #checking characters from C

for eachchar in C:
    freq_count[eachchar]=0
    
    
#counting frequency
for line in input3:
    for char in line:
        if char in C:
            if char in freq_count:
              freq_count[char] += 1
            else:
              freq_count[char] = 1

#print (freq_count)    
    

class node:                     #node class
    def _init_(self):
        self.left=None
        self.right=None
        self.char=None
        self.freq=None
    def __lt__(self,other):
        return self.freq<other.freq
           
        
        

Q =[]
sum_freq=0
#heapq.heapify(Q)
for c in C:		                #assigning frequency and characters to node and pushing it to heapq 						
    my_node = node()		
    my_node.char = c
    my_node.freq=freq_count[c]
    my_node.left=None
    my_node.right=None   		
    print(c, freq_count[c])
    sum_freq+=freq_count[c]
    heapq.heappush(Q, (freq_count[c], my_node))
#print(Q)
n=len(Q)
#print(n)

def Huffman(Q):                    #Huffman Tree 

    for i in range(0,n-1):
        z=node()
        
        x = heapq.heappop(Q)[1]
        z.left=x
        y= heapq.heappop(Q)[1]
        z.right=y
        z.freq=x.freq+y.freq
        heapq.heappush(Q,(z.freq,z))
    return heapq.heappop(Q)[1]

W={}                       #initialized dictionary for length calculation of bits
def traverseTree(node, bit):
    if node.left is None and node.right is None:	# if this is leaf node
        print (node.char, bit)			# print code (or save it somewhere else)
        W[node.char]=bit
    else:
        traverseTree(node.left, bit + '0')	# stick a 0 to the bit and continue down left
        traverseTree(node.right, bit + '1')	# stick a 1 to the bit and continue down right


a=Huffman(Q)
#print(a)
var_sum=0
traverseTree(a,'')    #Traversing through the tree recursively

#print(sum_freq)
fixed_length_encoding=5*sum_freq
var_length_encoding=0
for i in range(0,len(C)-1):
    length=len(W[C[i]])
    #print(length)
    var_length_encoding+=length*freq_count[C[i]]

difference=fixed_length_encoding-var_length_encoding
print('The text was encoded using '+str(var_length_encoding)+' bits')
print('The text had '+str(sum_freq)+ ' valid characters')
print('Using a 5-bit fixed length encoding, this would have been '+str(fixed_length_encoding)+' bits long')
print('So, we saved '+str(difference)+' bits!')












