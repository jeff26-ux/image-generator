import openai

# Set your OpenAI API key
openai.api_key = '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'

# Make a request without specifying the model
response = openai.Completion.create(
  engine="text-davinci-003",  # Specify the engine if needed
  prompt="Kucing"
)

# Access the generated text
generated_text = response['choices'][0]['text']
print(generated_text)
