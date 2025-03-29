# This code implements a simple command-line chatbot using GPT-2 for text generation.
# It loads the pre-trained GPT-2 model and tokenizer, tokenizes user input, generates a response, and decodes it for display.
# The chatbot runs in a loop, allowing conversation until the user types 'exit', 'quit', or 'bye'.


from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")


def generate_response(prompt):
    """
    Function to generate a response from GPT-2 based on the input prompt.
    """
    # Tokenize the input prompt
    inputs = tokenizer.encode(prompt, return_tensors="pt")

    # Generate the output based on the input
    outputs = model.generate(inputs, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2)

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response


def chat():
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye! Have a great day!")
            break

        response = generate_response(user_input)
        print(f"Chatbot: {response}")


# Run the chatbot only if this script is executed directly
if __name__ == "__main__":
    chat()
