print("Chatbot: Hello! I am a simple chatbot.")
print("Chatbot: Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("Chatbot: Goodbye! Have a nice day 😊")
        break

    elif "hello" in user_input or "hi" in user_input:
        print("Chatbot: Hello! How can I help you?")

    elif "how are you" in user_input:
        print("Chatbot: I'm doing great! Thanks for asking.")

    elif "your name" in user_input:
        print("Chatbot: I am a rule-based chatbot.")

    elif "help" in user_input:
        print("Chatbot: I can answer simple questions like greetings or my name.")

    else:
        print("Chatbot: Sorry, I didn't understand that.")