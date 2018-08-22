##Given you have temperature data from two sensors, calculate the average temperature for each
##one second duration across both sensors.
##Constraints
import os
import csv
if __name__=="__main__":
    m=0
    j=0
    k=0
    l=0
    #print(i)
    temp=0
    temp1=0
    temp2=0
    temp3=0
    with open ('test.csv','r') as csvfile:
        a=csv.reader(csvfile)
        
        for row in a:
            row = [int(i) for i in row]
            #row(1) = int(row(1))
            #print row[1]
            if row[1] in range(10000,10999):
                m+=1
                temp=temp+row[2]
               
            elif row[1] in range(11000,11999):
                j+=1
                temp1=temp1+row[2]
                
            elif row[1] in range(12000,12999):
                k+=1
                temp2=temp2+row[2]
            elif row[1] in range(13000,13999):
                l+=1
                temp3=temp3+row[2]
            else:
                print("check the input data")
        
        print "the rage is 10000-10999 :", float(temp)/float(m)
        print "the rage is 11000-11999 :", float(temp1)/float(j)
        print "the rage is 12000-12999 :", float(temp2)/float(k)
        print "the rage is 13000-13999 :", float(temp3)/float(l)

