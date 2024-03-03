---
layout: post
title: LangChain for LLM Application Development
date: 2024-03-02 19:20 +0900
categories:
  - Deep-Learning
  - LangChain
tags: 
math: true
---
# LangChain for LLM Application Development

https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/

## Components

Models
- LLMs: 20+ integrations
- Chat Models
- Text Embedding Models: 10+ integrations

Prompts
- Prompt Templates
- Output Parsers: 5+ implementations
- Retry/fixing logic
- Example Selectors: 5+ implementations

Indexes
- Document Loaders: 50+ implementations
- Text Splitters: 10+ implementations
- Vector stores: 10+ integrations
- Retrievers: 5+ integrations/implementations

Chains
- Prompt + LLM + Output parsing
- Can be used as building blocks for longer chains
- More application specific chains: 20+ types

Agents
- Agent Types: 5+ types
- Algorithms for getting LLMs to use tools
- Agent Toolkits: 10+ implementations
- Agents armed with specific tools for a specific application


## Langchain: Models, Prompts, and Output Parsers

Why use prompt templates?
- allow reuse good long detailed prompts 
- Langchain provides prompts for common operations
- supports output parsing

![](https://i.imgur.com/zLpG9x4.png)


### Code
#### Chat API : OpenAI


Let's start with a direct API calls to OpenAI.


```python

def get_completion(prompt, model=llm_model):

	messages = [{"role": "user", "content": prompt}]

	response = openai.ChatCompletion.create(

		model=model,

		messages=messages,

		temperature=0,

	)

	return response.choices[0].message["content"]

```

  
  

```python
get_completion("What is 1+1?")
```

  

	'As an AI language model, I can tell you that the answer to 1+1 is 2.'

  
  
  
  

```python

customer_email = """

Arrr, I be fuming that me blender lid \

flew off and splattered me kitchen walls \

with smoothie! And to make matters worse,\

the warranty don't cover the cost of \

cleaning up me kitchen. I need yer help \

right now, matey!

"""

```

  

#### Chat API : OpenAI

  

Let's start with a direct API calls to OpenAI.

  
  

```python

def get_completion(prompt, model=llm_model):

messages = [{"role": "user", "content": prompt}]

response = openai.ChatCompletion.create(

model=model,

messages=messages,

temperature=0,

)

return response.choices[0].message["content"]

  

```

  
  

```python

get_completion("What is 1+1?")

```

  
  
  
  

	'As an AI language model, I can tell you that the answer to 1+1 is 2.'

  
  
  
  

```python

customer_email = """

Arrr, I be fuming that me blender lid \

flew off and splattered me kitchen walls \

with smoothie! And to make matters worse,\

the warranty don't cover the cost of \

cleaning up me kitchen. I need yer help \

right now, matey!

"""

```

  
  

```python

## Chat API : OpenAI

  

Let's start with a direct API calls to OpenAI.

  

def get_completion(prompt, model=llm_model):

	messages = [{"role": "user", "content": prompt}]

	response = openai.ChatCompletion.create(

		model=model,

		messages=messages,

		temperature=0,

	)

	return response.choices[0].message["content"]

  
  

get_completion("What is 1+1?")

  

customer_email = """

Arrr, I be fuming that me blender lid \

flew off and splattered me kitchen walls \

with smoothie! And to make matters worse,\

the warranty don't cover the cost of \

cleaning up me kitchen. I need yer help \

right now, matey!

"""

```

#### Output Parsers

  

Let's start with defining how we would like the LLM output to look like:

  
  

```python

{

"gift": False,

"delivery_days": 5,

"price_value": "pretty affordable!"

}

```

```python

customer_review = """\

This leaf blower is pretty amazing. It has four settings:\

candle blower, gentle breeze, windy city, and tornado. \

It arrived in two days, just in time for my wife's \

anniversary present. \

I think my wife liked it so much she was speechless. \

So far I've been the only one using it, and I've been \

using it every other morning to clear the leaves on our lawn. \

It's slightly more expensive than the other leaf blowers \

out there, but I think it's worth it for the extra features.

"""

  

review_template = """\

For the following text, extract the following information:

  

gift: Was the item purchased as a gift for someone else? \

Answer True if yes, False if not or unknown.

  

delivery_days: How many days did it take for the product \

to arrive? If this information is not found, output -1.

  

price_value: Extract any sentences about the value or price,\

and output them as a comma separated Python list.

  

Format the output as JSON with the following keys:

gift

delivery_days

price_value

  

text: {text}

"""

```

  
  

```python

from langchain.prompts import ChatPromptTemplate

  

prompt_template = ChatPromptTemplate.from_template(review_template)

print(prompt_template)

```

  

	input_variables=['text'] output_parser=None partial_variables={} messages=[HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['text'], output_parser=None, partial_variables={}, template='For the following text, extract the following information:\n\ngift: Was the item purchased as a gift for someone else? Answer True if yes, False if not or unknown.\n\ndelivery_days: How many days did it take for the product to arrive? If this information is not found, output -1.\n\nprice_value: Extract any sentences about the value or price,and output them as a comma separated Python list.\n\nFormat the output as JSON with the following keys:\ngift\ndelivery_days\nprice_value\n\ntext: {text}\n', template_format='f-string', validate_template=True), additional_kwargs={})]

  
  
  

```python

messages = prompt_template.format_messages(text=customer_review)

chat = ChatOpenAI(temperature=0.0, model=llm_model)

response = chat(messages)

print(response.content)

```

  

	{
	
	"gift": true,
	
	"delivery_days": 2,
	
	"price_value": ["It's slightly more expensive than the other leaf blowers out there, but I think it's worth it for the extra features."]
	
	}

  
  
  

```python

type(response.content)

```

  
  
  
  

	str

  
  
  
  

```python

# You will get an error by running this line of code

# because'gift' is not a dictionary

# 'gift' is a string

response.content.get('gift')

```

  
  

---------------------------------------------------------------------------

  

	AttributeError Traceback (most recent call last)
	
	  
	
	Cell In[35], line 4
	
	1 # You will get an error by running this line of code
	
	2 # because'gift' is not a dictionary
	
	3 # 'gift' is a string
	
	----> 4 response.content.get('gift')
	
	  
	  
	
	AttributeError: 'str' object has no attribute 'get'

  
  

##### Parse the LLM output string into a Python dictionary

  
  

```python

from langchain.output_parsers import ResponseSchema

from langchain.output_parsers import StructuredOutputParser

```

  
  

```python

gift_schema = ResponseSchema(name="gift",

description="Was the item purchased\

as a gift for someone else? \

Answer True if yes,\

False if not or unknown.")

delivery_days_schema = ResponseSchema(name="delivery_days",

description="How many days\

did it take for the product\

to arrive? If this \

information is not found,\

output -1.")

price_value_schema = ResponseSchema(name="price_value",

description="Extract any\

sentences about the value or \

price, and output them as a \

comma separated Python list.")

  

response_schemas = [gift_schema,

delivery_days_schema,

price_value_schema]

```

  
  

```python

output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

```

  
  

```python

format_instructions = output_parser.get_format_instructions()

```

  
  

```python

print(format_instructions)

```

  

The output should be a markdown code snippet formatted in the following schema, including the leading and trailing "\`\`\`json" and "\`\`\`":

```json

{

"gift": string // Was the item purchased as a gift for someone else? Answer True if yes, False if not or unknown.

"delivery_days": string // How many days did it take for the product to arrive? If this information is not found, output -1.

"price_value": string // Extract any sentences about the value or price, and output them as a comma separated Python list.

}

```

  
  
  

```python

review_template_2 = """\

For the following text, extract the following information:

  

gift: Was the item purchased as a gift for someone else? \

Answer True if yes, False if not or unknown.

  

delivery_days: How many days did it take for the product\

to arrive? If this information is not found, output -1.

  

price_value: Extract any sentences about the value or price,\

and output them as a comma separated Python list.

  

text: {text}

  

{format_instructions}

"""

  

prompt = ChatPromptTemplate.from_template(template=review_template_2)

  

messages = prompt.format_messages(text=customer_review,

format_instructions=format_instructions)

```

  

```python

print(messages[0].content)

```

  

	For the following text, extract the following information:
	
	gift: Was the item purchased as a gift for someone else? Answer True if yes, False if not or unknown.
	
	delivery_days: How many days did it take for the productto arrive? If this information is not found, output -1.
	
	price_value: Extract any sentences about the value or price,and output them as a comma separated Python list.
	
	text: This leaf blower is pretty amazing. It has four settings:candle blower, gentle breeze, windy city, and tornado. It arrived in two days, just in time for my wife's anniversary present. I think my wife liked it so much she was speechless. So far I've been the only one using it, and I've been using it every other morning to clear the leaves on our lawn. It's slightly more expensive than the other leaf blowers out there, but I think it's worth it for the extra features.
	
	The output should be a markdown code snippet formatted in the following schema, including the leading and trailing "\`\`\`json" and "\`\`\`":

```json

{

"gift": string // Was the item purchased as a gift for someone else? Answer True if yes, False if not or unknown.

"delivery_days": string // How many days did it take for the product to arrive? If this information is not found, output -1.

"price_value": string // Extract any sentences about the value or price, and output them as a comma separated Python list.

}

```

  
  
  

```python

response = chat(messages)

```

  
  

```python

print(response.content)

```

  

```json

{

"gift": true,

"delivery_days": "2",

"price_value": ["It's slightly more expensive than the other leaf blowers out there, but I think it's worth it for the extra features."]

}

```

  
  
  

```python

output_dict = output_parser.parse(response.content)

```

  
  

```python

output_dict

```

  
  
  
  

	{'gift': True,
	
	'delivery_days': '2',
	
	'price_value': ["It's slightly more expensive than the other leaf blowers out there, but I think it's worth it for the extra features."]}

  
  
  
  

```python

type(output_dict)

```

  

	dict


```python

output_dict.get('delivery_days')

```


	'2'





## Memory

Large Language Models are 'stateless'
- Each transaction is independent

Chatbots appear to have memory by providing the full conversation as 'context'

>#### Large Language Models (LLMs)와 Stateless의 의미
>
>- **독립적 요청 처리**: LLMs의 stateless 특성은 각 요청을 이전의 상호작용과 독립적으로 처리한다는 것을 의미
>- **맥락 부재**: 모델은 주어진 입력만을 기반으로 응답을 생성하며, 이전 요청의 맥락은 고려하지 않음
>- **세션 상태 유지 부재**: LLMs는 사용자 세션 정보나 이전 상호작용을 기억하지 않음
>
>##### Stateless 모델의 장점
>
>- **단순성과 확장성**: 요청 간 상태 정보 공유가 필요 없어 시스템 설계가 단순하고 확장이 용이
>- **무상태성**: 상태 정보의 저장과 관리를 최소화해 시스템의 신뢰성과 가용성 향상
>
>##### Stateless 모델의 단점
>
>- **맥락 제한**: 이전 맥락을 고려하지 않아 긴 대화나 복잡한 상호작용 처리에 제한이 있을 수 있음
>- **상태 유지 필요성**: 특정 애플리케이션에서 사용자 맥락이 중요할 경우, 외부 시스템을 통한 상태 정보 관리가 필요
>
>LLMs의 stateless 특성은 강력한 언어 처리 능력을 제공하지만, 복잡한 상호작용을 처리하기 위해서는 상태 정보의 관>리가 필요할 수 있음


LangChain provides several kinds of 'memory' to store and accumulate the conversation

```python
from langchain.char_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

llm = ChatOpenAI(temperature=0.0)
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm,
								 memory=memory,
								 verbose=False
)

```

## Outline[](https://s172-31-10-142p57746.lab-aws-production.deeplearning.ai/notebooks/L2-Memory.ipynb#Outline)

- ConversationBufferMemory
- ConversationBufferWindowMemory
- ConversationTokenBufferMemory
- ConversationSummaryMemory
### Code


  

#### ConversationBufferMemory

  
  

```python

import os

  

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv()) # read local .env file

  

import warnings

warnings.filterwarnings('ignore')

```

  

Note: LLM's do not always produce the same results. When executing the code in your notebook, you may get slightly different answers that those in the video.

  
  

```python

# account for deprecation of LLM model

import datetime

# Get the current date

current_date = datetime.datetime.now().date()

  

# Define the date after which the model should be set to "gpt-3.5-turbo"

target_date = datetime.date(2024, 6, 12)

  

# Set the model variable based on the current date

if current_date > target_date:

llm_model = "gpt-3.5-turbo"

else:

llm_model = "gpt-3.5-turbo-0301"

```

  
  

```python

from langchain.chat_models import ChatOpenAI

from langchain.chains import ConversationChain

from langchain.memory import ConversationBufferMemory

  

```

  
  

```python

llm = ChatOpenAI(temperature=0.0, model=llm_model)

memory = ConversationBufferMemory()

conversation = ConversationChain(

llm=llm,

memory = memory,

verbose=True

)

```

  
  

```python
conversation.predict(input="Hi, my name is Andrew")
```

  

	[1m> Entering new ConversationChain chain...[0m
	
	Prompt after formatting:
	
	[32;1m[1;3mThe following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.
	
	Current conversation:
	
	Human: Hi, my name is Andrew
	
	AI:[0m
	
	[1m> Finished chain.[0m

  

	"Hello Andrew, it's nice to meet you. My name is AI. How can I assist you today?"

  
  
  
  

```python
conversation.predict(input="What is 1+1?")
```

  
	
	[1m> Entering new ConversationChain chain...[0m
	
	Prompt after formatting:
	
	[32;1m[1;3mThe following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.
	
	Current conversation:
	
	Human: Hi, my name is Andrew
	
	AI: Hello Andrew, it's nice to meet you. My name is AI. How can I assist you today?
	
	Human: What is 1+1?
	
	AI:[0m
	
	[1m> Finished chain.[0m
	
	  
	  
	  
	  
	  
	
	'The answer to 1+1 is 2.'

  
  
  
  

```python
conversation.predict(input="What is my name?")
```

  
	
	[1m> Entering new ConversationChain chain...[0m
	
	Prompt after formatting:
	
	[32;1m[1;3mThe following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.
	
	Current conversation:
	
	Human: Hi, my name is Andrew
	
	AI: Hello Andrew, it's nice to meet you. My name is AI. How can I assist you today?
	
	Human: What is 1+1?
	
	AI: The answer to 1+1 is 2.
	
	Human: What is my name?
	
	AI:[0m
	
	[1m> Finished chain.[0m
	
	  
	  
	  
	  
	  
	
	'Your name is Andrew, as you mentioned earlier.'

  
  
  
  

```python
print(memory.buffer)
```

  

	Human: Hi, my name is Andrew
	
	AI: Hello Andrew, it's nice to meet you. My name is AI. How can I assist you today?
	
	Human: What is 1+1?
	
	AI: The answer to 1+1 is 2.
	
	Human: What is my name?
	
	AI: Your name is Andrew, as you mentioned earlier.

  
  
  

```python
memory.load_memory_variables({})
```

  
  
  
  

	{'history': "Human: Hi, my name is Andrew\nAI: Hello Andrew, it's nice to meet you. My name is AI. How can I assist you today?\nHuman: What is 1+1?\nAI: The answer to 1+1 is 2.\nHuman: What is my name?\nAI: Your name is Andrew, as you mentioned earlier."}

  
  
  
  

```python
memory = ConversationBufferMemory()
```

  
  

```python
memory.save_context({"input": "Hi"},
{"output": "What's up"})
```

  
  

```python
print(memory.buffer)
```

  
	
	Human: Hi
	
	AI: What's up

  
  
  

```python
memory.load_memory_variables({})
```

  
  
  
  

	{'history': "Human: Hi\nAI: What's up"}

  
  
  
  

```python
memory.save_context({"input": "Not much, just hanging"},
{"output": "Cool"})
```

  
  

```python
memory.load_memory_variables({})
```

  
  
  
  

	{'history': "Human: Hi\nAI: What's up\nHuman: Not much, just hanging\nAI: Cool"}

  
  
  

#### ConversationBufferWindowMemory

  
  

```python
from langchain.memory import ConversationBufferWindowMemory
```

  
  

```python
memory = ConversationBufferWindowMemory(k=1)
```

  
  

```python
memory.save_context({"input": "Hi"},

{"output": "What's up"})

memory.save_context({"input": "Not much, just hanging"},

{"output": "Cool"})
```

  
  

```python
memory.load_memory_variables({})
```

  
  
  
  

	{'history': 'Human: Not much, just hanging\nAI: Cool'}

  
  
  
  

```python
llm = ChatOpenAI(temperature=0.0, model=llm_model)

memory = ConversationBufferWindowMemory(k=1)

conversation = ConversationChain(

llm=llm,

memory = memory,

verbose=False

)
```

  
  

```python
conversation.predict(input="Hi, my name is Andrew")
```

  
  
  
  

	"Hello Andrew, it's nice to meet you. My name is AI. How can I assist you today?"

  
  
  
  

```python
conversation.predict(input="What is 1+1?")
```

  
  
  
  

	'The answer to 1+1 is 2.'

  
  
  
  

```python
conversation.predict(input="What is my name?")
```

  
  
  
  

	"I'm sorry, I don't have access to that information. Could you please tell me your name?"

  
  
  

#### ConversationTokenBufferMemory

  
  

```python

#!pip install tiktoken

```

```python
from langchain.memory import ConversationTokenBufferMemory

from langchain.llms import OpenAI

llm = ChatOpenAI(temperature=0.0, model=llm_model)
```

```python
memory = ConversationTokenBufferMemory(llm=llm, max_token_limit=50)

memory.save_context({"input": "AI is what?!"},

{"output": "Amazing!"})

memory.save_context({"input": "Backpropagation is what?"},

{"output": "Beautiful!"})

memory.save_context({"input": "Chatbots are what?"},

{"output": "Charming!"})

```


```python
memory.load_memory_variables({})
```

	{'history': 'AI: Amazing!\nHuman: Backpropagation is what?\nAI: Beautiful!\nHuman: Chatbots are what?\nAI: Charming!'}

#### ConversationSummaryMemory

```python
from langchain.memory import ConversationSummaryBufferMemory
```

```python
# create a long string

schedule = "There is a meeting at 8am with your product team. \

You will need your powerpoint presentation prepared. \

9am-12pm have time to work on your LangChain \

project which will go quickly because Langchain is such a powerful tool. \

At Noon, lunch at the italian resturant with a customer who is driving \

from over an hour away to meet you to understand the latest in AI. \

Be sure to bring your laptop to show the latest LLM demo."

  

memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=100)

memory.save_context({"input": "Hello"}, {"output": "What's up"})

memory.save_context({"input": "Not much, just hanging"},

{"output": "Cool"})

memory.save_context({"input": "What is on the schedule today?"},

{"output": f"{schedule}"})
```


```python
memory.load_memory_variables({})
```

	{'history': "System: The human and AI engage in small talk before discussing the day's schedule. The AI informs the human of a morning meeting with the product team, time to work on the LangChain project, and a lunch meeting with a customer interested in the latest AI developments."}

```python
conversation = ConversationChain(

llm=llm,

memory = memory,

verbose=True

)
```

```python
conversation.predict(input="What would be a good demo to show?")
```

  

	[1m> Entering new ConversationChain chain...[0m
	
	Prompt after formatting:
	
	[32;1m[1;3mThe following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.
	
	Current conversation:
	
	System: The human and AI engage in small talk before discussing the day's schedule. The AI informs the human of a morning meeting with the product team, time to work on the LangChain project, and a lunch meeting with a customer interested in the latest AI developments.
	
	Human: What would be a good demo to show?
	
	AI:[0m
	
	[1m> Finished chain.[0m
	
	  
	  
	  
	  
	  
	
	"Based on the customer's interest in AI developments, I would suggest showcasing our latest natural language processing capabilities. We could demonstrate how our AI can accurately understand and respond to complex language queries, and even provide personalized recommendations based on the user's preferences. Additionally, we could highlight our AI's ability to learn and adapt over time, making it a valuable tool for businesses looking to improve their customer experience."

  
  
  
  

```python
memory.load_memory_variables({})
```
	
	{'history': "System: The human and AI engage in small talk before discussing the day's schedule. The AI informs the human of a morning meeting with the product team, time to work on the LangChain project, and a lunch meeting with a customer interested in the latest AI developments. The human asks what would be a good demo to show.\nAI: Based on the customer's interest in AI developments, I would suggest showcasing our latest natural language processing capabilities. We could demonstrate how our AI can accurately understand and respond to complex language queries, and even provide personalized recommendations based on the user's preferences. Additionally, we could highlight our AI's ability to learn and adapt over time, making it a valuable tool for businesses looking to improve their customer experience."}
