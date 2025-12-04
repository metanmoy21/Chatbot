import spacy
import random

nlp = spacy.load("en_core_web_md")

intents = [
    {
        "tag": "greeting",
        "patterns": ["hello", "hi", "hey", "good morning", "good evening"],
        "responses": ["Hello!", "Hi there!", "Hey! How can I help you today?"]
    },
    {
        "tag": "goodbye",
        "patterns": ["bye", "see you", "goodbye", "exit", "quit"],
        "responses": ["Goodbye!", "See you later!", "Bye! Have a nice day!"]
    },
    {
        "tag": "thanks",
        "patterns": ["thanks", "thank you", "thank"],
        "responses": ["You're welcome!", "Happy to help!", "No problem!"]
    },
    {
        "tag": "about",
        "patterns": ["who are you", "what can you do", "your name", "about you"],
        "responses": ["I am a smart chatbot created using Python and spaCy!", 
                      "I can answer your questions and chat with you."]
    },
    {
        "tag": "weather",
        "patterns": ["weather", "temperature", "rain", "forecast"],
        "responses": ["I cannot fetch live weather yet, but you can check online!"]
    },
    {
        "tag": "age",
        "patterns": ["how old are you", "your age"],
        "responses": ["I am timeless!", "I don’t have an age."]
    }
]

def get_response(user_input):
    user_doc = nlp(user_input.lower())
    max_similarity = 0
    best_response = "Sorry, I don't understand that."

    for intent in intents:
        for pattern in intent["patterns"]:
            pattern_doc = nlp(pattern.lower())
            similarity = user_doc.similarity(pattern_doc)
            if similarity > max_similarity:
                max_similarity = similarity
                best_response = random.choice(intent["responses"])

    return best_response

def chatbot():
    print("🤖 Chatbot: Hello! Type 'quit' to exit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            print("🤖 Chatbot: Goodbye! Have a nice day!")
            break

        reply = get_response(user_input)
        print("🤖 Chatbot:", reply)

if __name__ == "__main__":
    chatbot()
