print("Simple ChatBot!")
print("Enter 'bye' to exit.")

while True:
    user = input("You: ").lower()
    
    if user == "hi" or user == "hello":
        print("Bot: Hello!, How can i help you?")
    elif user == "how are you":
        print("Bot: I'm doing great!")
    elif user == "what is your name":
        print("Bot: My name is ASIF'S BOT.")
    elif user == "what does it means":
        print("Bot: it means i'm maked by ASIF.")
    elif user == "who made you":
        print("Bot: I was created using Python.")
    elif user == "what can you do":
        print("Bot: I can chat with you and answer simple questions.")
    elif user == "tell me a joke":
        print("Bot: Why do programmers prefer Python? Because it's easy!")
    elif user == "which language do you use":
        print("Bot: I use Python language.")
    elif user == "what is python":
        print("Bot: Python is a popular programming language.")
    elif user == "what is your favorite color":
        print("Bot: I like blue.")
    elif user == "do you like coding":
        print("Bot: Yes! Coding is fun.")
    elif user == "good morning":
        print("Bot: Good morning! Have a nice day.")
    elif user == "good night":
        print("Bot: Good night! Sleep well.")
    elif user == "thank you":
        print("Bot: You're welcome!")
    elif user == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand.")

