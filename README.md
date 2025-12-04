# Chatbot

**Company** - CODETECH IT SOLUTIONS

**Name** - Tanmoy Das

**Intern ID** - CT06DR1738

**Domain** - Python Programming

**Duration** - 6 weeks

**Mentor** - Neela Santosh

This Python script implements a simple yet intelligent chatbot using spaCy, a popular Natural Language Processing (NLP) library. The chatbot is capable of understanding user inputs and responding with contextually appropriate answers based on predefined intents. It demonstrates how Python and NLP techniques can be used to create an interactive and conversational agent.

**Tools and Libraries Used**

* **spaCy** - The primary tool used in this project is spaCy, which is a state-of-the-art NLP library in Python. SpaCy provides pre-trained models, tokenization, part-of-speech tagging, named entity recognition, and importantly for this script, vector-based similarity calculations. The chatbot uses the en_core_web_md model, which is a medium-sized English model containing word vectors. These vectors allow the chatbot to measure the semantic similarity between user input and predefined patterns, rather than relying on exact keyword matches. This makes the chatbot more flexible and human-like in understanding input variations.

* **Random** - The Python random library is used to select a response randomly from a list of possible responses for a given intent. This helps the chatbot appear more natural and less repetitive in conversation.

**How the Chatbot Works**

The chatbot’s functionality is centered around a list of intents. Each intent consists of -

* **Tag** - A label for the type of intent (e.g., "greeting", "goodbye").

* **Patterns** - A list of possible user inputs that the chatbot might encounter for that intent. For example, the "greeting" intent has patterns like "hello", "hi", and "good morning".

* **Responses** - A list of responses that the chatbot can randomly choose from when that intent is detected.

**Processing User Input**

The get_response(user_input) function is the heart of the chatbot’s logic. When a user inputs a message -

The input is converted to lowercase and passed to the spaCy NLP model to create a document object (user_doc) containing the tokenized and vectorized representation of the input.

For each intent, and for each pattern in that intent, the function also creates a spaCy document object. It then calculates the semantic similarity between the user input and the pattern using user_doc.similarity(pattern_doc).

The chatbot keeps track of the highest similarity score and selects the corresponding response for that intent. If no pattern is sufficiently similar, the chatbot defaults to a fallback response: “Sorry, I don't understand that.”

This vector-based similarity approach allows the chatbot to understand variations in user inputs. For example, if the user types "good evening" or "hi there", it can still match the "greeting" intent even if the exact phrase wasn’t in the patterns list.

**Chatbot Interaction**

The chatbot() function handles the actual interaction with the user -

It starts with a greeting message and informs the user that they can type "quit" to exit.

It then enters a loop where it repeatedly takes user input, checks if the user wants to quit, and calls get_response() to generate a reply.

The response is then printed, allowing for a back-and-forth conversation.

**Real-Life Applications**

This simple chatbot can serve as a foundation for many real-world applications -

* **Customer Support** - Businesses can create chatbots to handle frequently asked questions or guide users through their services.

* **Virtual Assistants** The code can be extended to include functionality like reminders, scheduling, or fetching data from APIs.

* **Educational Tools** - Chatbots can help students practice language skills or interact with educational content in a conversational way.

* **Entertainment** - Chatbots can be designed to tell jokes, play games, or engage users in casual conversation.

**Conclusion**

In summary, this Python script demonstrates how spaCy and simple Python logic can be combined to create a conversational AI that is capable of understanding natural language input and responding appropriately. The use of word vectors and similarity measures makes the chatbot more intelligent than simple keyword-matching systems, while the use of random responses adds a human-like variability to the conversation. Although this chatbot is relatively simple, it forms a solid foundation for more advanced AI assistants that can handle complex queries, integrate with APIs, and provide personalized interactions.

**Output** 

<img width="506" height="209" alt="Image" src="https://github.com/user-attachments/assets/fecb881d-d524-40c9-91b5-16b9629f7bbe" />
