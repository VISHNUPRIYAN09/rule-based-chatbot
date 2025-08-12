# Simple rule-based chatbot using if-else

print("Chatbot: Hi! I am your assistant. Type 'bye' to exit.")

while True:
    user_input = input("You: ").strip().lower()  # Strips whitespace and converts to lowercase for easy comparison

    # Handle empty input
    if not user_input:
        print("Chatbot: Please say something!")  # Prompt if no input is given
    elif user_input in ['hi', 'hello']:
        print("Chatbot: Hello! How can I help you today?")  # Responds to greetings
    elif user_input in ['how are you', 'how are you doing']:
        print("Chatbot: I'm just a bot, but I'm doing great! Thanks for asking.")  # Responds to 'how are you'
    elif 'your name' in user_input:
        print("Chatbot: I am a simple chatbot built with Python.")  # Responds to name questions
    elif user_input in ['bye', 'exit', 'quit']:
        print("Chatbot: Goodbye! Have a nice day.")  # Exits the chatbot
        break
    else:
        print("Chatbot: Sorry, I didn't understand that.")  # Default response for unrecognized input