import openai

# Initialize OpenAI API
openai.api_key = 'YOUR_API_KEY'

def generate_game_code(prompt):
    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=[
            {"role": "system", "content": "You are a game engine that generates Python game code."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    code = response.choices[0].message['content']
    return code

# Example prompt
prompt = "Create a simple Pygame program where a square moves with arrow keys."

generated_code = generate_game_code(prompt)
print("Generated Code:\n", generated_code)

# Save to a Python file and run
with open('generated_game.py', 'w') as f:
    f.write(generated_code)