print("Welcome to a Basic Chatbot")

while True:
    user = input("You: ").lower()

    if user in ["hello", "hi", "hii", "hlo"]:

        print("Bot: Hi 😊! Nice to meet you. What is your name?")
        name = input("You: ")

        print(f"Bot: Nice to meet you, {name}! How are you?")
        reply = input("You: ").lower()

        if "fine" in reply or "good" in reply:
            print(f"Bot: Great, {name}! How can I help you?")

        elif "bad" in reply or "sad" in reply:
            print("Bot: I hope you feel better soon.")

        else:
            print("Bot: Okay 😊")

    elif "who are you" in user:
        print("Bot: I am a simple Python chatbot.")

    elif "what is python" in user:
        print("Bot: Python is a popular programming language.")

    elif "who built you" in user or "who created you" in user:
        print("Bot: i was created by Maneesha using python.")

    elif "what is your work" in user or "what do you do" in user:
        print("Bot: i chat with users and answer simple questions.")

    elif "thanks" in user:
        print("Bot: You're welcome!")

    elif "bye" in user:
        print("Bot: Bye 👋 Have a great day!")
        break

    else:
        print("Bot: Sorry, I don't understand.")