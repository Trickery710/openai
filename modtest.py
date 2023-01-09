import openai
##shouldn't hurt
openai.api_key="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"
while True:
    user_input = input("Enter your code: ")
    completions = openai.Completion.create(
        engine="davinci",
        prompt=user_input,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    completion = completions.choices[0].text
    print(f"Code completion: {completion}")
