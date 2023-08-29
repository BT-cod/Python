# Write a python program to accept a file name from the user and perform the following operations
# 1. Display the first N line of the file
# 2. Find the frequency of occurrence of the word accepted from the user in the file

#import section
import os.path
import sys

#check and open file
fname = input("Enter The Filename: ")
if not os.path.isfile(fname):
    print("File", fname, "doesn't exist")
    sys.exit(0)

with open(fname, "r") as infile:
    lineList = infile.readlines()

#read and print
for i, line in enumerate(lineList[:10], 1):
    print(i, ":", line, end="")

#count and print
word = input("Enter The Word: ")
cnt = sum(line.count(word) for line in lineList)
print("The word", word, "repeated", cnt, "times in the file")