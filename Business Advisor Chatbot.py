from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a ChatBot instance
chatbot = ChatBot('BusinessAdvisor')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)


trainer.train('chatterbot.corpus.english')

# Add custom training data
custom_training_data = [
    "Tell me about business planning",
    "Business planning involves creating a roadmap for your business's future, outlining goals, strategies, and potential challenges.",
    "How can I improve my sales?",
    "To improve sales, focus on understanding your target audience, enhancing your product or service, and implementing effective marketing strategies.",
    "What are some marketing tips?",
    "Some marketing tips include identifying your target market, utilizing social media, creating engaging content, and tracking the performance of your campaigns.",
    "How do I create a business budget?",
    "Creating a business budget involves listing all expenses, estimating revenues, and regularly monitoring actual performance against projected figures.",
    "Thank you",
    "You're welcome! If you have more questions, feel free to ask."
]

trainer.train(custom_training_data)

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Business Advisor: Goodbye! If you need more advice, come back anytime.")
        break
    response = chatbot.get_response(user_input)
    print("Business Advisor", response)
