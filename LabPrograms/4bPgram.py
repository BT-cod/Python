# Roman to Integer Conversion
def romanToInt(romanStr):
    roman_list = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    romanCal = list(romanStr[::-1])
    value = 0
    RHS = roman_list[romanCal[0]]
    for eachNumber in romanCal:
        LHS = roman_list[eachNumber]
        if LHS < RHS:
            value -= LHS
        else:
            value += LHS
        RHS = LHS
    return value

romanStr = input("Enter Roman Number To Convert: ")
print(romanToInt(romanStr))