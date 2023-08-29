# Write a python program to find the whether the given input is palindrome or not (for both
# string and integer) using the concept of polymorphism and inheritance.

# class PaliStr:
#  def __init__(self):
#         self.isPali = False

#  def chkPalindrome(self, myStr):
#         if myStr == myStr[::-1]:
#                 self.isPali = True
#         else:
#                 self.isPali = False

#         return self.isPali

# class PaliInt(PaliStr):
#  def __init__(self):
#         self.isPali = False

#  def chkPalindrome(self, val):
#         temp = val
#         rev = 0
#         while temp != 0:
#                 dig = temp % 10
#                 rev = (rev*10) + dig
#                 temp = temp //10

#         if val == rev:
#                 self.isPali = True
#         else:
#                 self.isPali = False

#         return self.isPali
# st = input("Enter a string : ")
# stObj = PaliStr()
# if stObj.chkPalindrome(st):
#  print("Given string is a Palindrome")
# else:
#  print("Given string is not a Palindrome")
# val = int(input("Enter a integer : "))
# intObj = PaliInt()
# if intObj.chkPalindrome(val):
#  print("Given integer is a Palindrome")
# else:
#      print("Given integer is not a Palindrome")


#SuperClass
class Palindrome:
    def __init__(self):
        pass
#SubClass to check string
    def chkPalindrome(self, value):
        return str(value) == str(value)[::-1]
#SubClass to check number
class PalindromeInteger(Palindrome):
    def chkPalindrome(self, value):
        temp = value
        rev = 0
        while temp != 0:
            dig = temp % 10
            rev = (rev * 10) + dig
            temp = temp // 10
        return value == rev
#Take input and print output for string
st = input("Enter the string: ")
stObj = Palindrome()
if stObj.chkPalindrome(st):
    print("Given String is Palindrome")
else:
    print("Given String is not Palindrome")
#Take input and print output for number
val = int(input("Enter the number: "))
valObj = PalindromeInteger()
if stObj.chkPalindrome(val):
    print("Given Number is Palindrome")
else:
    print("Given Number is not Palindrome")


# temp is initialized with the value 1221.
#   In the first iteration of the loop:
#       dig is assigned the value 1221 % 10, which is 1.
#       rev is updated to 0 * 10 + 1, which becomes 1.
#       temp is updated to 1221 // 10, which becomes 122.
#   In the second iteration:
#       dig is assigned the value 122 % 10, which is 2.
#       rev is updated to 1 * 10 + 2, which becomes 12.
#       temp is updated to 122 // 10, which becomes 12.
#   In the third iteration:
#       dig is assigned the value 12 % 10, which is 2.
#       rev is updated to 12 * 10 + 2, which becomes 122.
#       temp is updated to 12 // 10, which becomes 1.
#   In the fourth iteration:
#       dig is assigned the value 1 % 10, which is 1.
#       rev is updated to 122 * 10 + 1, which becomes 1221.
#       temp is updated to 1 // 10, which becomes 0.