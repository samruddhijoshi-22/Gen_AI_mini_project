from transformers import pipeline
#Load gpt-2 for text generation
generator =pipeline("text-generation",model="gpt2")

prompt ="Artificial Intelligence is creating new career opportunities in fields like"

#generate text
output =generator(prompt,max_length=200,num_return_sequences=1) 

print("Generated Content:\n",output[0]['generated_text'])

# This code uses Hugging Face's GPT-2 text-generation pipeline to generate text based on a given prompt.
# It outputs a continuation of the prompt with a specified maximum length and number of sequences.
