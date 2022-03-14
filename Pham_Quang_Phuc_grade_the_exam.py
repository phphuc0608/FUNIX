import pandas as pd
import numpy as np

def splt(word):
    return [char for char in word]

def studentidnum(studentid_num):
    for i in range (1, len(studentid_num)):
        if studentid_num[i] != "1" and studentid_num[i] != "2" and studentid_num[i] != "3" and studentid_num[i] != "4" and studentid_num[i] != "5" and studentid_num[i] != "6" and studentid_num[i] != "7" and studentid_num[i] != "8" and studentid_num[i] != "9" and studentid_num[i] != "0":
            return 1
        else: 
            return 0


filename=input("Enter a filename: ")
try:
    file = open(str(filename+".txt"),"r")
    print("Successfully opened", str(filename+".txt"))


except:
    print("File can't be found, please try again")
#------------------------------------------
print("**** ANALYZING ****")
line_count = 0
invalid=0
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
key=answer_key.split(",")
student_score = []
for line in file:
    if line !="\n":
        line_count +=1
    ln=line.split(",")
    studentid=splt(ln[0])
    if len(ln)!=26:
        print("Invalid line of data: does not contain exactly 26 values:\n",line)
        invalid+=1
    elif studentid[0]!="N" or len(studentid)!= 9 or studentidnum(studentid)==1:
        print("Invalid line of data: N# is invalid\n",line)
        invalid+=1
if invalid==0:
    print("No errors found!")
print("**** REPORT ****")
print("Total valid lines of data:", line_count-invalid)
print("Total invalid lines of data:", invalid)

"""
for i in range (0, line_count-1):
    score=0
    if len(ln)==26 and studentid[0]=="N" and len(studentid)== 9 or studentidnum(studentid)==0:
        for j in range (0, len(key)):
            if ln[j+1] == key[j]:
                score+=4
            elif ln[j+1]==" ":
                score+=0
            else :
                score-=1
        print(score)
"""

