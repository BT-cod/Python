
# Sentence Statistics

# sentence = input("Enter your sentence: ")
# word = sentence.split(" ")
# print("Your sentence has ", len(word), " number of words")
# numcnt = upcnt = locnt = 0

# for characters in sentence:
#     if "0" <= characters <= "9":
#         numcnt += 1
#     elif "A" <= characters <= "Z":
#         upcnt += 1
#     elif "a" <= characters <= "z":
#         locnt += 1

# print("Your Sentence has ", numcnt, "number of integers, " , upcnt, "number of Upper case letters and", locnt, "number of lower case letters")

# String Similarity

# string1 = input("Enter your 1st string: \n")
# string2 = input("Enter your 2nd string: \n")
# if len(string1) < len(string2):
#     short = len(string1)
#     long = len(string2)
# else:
#     short = len(string2)
#     long = len(string1)
# letterCnt = 0
# for characters in range(short):
#     if string1[characters] == string2[characters]:
#         letterCnt += 1
# print("The similarity between given strings was: ", letterCnt/long)


import random
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])
    
    merged = []
    i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1
    merged.extend(left_half[i:])
    merged.extend(right_half[j:])
    return merged

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

my_list = [random.randint(0, 999) for _ in range(10)]

print("\nUnsorted List")
print(my_list)
print("\nSorting using Insertion Sort")
insertion_sort(my_list)
print(my_list)
my_list = [random.randint(0, 999) for _ in range(10)]
print("\nUnsorted List")
print(my_list)
print("\nSorting using Merge Sort")
my_list = merge_sort(my_list)
print(my_list)


