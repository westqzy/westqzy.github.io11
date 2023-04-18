import openai

openai.api_key="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"

# 使用text-davinci-002或003
model_engine="text-davinci-003"

# 想要询问的话
prompt = "东南大学肖智星是谁"

completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5)

Response = completion.choices[0].text
print(Response)