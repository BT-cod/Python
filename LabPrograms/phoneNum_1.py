# import re

# def is_valid_phone_number(numStr):
#     return len(numStr) == 12 and numStr[3] == numStr[7] == '-' and numStr.replace('-', '').isdigit()

# def check_phone_number(numStr):
#     return bool(re.match(r'^\d{3}-\d{3}-\d{4}$', numStr))

# ph_num = input("Enter a phone number: ")

# print("Without using Regular Expression")
# print("Valid phone number" if is_valid_phone_number(ph_num) else "Invalid phone number")

# print("Using Regular Expression")
# print("Valid phone number" if check_phone_number(ph_num) else "Invalid phone number")

import re
def isphonenumber(numStr):
 if len(numStr) != 12:
    return False
 for i in range(len(numStr)):
    if i==3 or i==7:
        if numStr[i] != "-":
            return False
    else:
        if numStr[i].isdigit() == False:
            return False
 return True
def chkphonenumber(numStr):
 ph_no_pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
 if ph_no_pattern.match(numStr):
    return True
 else:
    return False
ph_num = input("Enter a phone number : ")
print("Without using Regular Expression")
if isphonenumber(ph_num):
 print("Valid phone number")
else:
    print("Invalid phone number")
print("Using Regular Expression")
if chkphonenumber(ph_num):
 print("Valid phone number")
else:
 print("Invalid phone number")

