# # Write a program that will take user input and convert it into capital letters
# # input -- "helloworld"
# # output -- "HELLOWORLD"

# name = input("Enter Your Name: ")
# capitalizedName = name.lower()
# print("Output: ", capitalizedName)

# # Write a Program, that takes user input and Use these string methods.
# #-------------------------------------------------------------------------------
# #2 lower()	Converts a string into lower case

# # name = input("Enter Your Name: ")
# # loweredName = name.lower()
# # print("Output: ", loweredName)

# #-------------------------------------------------------------------------------
# #3 capitalize()	Converts the first character to upper case

# # name = input("Enter Your Name: ")
# # capitalName = name.capitalize()
# # print("Output: ", capitalName)

# #-------------------------------------------------------------------------------
# #4 swapcase()	Swaps cases, lower case becomes upper case and vice versa

# # name = input("Enter Your Name: ")
# # swapName = name.swapcase()
# # print("Output: ", swapName)

# #-------------------------------------------------------------------------------
# #5 title()	Converts the first character of each word to upper case

# # name = input("Enter Your Name: ")
# # titleName = name.title()
# # print("Output: ", titleName)

# import library
from twilio.rest import Client
import random

# Replace these values with your actual Twilio Account SID and Auth Token
account_sid = 'ACcab7a6f77a1c668bf3527f5390c560ff'
auth_token = 'f86d5a8e38721e0703236e34f6870065'

# Your Twilio phone number (must be purchased from Twilio)
twilio_phone_number = 'your_twilio_phone_number'

# Your friend's mobile number (replace with the actual number)
friend_mobile_number = '+919731231817'

# Generate a random 6-digit OTP
otp = str(random.randint(100000, 999999))

# Message to be sent
message_body = f'Your OTP is: {otp}'

# Initialize the Twilio client
client = Client(account_sid, auth_token)

# Send the OTP via SMS
message = client.messages.create(
    body=message_body,
    from_=twilio_phone_number,
    to=friend_mobile_number
)

print(f'OTP sent to {friend_mobile_number}')
