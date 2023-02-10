import openai as chat
chat.organization = 'org-1QMU4er8YZ9u4xVIlIIURjFb'
chat.api_key = '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'

model_engine = "text-davinci-003"
prompt1 = "What motivated you to choose a career in IT , Cyber Security and the virtual work space?"

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
