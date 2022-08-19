import os
import openai
import sys


openai.api_key = "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"

translate_input = input("What to Translate: ")

response = openai.Completion.create(
  model="text-davinci-002",
  prompt="Translate this into German:\n\n" + translate_input,
  temperature=0.3,
  max_tokens=3000,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)


file_path = '/Users/anchalbhardwaj/Downloads/gpt3/result.txt'
sys.stdout = open(file_path, "w")
print("English: " + translate_input)
print("Translation: " + response["choices"][0]["text"])
