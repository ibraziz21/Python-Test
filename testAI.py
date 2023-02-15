import openai as chat
chat.organization = ''
chat.api_key = ''

model_engine = "text-davinci-003"
prompt1 = input("Your Question Here: ")

completion = chat.Completion.create(
    engine = model_engine,
    prompt = prompt1, 
    max_tokens=2048,
    n=1,
    stop=None,
    temperature=0.5,
)
response = completion.choices[0].text
print(response)
