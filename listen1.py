import openai

# Set the API key for the GPT-3 API
openai.api_key = "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"

def generate_response(input_text):
    # Use the GPT-3 API to generate a response based on the input text
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=input_text,
        temperature=0.7
    )

    # Return the response text
    return response.choices[0].text

# Continuously listen for voice input and generate responses
while True:
    input_text = input("Speak: ")
    response_text = generate_response(input_text)
    print("Response: ", response_text)

