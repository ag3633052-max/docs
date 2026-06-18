import openai

# Set your API key here
openai.api_key = 'YOUR_API_KEY'  # Replace with your actual API key

response = openai.ChatCompletion.create(
    model='gpt-4',  # or 'gpt-3.5-turbo'
    messages=[
        {"role": "system", "content": "You are a helpful assistant for generating Python game code."},
        {"role": "user", "content": "Create a simple Pygame program where a square moves with arrow keys."}
    ],
    max_tokens=500
)

generated_code = response.choices[0].message['content']
print("Generated code:\n")
print(generated_code)