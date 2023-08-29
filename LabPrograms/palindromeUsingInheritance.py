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
st = input("Enter a string: ")
stObj = Palindrome()
if stObj.chkPalindrome(st):
    print("Given string is a Palindrome")
else:
    print("Given string is not a Palindrome")

#Take input and print output for number
val = int(input("Enter an integer: "))
intObj = PalindromeInteger()
if intObj.chkPalindrome(val):
    print("Given integer is a Palindrome")
else:
    print("Given integer is not a Palindrome")


