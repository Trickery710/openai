import openai

def get_answer(prompt):
  model_engine = "text-davinci-002"
  prompt = (f"{prompt}"
           )

  completions = openai.Completion.create(
      engine=model_engine,
      prompt=prompt,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.5,
  )

  message = completions.choices[0].text
  return message

answers = []

while True:
  question = input("Ask a question: ")
  if question == "exit":
    break
  answer = get_answer(question)
  answers.append(answer)
  print(answer)

print(answers)
