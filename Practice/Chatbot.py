def chatbot(user_input):
    user = user_input.lower().strip()

    if "hello" in user or "hi" in user or "hey" in user:
        return "Hello! How can I help you today?"
    elif "track" in user or "order" in user:
        return "Please provide your order number to track your shipment, you will get updates on your registered email."
    elif "return" in user or "refund" in user:
        return "Our return policy allows 30 days. What's your order number?"
    elif "price" in user or "cost" in user:
        return "What product would you like to know the price of?"
    elif "problem" in user or "issue" in user or "broken" in user:
        return "I'm sorry to hear that. Can you describe the issue?"
    elif "thank" in user:
        return "You're welcome! Anything else?"
    elif "bye" in user or "exit" in user or "quit" in user:
        return "Thank you for contacting us. Goodbye!"
    elif user.isdigit():
        return "Thanks for providing the number. Let me check that for you."
    else:
        return "I'm not sure I understand. Could you rephrase that?"
    
def main():
    print("Type 'bye' to exit\n")
    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        response = chatbot(user_input)
        print(f"Bot: {response}\n")
        if "bye" in user_input.lower() or "exit" in user_input.lower():
            break

main()