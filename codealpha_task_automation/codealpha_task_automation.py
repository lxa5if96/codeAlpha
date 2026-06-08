import re

with open('file_name.txt', 'r') as file:
    content = file.read()

emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)

with open('email.txt', 'w') as file:
    for email in emails:
        file.write(email + "\n")

print("Email address extracted and saved to emails.txt")