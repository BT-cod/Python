import re

phone_regex = re.compile(r'\+\d{12}')
email_regex = re.compile(r'[A-Za-z0-9._]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}')

with open('example.txt', 'r') as f:
    for line in f:
        phone_matches = phone_regex.findall(line)
        email_matches = email_regex.findall(line)
        print(*phone_matches)
        print(*email_matches)