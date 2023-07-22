
import re

def code_clause_chatbot(user_input):
    
    patterns = {
        r'.*\bhello\b.*': 'Hello! How can I help you with Code Clause?',
        r'.*\bhi\b.*': 'Hi! What can I assist you with today?',
        r'.*\b(what|how).*\bcode clause\b.*': 'Code Clause is a platform that provides programming tutorials and resources.',
        r'.*\bpython\b.*': 'Python is a popular programming language used for various applications.',
        r'.*\bjavascript\b.*': 'JavaScript is a widely-used programming language for web development.',
        r'.*\bresources\b.*': 'You can find various programming resources on Code Clause, including tutorials, articles, and code samples.',
        r'.*\bthank you\b.*': 'You\'re welcome! If you have any more questions, feel free to ask.',
        r'.*\bbye\b.*': 'Goodbye! Have a great day!',
        r'.*': "I'm sorry, I don't understand. Can you please rephrase your question?",
    }

    # Check for matches in user input and return the corresponding response
    for pattern, response in patterns.items():
        if re.match(pattern, user_input.lower()):
            return response

    return "I'm sorry, I'm not sure how to help with that. Please ask another question."

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Chatbot: Goodbye! Have a nice day!")
        break
    response = code_clause_chatbot(user_input)
    print("Chatbot:", response)
