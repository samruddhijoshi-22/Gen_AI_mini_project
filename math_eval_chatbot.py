# This code creates a chatbot GUI using Tkinter, integrating GPT-2 for text generation and evaluating basic math expressions.
# User inputs are displayed in the chat window, and the chatbot responds based on either math evaluation or GPT-2-generated text.
# The GUI includes a styled chat window, input field, and "Send" button for user interaction.


import tkinter as tk
import re
from tkinter import scrolledtext
from transformers import pipeline

# Load a text-generation AI model (like GPT-2 or DialoGPT-small)
generator = pipeline("text-generation", model="gpt2")  # Fixed task name to "text-generation"


def eval_math_expression(user_input):
    try:
        # Extract and evaluate mathematical expressions using regex
        expression = re.findall(r'[\d\+\-\*\/\(\)\.\s]+', user_input)
        if expression:
            math_exp = "".join(expression).strip()
            return str(eval(math_exp))  # Evaluate safely
    except Exception:
        return None  # Return None if evaluation fails


def chatbot_response(user_input):
    # Handle math expressions first
    math_result = eval_math_expression(user_input)
    if math_result:  # Return answer if it's a valid math expression
        return f"The answer is: {math_result}"

    # Generate conversational response
    response = generator(user_input, max_length=100, num_return_sequences=1, temperature=0.6, top_p=0.9)
    return response[0]['generated_text'].strip()


def send_message():
    user_input = entry.get()
    if user_input.strip():
        chat_window.insert(tk.END, "You: " + user_input + "\n", "user")
        entry.delete(0, tk.END)

        bot_response = chatbot_response(user_input)
        chat_window.insert(tk.END, "Sam's ChatBot: " + bot_response + "\n", "bot")

        chat_window.yview(tk.END)


# Create GUI window with styling
root = tk.Tk()
root.title("Sam's ChatBot")
root.geometry("500x600")
root.configure(bg="#2C2C2C")

chat_window = scrolledtext.ScrolledText(
    root, wrap=tk.WORD, width=60, height=20, font=("Arial", 12),
    bg="#1E1E1E", fg="#D4D4D4", borderwidth=2, relief="groove"
)
chat_window.pack(pady=10, padx=10)
chat_window.tag_configure("user", foreground="#1E90FF", font=("Arial", 12, "bold"))
chat_window.tag_configure("bot", foreground="#32CD32", font=("Arial", 12))

entry_frame = tk.Frame(root, bg="#2C2C2C")
entry_frame.pack(pady=5)
entry = tk.Entry(entry_frame, width=40, font=("Arial", 14), bg="#3C3C3C", fg="#D4D4D4", relief="ridge", bd=3)
entry.grid(row=0, column=0, padx=5, pady=5)

send_button = tk.Button(entry_frame, text="Send", command=send_message, font=("Arial", 12),
                        bg="#007ACC", fg="white", activebackground="#005A9E", width=8)
send_button.grid(row=0, column=1, padx=5)

root.mainloop()
