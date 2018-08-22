##Seating Arrangement. You have n students and n chairs in an exam hall. n/3 students are writing
##Maths, n/3 are writing physics and n/3 are writing chemistry. The n chairs are arranged in two
##rows, with n/2 in each row. Write an algorithm to make sure no two maths students sit either
##next/in front/behind of another maths students.

import os
import sys
a=['M','P','C']
n=18 #you can give n value 
row=n/2
if __name__=="__main__":
    for i in range(0,2): # 2 rows 
        
        for j in range (i,row+i): # n/2 rows for each person
            j=j%3  # n/3 writing Maths, n/3 are writing physics and n/3 are writing chemistry.
            print a[j],
        print "\n"
       