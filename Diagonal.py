# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 21:26:24 2024

@author: ASUS
"""
#WAP to find diagonal of the matrix

list1=[[1,2,3,19],[2,5,6,89],[7,8,9,89],[2,5,5,6]]
lenght=len(list1)
print(list1)
for  i in range(lenght):
    for j in range(lenght):
        if i==j:
            print(i,j)
            print("Diagonal  =",list1[i][j])
        
       