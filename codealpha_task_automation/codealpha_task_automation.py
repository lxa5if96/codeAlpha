import re

try:
    with open("file_name.txt", "r") as file:
        content = file.read()

    emails = re.findall(
        r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
        content
    )

    with open("email.txt", "w") as file:
        for email in emails:
            file.write(email + "\n")

    print("Email addresses extracted and saved to email.txt")

except FileNotFoundError:
    print("Input file not found. Please check the file name and location.")