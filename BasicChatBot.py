import random

def get_response(user_input):
    """
    Returns a response based on user input using rule-based matching
    """
    # Convert input to lowercase for easier matching
    user_input = user_input.lower().strip()
    
    # Greeting responses
    if user_input in ["hello", "hi", "hey", "greetings"]:
        responses = ["Hi!", "Hello there!", "Hey! How can I help you?", "Greetings!"]
        return random.choice(responses)
    
    # How are you responses
    elif user_input in ["how are you", "how are you?", "how's it going", "how are things"]:
        responses = ["I'm fine, thanks!", "I'm doing great! How about you?", 
                     "Pretty good! Thanks for asking.", "I'm excellent, thank you!"]
        return random.choice(responses)
    
    # Name responses
    elif user_input in ["what's your name", "what is your name", "who are you", "your name"]:
        return "I'm ChatBot, your friendly assistant!"
    
    # Help responses
    elif user_input in ["help", "help me", "what can you do"]:
        return "I can chat with you! Try saying hello, asking how I am, or saying goodbye."
    
    # Thank you responses
    elif user_input in ["thank you", "thanks", "thank you!", "thanks!"]:
        responses = ["You're welcome!", "Happy to help!", "No problem!", "Anytime!"]
        return random.choice(responses)
    
    # Goodbye responses
    elif user_input in ["bye", "goodbye", "see you", "exit", "quit"]:
        responses = ["Goodbye!", "See you later!", "Bye! Have a great day!", 
                     "Take care!", "Until next time!"]
        return random.choice(responses)
    
    # Age responses
    elif user_input in ["how old are you", "what's your age", "your age"]:
        return "I'm timeless! I exist in the digital realm."
    
    # Joke responses
    elif user_input in ["tell me a joke", "joke", "make me laugh"]:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
            "Why did the chatbot go to therapy? It had too many issues to resolve!",
            "What's a chatbot's favorite snack? Computer chips! 🍟"
        ]
        return random.choice(jokes)
    
    # Default response for unrecognized input
    else:
        default_responses = [
            "I'm not sure I understand. Can you rephrase that?",
            "Hmm, I don't know how to respond to that yet.",
            "Interesting! Tell me more.",
            "I'm still learning. Try asking me something else!",
            "Sorry, I didn't quite get that. Try 'help' to see what I can do."
        ]
        return random.choice(default_responses)

def chatbot():
    """
    Main chatbot function that runs the conversation loop
    """
    print("=" * 50)
    print("ChatBot: Hello! I'm a simple chatbot.")
    print("ChatBot: Type 'bye' or 'quit' to exit.")
    print("ChatBot: Type 'help' to see what I can do.")
    print("=" * 50)
    print()
    
    # Main conversation loop
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        # Check if user wants to exit
        if user_input.lower() in ["bye", "goodbye", "exit", "quit"]:
            response = get_response(user_input)
            print(f"ChatBot: {response}")
            break
        
        # Skip empty input
        if not user_input:
            print("ChatBot: Please say something!")
            continue
        
        # Get and display response
        response = get_response(user_input)
        print(f"ChatBot: {response}")
        print()

# Run the chatbot
if __name__ == "__main__":
    chatbot()