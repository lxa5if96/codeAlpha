import os
import re

base_dir = os.path.dirname(os.path.abspath(__file__))

input_file = os.path.join(base_dir, "data.txt")
output_file = os.path.join(base_dir, "email.txt")

with open(input_file, "r") as file:
    content = file.read()

emails = re.findall(
    r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
    content
)

with open(output_file, "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Email addresses extracted and saved to email.txt")