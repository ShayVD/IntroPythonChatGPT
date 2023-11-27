import os
import openai
from os import getenv
from dotenv import load_dotenv

load_dotenv()

# pass the api key
openai.api_key = getenv("OPENAI_API_KEY")

# define the prompt
messages = []
messages.append({"role": "system", "content": "you are a CTO mentoring developers, dont only provide answers also ask guiding questions"})
messages.append({"role": "user", "content": "why is my website down?"})

try:
  # make an api call
  response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=0,
    n=1,
    max_tokens=20
  )

  # print the response
  print(response.choices[0].message.content)

# authentication issue
except openai.AuthenticationError as e:
  print("No Valid Token/Authentication Error: %s" % e.message)

# invalid request issue
except openai.BadRequestError as e:
  print("Bad Request Error: %s" % e.message)
