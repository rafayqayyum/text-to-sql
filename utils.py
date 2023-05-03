import openai
import os

max_words=500
max_response=700
openai.api_key =os.environ['OPENAI_API_KEY']
#function to generate summary
def generate_sql(prompt,dbtype='mysql'):
  tokens_discarded=0
  try:
    message=[{"role":"system",'content':"You are given a schema and a natural language query. You convert the natural language query to SQL query for "+dbtype+" database."},
             {"role":"user",'content':prompt}]
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=message,
      temperature=0.90,
      max_tokens=max_response,
      top_p=1.0,
      frequency_penalty=0.1,
      presence_penalty=0.1)
    query=response.choices[0]['message']['content'].strip()
    # clean
    query=query.replace('\n',' ')
    query=query.replace('\t',' ')
    query=query.replace('  ',' ')
    return True,query,tokens_discarded
  # check for openai api key error
  except openai.error.AuthenticationError as e:
    return False,'Invalid OpenAI API Key',0
  # check for access error
  except openai.error.PermissionError as e:
    return False,'Your OpenAI API Key does not have access to this model',0
  # check for rate limit error
  except openai.error.RateLimitError as e:
    return False,'OpenAI API Key Rate Limit Reached',0
  except Exception as e:
    return False,None,0