# Create an object consisting of User details like name, age, gender and phoneNo.
# After creating an object print a single element of the user object by asking the input from the user.
# example: if the user gives the input of name, then only names of all the users should be diplayed or
# if the user gives the input of phonoNo, then only phonoNos of all the users should be diplayed

usrIpt = input("Enter Parameter to search:\nSuch as name, age and address: \n ==> ")
userLst = [
    {
        "name": "Name1",
        "address": "Address1",
        "age": 10
    },
    {
        "name": "Name2",
        "address": "Address2",
        "age": 12
    },
    {
        "name": "Name3",
        "address": "Address3",
        "age": 13
    },
    {
        "name": "Name4",
        "address": "Address4",
        "age": 14
    },
    {
        "name": "Name5",
        "address": "Address5",
        "age": 15
    },
    {
        "name": "Name6",
        "address": "Address6",
        "age": 16
    }
]

if usrIpt == "name" or usrIpt == "age" or usrIpt == "address":
        for user in userLst:
                print(user[usrIpt])
else:
        print("Enter Valid Parameter and try again")
