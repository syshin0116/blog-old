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

### Outline[](https://s172-31-10-142p57746.lab-aws-production.deeplearning.ai/notebooks/L2-Memory.ipynb#Outline)

#### Memory

- ConversationBufferMemory
	- This memory allows for storing of messages and then extracts the messages in a variable.
- ConversationBufferWindowMemory
	- This memory keeps a list of the interactions of the conversation over time. It only uses the last K interactions.
- ConversationTokenBufferMemory
	- This memory keeps a buffer of recent interactions in memory, and uses token length rather than number of interactions to determine when to flush interactions.
- ConversationSummaryMemory
	- This memory creates a summary of the conversation over time.

#### Additional Memory Types
- Vector data memory
	- Stores text (from conversation or elsewhere) in a vector database and retrieves the most relevant blocks of text.
- Entity memories
	- Using an LLM, it remembers details about specific entities.

You can also use multiple memories at one time.

E.g., Conversation memory + Entity memory to recall individuals.

You can also store the conversation in a conventional database (such as key-value store or SQL)
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


## Chains

### Sequential Chains
Sequential chain is another type of chains. The idea is to combine multiple chains where the
output of the one chain is the input of the next chain.

There is two type of sequential chains:
1. SimpleSequentialChain: Single input/output
2. SequentialChain: multiple inputs/outputs

![](https://i.imgur.com/v2JRuE4.png)



```python
from langchain.chains import SimpleSequentialChain

llm = ChatOpenAI(temperature=0.9, model=llm_model)

# prompt template 1
first_prompt = ChatPromptTemplate.from_template(
    "What is the best name to describe \
    a company that makes {product}?"
)

# Chain 1
chain_one = LLMChain(llm=llm, prompt=first_prompt)

# prompt template 2
second_prompt = ChatPromptTemplate.from_template(
    "Write a 20 words description for the following \
    company:{company_name}"
)
# chain 2
chain_two = LLMChain(llm=llm, prompt=second_prompt)

overall_simple_chain = SimpleSequentialChain(chains=[chain_one, chain_two],
                                             verbose=True
                                            )

print(overall_simple_chain.run(product))
```

> 	Entering new SimpleSequentialChain chain...
	Queenly Linens.
	Queenly Linens is a high-quality linen supplier that offers elegant and sophisticated linens for an exquisite dining experience.
	
> 	Finished chain.
	
>	'Queenly Linens is a high-quality linen supplier that offers elegant and sophisticated linens for an exquisite dining experience.'



### SequentialChain


![](https://i.imgur.com/8birWTW.png)

```python
from langchain.chains import SequentialChain

llm = ChatOpenAI(temperature=0.9, model=llm_model)

# prompt template 1: translate to english
first_prompt = ChatPromptTemplate.from_template(
    "Translate the following review to english:"
    "\n\n{Review}"
)
# chain 1: input= Review and output= English_Review
chain_one = LLMChain(llm=llm, prompt=first_prompt, 
                     output_key="English_Review"
                    )


second_prompt = ChatPromptTemplate.from_template(
    "Can you summarize the following review in 1 sentence:"
    "\n\n{English_Review}"
)
# chain 2: input= English_Review and output= summary
chain_two = LLMChain(llm=llm, prompt=second_prompt, 
                     output_key="summary"
                    )


# prompt template 3: translate to english
third_prompt = ChatPromptTemplate.from_template(
    "What language is the following review:\n\n{Review}"
)
# chain 3: input= Review and output= language
chain_three = LLMChain(llm=llm, prompt=third_prompt,
                       output_key="language"
                      )



# prompt template 4: follow up message
fourth_prompt = ChatPromptTemplate.from_template(
    "Write a follow up response to the following "
    "summary in the specified language:"
    "\n\nSummary: {summary}\n\nLanguage: {language}"
)
# chain 4: input= summary, language and output= followup_message
chain_four = LLMChain(llm=llm, prompt=fourth_prompt,
                      output_key="followup_message"
                     )


# overall_chain: input= Review 
# and output= English_Review,summary, followup_message
overall_chain = SequentialChain(
    chains=[chain_one, chain_two, chain_three, chain_four],
    input_variables=["Review"],
    output_variables=["English_Review", "summary","followup_message"],
    verbose=True
)

review = df.Review[5]
print(overall_chain(review))
```


> 	Entering new SequentialChain chain...
	
> 	Finished chain.
	
> 	{'Review': "Je trouve le goût médiocre. La mousse ne tient pas, c'est bizarre. J'achète les mêmes dans le commerce et le goût est bien meilleur...\nVieux lot ou contrefaçon !?",
	 'English_Review': "I find the taste mediocre. The foam doesn't hold, it's weird. I buy the same ones in stores and the taste is much better... Old batch or counterfeit!?",
	 'summary': 'The reviewer finds the taste of the product mediocre and suspects that they received an old batch or counterfeit product as the foam does not hold up.',
	 'followup_message': "Réponse de suivi: Nous sommes désolés d'apprendre que vous n'avez pas apprécié le goût de notre produit et que vous pensez avoir reçu un lot périmé ou contrefait. Nous prenons très au sérieux la qualité de nos produits et nous vous assurons que nous enquêterons sur ce problème. Si vous pouviez nous indiquer le numéro de lot ou d'autres détails, cela nous aiderait à résoudre le problème. Nous espérons avoir l'occasion de regagner votre confiance dans notre marque à l'avenir. Merci de nous avoir informés de votre expérience."}



### Router Chain


![](https://i.imgur.com/NnvjkHd.png)

```python
physics_template = """You are a very smart physics professor. \
You are great at answering questions about physics in a concise\
and easy to understand manner. \
When you don't know the answer to a question you admit\
that you don't know.

Here is a question:
{input}"""


math_template = """You are a very good mathematician. \
You are great at answering math questions. \
You are so good because you are able to break down \
hard problems into their component parts, 
answer the component parts, and then put them together\
to answer the broader question.

Here is a question:
{input}"""

history_template = """You are a very good historian. \
You have an excellent knowledge of and understanding of people,\
events and contexts from a range of historical periods. \
You have the ability to think, reflect, debate, discuss and \
evaluate the past. You have a respect for historical evidence\
and the ability to make use of it to support your explanations \
and judgements.

Here is a question:
{input}"""


computerscience_template = """ You are a successful computer scientist.\
You have a passion for creativity, collaboration,\
forward-thinking, confidence, strong problem-solving capabilities,\
understanding of theories and algorithms, and excellent communication \
skills. You are great at answering coding questions. \
You are so good because you know how to solve a problem by \
describing the solution in imperative steps \
that a machine can easily interpret and you know how to \
choose a solution that has a good balance between \
time complexity and space complexity. 

Here is a question:
{input}"""
```

```python
prompt_infos = [
    {
        "name": "physics", 
        "description": "Good for answering questions about physics", 
        "prompt_template": physics_template
    },
    {
        "name": "math", 
        "description": "Good for answering math questions", 
        "prompt_template": math_template
    },
    {
        "name": "History", 
        "description": "Good for answering history questions", 
        "prompt_template": history_template
    },
    {
        "name": "computer science", 
        "description": "Good for answering computer science questions", 
        "prompt_template": computerscience_template
    }
]
```


```python
from langchain.chains.router import MultiPromptChain
from langchain.chains.router.llm_router import LLMRouterChain,RouterOutputParser
from langchain.prompts import PromptTemplate

llm = ChatOpenAI(temperature=0, model=llm_model)


destination_chains = {}
for p_info in prompt_infos:
    name = p_info["name"]
    prompt_template = p_info["prompt_template"]
    prompt = ChatPromptTemplate.from_template(template=prompt_template)
    chain = LLMChain(llm=llm, prompt=prompt)
    destination_chains[name] = chain  
    
destinations = [f"{p['name']}: {p['description']}" for p in prompt_infos]
destinations_str = "\n".join(destinations)
```


```python
default_prompt = ChatPromptTemplate.from_template("{input}")
default_chain = LLMChain(llm=llm, prompt=default_prompt)
```

`````python
MULTI_PROMPT_ROUTER_TEMPLATE = """Given a raw text input to a \
language model select the model prompt best suited for the input. \
You will be given the names of the available prompts and a \
description of what the prompt is best suited for. \
You may also revise the original input if you think that revising\
it will ultimately lead to a better response from the language model.

<< FORMATTING >>
Return a markdown code snippet with a JSON object formatted to look like:
```json
{{{{
    "destination": string \ name of the prompt to use or "DEFAULT"
    "next_inputs": string \ a potentially modified version of the original input
}}}}
```

REMEMBER: "destination" MUST be one of the candidate prompt \
names specified below OR it can be "DEFAULT" if the input is not\
well suited for any of the candidate prompts.
REMEMBER: "next_inputs" can just be the original input \
if you don't think any modifications are needed.

<< CANDIDATE PROMPTS >>
{destinations}

<< INPUT >>
{{input}}

<< OUTPUT (remember to include the ```json)>>"""
`````

```python
router_template = MULTI_PROMPT_ROUTER_TEMPLATE.format(
    destinations=destinations_str
)
router_prompt = PromptTemplate(
    template=router_template,
    input_variables=["input"],
    output_parser=RouterOutputParser(),
)

router_chain = LLMRouterChain.from_llm(llm, router_prompt)
```

```python
chain = MultiPromptChain(router_chain=router_chain, 
                         destination_chains=destination_chains, 
                         default_chain=default_chain, verbose=True
                        )
```


```python
chain = MultiPromptChain(router_chain=router_chain, 
                         destination_chains=destination_chains, 
                         default_chain=default_chain, verbose=True
                        )
```


```python
chain.run("What is black body radiation?")
```

> Entering new MultiPromptChain chain...
physics: {'input': 'What is black body radiation?'}
> Finished chain.
>
>	"Black body radiation refers to the electromagnetic radiation emitted by a perfect black body, which is an object that absorbs all radiation that falls on it and emits radiation at all wavelengths. The radiation emitted by a black body depends only on its temperature and follows a specific distribution known as Planck's law. This type of radiation is important in understanding the behavior of stars, as well as in the development of technologies such as incandescent light bulbs and infrared cameras."


```python
chain.run("what is 2 + 2")
```

> Entering new MultiPromptChain chain...
math: {'input': 'what is 2 + 2'}
> Finished chain.
>
	'As an AI language model, I can answer this question easily. The answer to 2 + 2 is 4.'



### Q&A over Documents

![](https://i.imgur.com/m7Imxxe.png)


![](https://i.imgur.com/WlBh3UC.png)


![](https://i.imgur.com/vJFtsX8.png)

![](https://i.imgur.com/GMkCgB6.png)


### Code

#### LangChain: Q&A over Documents

  

An example might be a tool that would allow you to query a product catalog for items of interest.

  
  

```python

#pip install --upgrade langchain

```

  
  

```python

import os

  

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv()) # read local .env file

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

from langchain.chains import RetrievalQA

from langchain.chat_models import ChatOpenAI

from langchain.document_loaders import CSVLoader

from langchain.vectorstores import DocArrayInMemorySearch

from IPython.display import display, Markdown

from langchain.llms import OpenAI

```

  
  

```python

file = 'OutdoorClothingCatalog_1000.csv'

loader = CSVLoader(file_path=file)

```

  
  

```python

from langchain.indexes import VectorstoreIndexCreator

```

  
  

```python

#pip install docarray

```

  
  

```python

index = VectorstoreIndexCreator(

vectorstore_cls=DocArrayInMemorySearch

).from_loaders([loader])

```

  
  

```python

query ="Please list all your shirts with sun protection \

in a table in markdown and summarize each one."

```

  

**Note**:

- The notebook uses `langchain==0.0.179` and `openai==0.27.7`

- For these library versions, `VectorstoreIndexCreator` uses `text-davinci-003` as the base model, which has been deprecated since 1 January 2024.

- The replacement model, `gpt-3.5-turbo-instruct` will be used instead for the `query`.

- The `response` format might be different than the video because of this replacement model.

  
  

```python

llm_replacement_model = OpenAI(temperature=0,

model='gpt-3.5-turbo-instruct')

  

response = index.query(query,

llm = llm_replacement_model)

```

  
  

```python

display(Markdown(response))

```

  
  
  
  

| Name | Description | Sun Protection Rating |
| ---- | ---- | ---- |
| Men's Tropical Plaid Short-Sleeve Shirt | Made of 100% polyester, UPF 50+ rated, wrinkle-resistant, front and back cape venting, two front bellows pockets, imported | SPF 50+, blocks 98% of harmful UV rays |
| Men's Plaid Tropic Shirt, Short-Sleeve | Made of 52% polyester and 48% nylon, UPF 50+ rated, SunSmart technology blocks 98% of harmful UV rays, wrinkle-free, front and back cape venting, two front bellows pockets, imported | SPF 50+, blocks 98% of harmful UV rays |
| Men's TropicVibe Shirt, Short-Sleeve | Made of 71% nylon and 29% polyester, UPF 50+ rated, front and back cape venting, two front bellows pockets, imported | SPF 50+, blocks 98% of harmful UV rays |
| Sun Shield Shirt | Made of 78% nylon and 22% Lycra Xtra Life fiber, UPF 50+ rated, wicks moisture, fits comfortably over swimsuit, abrasion resistant |  |

  
  

#### Step By Step

  
  

```python

from langchain.document_loaders import CSVLoader

loader = CSVLoader(file_path=file)

```

  
  

```python

docs = loader.load()

```

  
  

```python

docs[0]

```

  
  
  
  

Document(page_content=": 0\nname: Women's Campside Oxfords\ndescription: This ultracomfortable lace-to-toe Oxford boasts a super-soft canvas, thick cushioning, and quality construction for a broken-in feel from the first time you put them on. \n\nSize & Fit: Order regular shoe size. For half sizes not offered, order up to next whole size. \n\nSpecs: Approx. weight: 1 lb.1 oz. per pair. \n\nConstruction: Soft canvas material for a broken-in feel and look. Comfortable EVA innersole with Cleansport NXT® antimicrobial odor control. Vintage hunt, fish and camping motif on innersole. Moderate arch contour of innersole. EVA foam midsole for cushioning and support. Chain-tread-inspired molded rubber outsole with modified chain-tread pattern. Imported. \n\nQuestions? Please contact us for any inquiries.", metadata={'source': 'OutdoorClothingCatalog_1000.csv', 'row': 0})

  
  
  
  

```python

from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()

```

  
  

```python

embed = embeddings.embed_query("Hi my name is Harrison")

```

  
  

```python

print(len(embed))

```

  

1536

  
  
  

```python

print(embed[:5])

```

  

	[-0.0219351164996624, 0.006751196924597025, -0.0182583499699831, -0.03915192559361458, -0.013979244977235794]

  
  
  

```python

db = DocArrayInMemorySearch.from_documents(

docs,

embeddings

)

```

  
  

```python

query = "Please suggest a shirt with sunblocking"

```

  
  

```python

docs = db.similarity_search(query)

```

  
  

```python

len(docs)

```

  
  
  
  

4

  
  
  
  

```python

docs[0]

```

  
  
  
  

Document(page_content=': 255\nname: Sun Shield Shirt by\ndescription: "Block the sun, not the fun – our high-performance sun shirt is guaranteed to protect from harmful UV rays. \n\nSize & Fit: Slightly Fitted: Softly shapes the body. Falls at hip.\n\nFabric & Care: 78% nylon, 22% Lycra Xtra Life fiber. UPF 50+ rated – the highest rated sun protection possible. Handwash, line dry.\n\nAdditional Features: Wicks moisture for quick-drying comfort. Fits comfortably over your favorite swimsuit. Abrasion resistant for season after season of wear. Imported.\n\nSun Protection That Won\'t Wear Off\nOur high-performance fabric provides SPF 50+ sun protection, blocking 98% of the sun\'s harmful rays. This fabric is recommended by The Skin Cancer Foundation as an effective UV protectant.', metadata={'source': 'OutdoorClothingCatalog_1000.csv', 'row': 255})

  
  
  
  

```python

retriever = db.as_retriever()

```

  
  

```python

llm = ChatOpenAI(temperature = 0.0, model=llm_model)

```

  
  

```python

qdocs = "".join([docs[i].page_content for i in range(len(docs))])

  

```

  
  

```python

response = llm.call_as_llm(f"{qdocs} Question: Please list all your \

shirts with sun protection in a table in markdown and summarize each one.")

  

```

  
  

```python

display(Markdown(response))

```

  
  

| Name | Description |
| --- | --- |
| Sun Shield Shirt | High-performance sun shirt with UPF 50+ sun protection, moisture-wicking, and abrasion-resistant fabric. Recommended by The Skin Cancer Foundation. |
| Men's Plaid Tropic Shirt | Ultracomfortable shirt with UPF 50+ sun protection, wrinkle-free fabric, and front/back cape venting. Made with 52% polyester and 48% nylon. |
| Men's TropicVibe Shirt | Men's sun-protection shirt with built-in UPF 50+ and front/back cape venting. Made with 71% nylon and 29% polyester. |
| Men's Tropical Plaid Short-Sleeve Shirt | Lightest hot-weather shirt with UPF 50+ sun protection, front/back cape venting, and two front bellows pockets. Made with 100% polyester. |

  

All of these shirts provide UPF 50+ sun protection, blocking 98% of the sun's harmful rays. They also have additional features such as moisture-wicking, wrinkle-free fabric, and front/back cape venting for added comfort.

  
  
  

```python

qa_stuff = RetrievalQA.from_chain_type(

llm=llm,

chain_type="stuff",

retriever=retriever,

verbose=True

)

```

  
  

```python

query = "Please list all your shirts with sun protection in a table \

in markdown and summarize each one."

```

  
  

```python

response = qa_stuff.run(query)

```

  

[1m> Entering new RetrievalQA chain...[0m

[1m> Finished chain.[0m

  
  
  

```python

display(Markdown(response))

```

  
  

| Shirt Number | Name | Description |
| --- | --- | --- |
| 618 | Men's Tropical Plaid Short-Sleeve Shirt | This shirt is made of 100% polyester and is wrinkle-resistant. It has front and back cape venting that lets in cool breezes and two front bellows pockets. It is rated UPF 50+ for superior protection from the sun's UV rays. |
| 374 | Men's Plaid Tropic Shirt, Short-Sleeve | This shirt is made with 52% polyester and 48% nylon. It is machine washable and dryable. It has front and back cape venting, two front bellows pockets, and is rated to UPF 50+. |
| 535 | Men's TropicVibe Shirt, Short-Sleeve | This shirt is made of 71% Nylon and 29% Polyester. It has front and back cape venting that lets in cool breezes and two front bellows pockets. It is rated UPF 50+ for superior protection from the sun's UV rays. |
| 255 | Sun Shield Shirt | This shirt is made of 78% nylon and 22% Lycra Xtra Life fiber. It is handwashable and line dry. It is rated UPF 50+ for superior protection from the sun's UV rays. It is abrasion-resistant and wicks moisture for quick-drying comfort. |
  

The Men's Tropical Plaid Short-Sleeve Shirt is made of 100% polyester and is wrinkle-resistant. It has front and back cape venting that lets in cool breezes and two front bellows pockets. It is rated UPF 50+ for superior protection from the sun's UV rays.

  

The Men's Plaid Tropic Shirt, Short-Sleeve is made with 52% polyester and 48% nylon. It has front and back cape venting, two front bellows pockets, and is rated to UPF 50+.

  

The Men's TropicVibe Shirt, Short-Sleeve is made of 71% Nylon and 29% Polyester. It has front and back cape venting that lets in cool breezes and two front bellows pockets. It is rated UPF 50+ for superior protection from the sun's UV rays.

  

The Sun Shield Shirt is made of 78% nylon and 22% Lycra Xtra Life fiber. It is abrasion-resistant and wicks moisture for quick-drying comfort. It is rated UPF 50+ for superior protection from the sun's UV rays.

  
  
  

```python

response = index.query(query, llm=llm)

```

  
  

```python

index = VectorstoreIndexCreator(

vectorstore_cls=DocArrayInMemorySearch,

embedding=embeddings,

).from_loaders([loader])

```

  

Reminder: Download your notebook to you local computer to save your work.



![](https://i.imgur.com/bj12AQp.png)


![](https://i.imgur.com/ZYzpL6C.png)


## Evaulation

### Outline:

* Example generation

* Manual evaluation (and debuging)

* LLM-assisted evaluation

* LangChain evaluation platform

### Code
  
```python

import os

  

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv()) # read local .env file

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

  

#### Create our QandA application

  
  

```python

from langchain.chains import RetrievalQA

from langchain.chat_models import ChatOpenAI

from langchain.document_loaders import CSVLoader

from langchain.indexes import VectorstoreIndexCreator

from langchain.vectorstores import DocArrayInMemorySearch

```

  
  

```python

file = 'OutdoorClothingCatalog_1000.csv'

loader = CSVLoader(file_path=file)

data = loader.load()

```

  
  

```python

index = VectorstoreIndexCreator(

vectorstore_cls=DocArrayInMemorySearch

).from_loaders([loader])

```

  
  

```python

llm = ChatOpenAI(temperature = 0.0, model=llm_model)

qa = RetrievalQA.from_chain_type(

llm=llm,

chain_type="stuff",

retriever=index.vectorstore.as_retriever(),

verbose=True,

chain_type_kwargs = {

"document_separator": "<<<<>>>>>"

}

)

```

  

##### Coming up with test datapoints

  
  

```python

data[10]

```

  
  

```python

data[11]

```

  

##### Hard-coded examples

  
  

```python

examples = [

{

"query": "Do the Cozy Comfort Pullover Set\

have side pockets?",

"answer": "Yes"

},

{

"query": "What collection is the Ultra-Lofty \

850 Stretch Down Hooded Jacket from?",

"answer": "The DownTek collection"

}

]

```

  

##### LLM-Generated examples

  
  

```python

from langchain.evaluation.qa import QAGenerateChain

  

```

  
  

```python

example_gen_chain = QAGenerateChain.from_llm(ChatOpenAI(model=llm_model))

```

  
  

```python

# the warning below can be safely ignored

```

  
  

```python

new_examples = example_gen_chain.apply_and_parse(

[{"doc": t} for t in data[:5]]

)

```

  
  

```python

new_examples[0]

```

  {'query': "What is the weight of the Women's Campside Oxfords per pair?",
 'answer': "The approximate weight of the Women's Campside Oxfords per pair is 1 lb.1 oz."}
  

```python

data[0]

```

  Document(page_content=": 0\nname: Women's Campside Oxfords\ndescription: This ultracomfortable lace-to-toe Oxford boasts a super-soft canvas, thick cushioning, and quality construction for a broken-in feel from the first time you put them on. \n\nSize & Fit: Order regular shoe size. For half sizes not offered, order up to next whole size. \n\nSpecs: Approx. weight: 1 lb.1 oz. per pair. \n\nConstruction: Soft canvas material for a broken-in feel and look. Comfortable EVA innersole with Cleansport NXT® antimicrobial odor control. Vintage hunt, fish and camping motif on innersole. Moderate arch contour of innersole. EVA foam midsole for cushioning and support. Chain-tread-inspired molded rubber outsole with modified chain-tread pattern. Imported. \n\nQuestions? Please contact us for any inquiries.", metadata={'source': 'OutdoorClothingCatalog_1000.csv', 'row': 0})

##### Combine examples

  
  

```python

examples += new_examples

```

  
  

```python

qa.run(examples[0]["query"])

```

  

#### Manual Evaluation

  
  

```python

import langchain

langchain.debug = True

```

  
  

```python

qa.run(examples[0]["query"])

```

	  [chain/start] [1:chain:RetrievalQA] Entering Chain run with input:
	{
	  "query": "Do the Cozy Comfort Pullover Set        have side pockets?"
	}
	[chain/start] [1:chain:RetrievalQA > 2:chain:StuffDocumentsChain] Entering Chain run with input:
	[inputs]
	[chain/start] [1:chain:RetrievalQA > 2:chain:StuffDocumentsChain > 3:chain:LLMChain] Entering Chain run with input:
	{
	  "question": "Do the Cozy Comfort Pullover Set        have side pockets?",
	  "context": ": 10\nname: Cozy Comfort Pullover Set, Stripe\ndescription: Perfect for lounging, this striped knit set lives up to its name. We used ultrasoft fabric and an easy design that's as comfortable at bedtime as it is when we have to make a quick run out.\n\nSize & Fit\n- Pants are Favorite Fit: Sits lower on the waist.\n- Relaxed Fit: Our most generous fit sits farthest from the body.\n\nFabric & Care\n- In the softest blend of 63% polyester, 35% rayon and 2% spandex.\n\nAdditional Features\n- Relaxed fit top with raglan sleeves and rounded hem.\n- Pull-on pants have a wide elastic waistband and drawstring, side pockets and a modern slim leg.\n\nImported.<<<<>>>>>: 73\nname: Cozy Cuddles Knit Pullover Set\ndescription: Perfect for lounging, this knit set lives up to its name. We used ultrasoft fabric and an easy design that's as comfortable at bedtime as it is when we have to make a quick run out. \n\nSize & Fit \nPants are Favorite Fit: Sits lower on the waist. \nRelaxed Fit: Our most generous fit sits farthest from the body. \n\nFabric & Care \nIn the softest blend of 63% polyester, 35% rayon and 2% spandex.\n\nAdditional Features \nRelaxed fit top with raglan sleeves and rounded hem. \nPull-on pants have a wide elastic waistband and drawstring, side pockets and a modern slim leg. \nImported.<<<<>>>>>: 632\nname: Cozy Comfort Fleece Pullover\ndescription: The ultimate sweater fleece \u2013 made from superior fabric and offered at an unbeatable price. \n\nSize & Fit\nSlightly Fitted: Softly shapes the body. Falls at hip. \n\nWhy We Love It\nOur customers (and employees) love the rugged construction and heritage-inspired styling of our popular Sweater Fleece Pullover and wear it for absolutely everything. From high-intensity activities to everyday tasks, you'll find yourself reaching for it every time.\n\nFabric & Care\nRugged sweater-knit exterior and soft brushed interior for exceptional warmth and comfort. Made from soft, 100% polyester. Machine wash and dry.\n\nAdditional Features\nFeatures our classic Mount Katahdin logo. Snap placket. Front princess seams create a feminine shape. Kangaroo handwarmer pockets. Cuffs and hem reinforced with jersey binding. Imported.\n\n \u2013 Official Supplier to the U.S. Ski Team\nTHEIR WILL TO WIN, WOVEN RIGHT IN. LEARN MORE<<<<>>>>>: 151\nname: Cozy Quilted Sweatshirt\ndescription: Our sweatshirt is an instant classic with its great quilted texture and versatile weight that easily transitions between seasons. With a traditional fit that is relaxed through the chest, sleeve, and waist, this pullover is lightweight enough to be worn most months of the year. The cotton blend fabric is super soft and comfortable, making it the perfect casual layer. To make dressing easy, this sweatshirt also features a snap placket and a heritage-inspired Mt. Katahdin logo patch. For care, machine wash and dry. Imported."
	}
	[llm/start] [1:chain:RetrievalQA > 2:chain:StuffDocumentsChain > 3:chain:LLMChain > 4:llm:ChatOpenAI] Entering LLM run with input:
	{
	  "prompts": [
	    "System: Use the following pieces of context to answer the users question. \nIf you don't know the answer, just say that you don't know, don't try to make up an answer.\n----------------\n: 10\nname: Cozy Comfort Pullover Set, Stripe\ndescription: Perfect for lounging, this striped knit set lives up to its name. We used ultrasoft fabric and an easy design that's as comfortable at bedtime as it is when we have to make a quick run out.\n\nSize & Fit\n- Pants are Favorite Fit: Sits lower on the waist.\n- Relaxed Fit: Our most generous fit sits farthest from the body.\n\nFabric & Care\n- In the softest blend of 63% polyester, 35% rayon and 2% spandex.\n\nAdditional Features\n- Relaxed fit top with raglan sleeves and rounded hem.\n- Pull-on pants have a wide elastic waistband and drawstring, side pockets and a modern slim leg.\n\nImported.<<<<>>>>>: 73\nname: Cozy Cuddles Knit Pullover Set\ndescription: Perfect for lounging, this knit set lives up to its name. We used ultrasoft fabric and an easy design that's as comfortable at bedtime as it is when we have to make a quick run out. \n\nSize & Fit \nPants are Favorite Fit: Sits lower on the waist. \nRelaxed Fit: Our most generous fit sits farthest from the body. \n\nFabric & Care \nIn the softest blend of 63% polyester, 35% rayon and 2% spandex.\n\nAdditional Features \nRelaxed fit top with raglan sleeves and rounded hem. \nPull-on pants have a wide elastic waistband and drawstring, side pockets and a modern slim leg. \nImported.<<<<>>>>>: 632\nname: Cozy Comfort Fleece Pullover\ndescription: The ultimate sweater fleece \u2013 made from superior fabric and offered at an unbeatable price. \n\nSize & Fit\nSlightly Fitted: Softly shapes the body. Falls at hip. \n\nWhy We Love It\nOur customers (and employees) love the rugged construction and heritage-inspired styling of our popular Sweater Fleece Pullover and wear it for absolutely everything. From high-intensity activities to everyday tasks, you'll find yourself reaching for it every time.\n\nFabric & Care\nRugged sweater-knit exterior and soft brushed interior for exceptional warmth and comfort. Made from soft, 100% polyester. Machine wash and dry.\n\nAdditional Features\nFeatures our classic Mount Katahdin logo. Snap placket. Front princess seams create a feminine shape. Kangaroo handwarmer pockets. Cuffs and hem reinforced with jersey binding. Imported.\n\n \u2013 Official Supplier to the U.S. Ski Team\nTHEIR WILL TO WIN, WOVEN RIGHT IN. LEARN MORE<<<<>>>>>: 151\nname: Cozy Quilted Sweatshirt\ndescription: Our sweatshirt is an instant classic with its great quilted texture and versatile weight that easily transitions between seasons. With a traditional fit that is relaxed through the chest, sleeve, and waist, this pullover is lightweight enough to be worn most months of the year. The cotton blend fabric is super soft and comfortable, making it the perfect casual layer. To make dressing easy, this sweatshirt also features a snap placket and a heritage-inspired Mt. Katahdin logo patch. For care, machine wash and dry. Imported.\nHuman: Do the Cozy Comfort Pullover Set        have side pockets?"
	  ]
	}
	[llm/end] [1:chain:RetrievalQA > 2:chain:StuffDocumentsChain > 3:chain:LLMChain > 4:llm:ChatOpenAI] [334.181ms] Exiting LLM run with output:
	{
	  "generations": [
	    [
	      {
	        "text": "The Cozy Comfort Pullover Set, Stripe has side pockets.",
	        "generation_info": null,
	        "message": {
	          "content": "The Cozy Comfort Pullover Set, Stripe has side pockets.",
	          "additional_kwargs": {},
	          "example": false
	        }
	      }
	    ]
	  ],
	  "llm_output": {
	    "token_usage": {
	      "prompt_tokens": 734,
	      "completion_tokens": 13,
	      "total_tokens": 747
	    },
	    "model_name": "gpt-3.5-turbo-0301"
	  }
	}
	[chain/end] [1:chain:RetrievalQA > 2:chain:StuffDocumentsChain > 3:chain:LLMChain] [434.547ms] Exiting Chain run with output:
	{
	  "text": "The Cozy Comfort Pullover Set, Stripe has side pockets."
	}
	[chain/end] [1:chain:RetrievalQA > 2:chain:StuffDocumentsChain] [449.445ms] Exiting Chain run with output:
	{
	  "output_text": "The Cozy Comfort Pullover Set, Stripe has side pockets."
	}
	[chain/end] [1:chain:RetrievalQA] [574.043ms] Exiting Chain run with output:
	{
	  "result": "The Cozy Comfort Pullover Set, Stripe has side pockets."
	}
	
	'The Cozy Comfort Pullover Set, Stripe has side pockets.'
	  

```python

# Turn off the debug mode

langchain.debug = False

```

  

#### LLM assisted evaluation

  
  

```python

predictions = qa.apply(examples)

```

  
  

```python

from langchain.evaluation.qa import QAEvalChain

```

  
  

```python

llm = ChatOpenAI(temperature=0, model=llm_model)

eval_chain = QAEvalChain.from_llm(llm)

```

  
  

```python

graded_outputs = eval_chain.evaluate(examples, predictions)

```

  
  

```python

for i, eg in enumerate(examples):

print(f"Example {i}:")

print("Question: " + predictions[i]['query'])

print("Real Answer: " + predictions[i]['answer'])

print("Predicted Answer: " + predictions[i]['result'])

print("Predicted Grade: " + graded_outputs[i]['text'])

print()

```

	  Example 0:
	Question: Do the Cozy Comfort Pullover Set        have side pockets?
	Real Answer: Yes
	Predicted Answer: The Cozy Comfort Pullover Set, Stripe has side pockets.
	Predicted Grade: CORRECT
	
	Example 1:
	Question: What collection is the Ultra-Lofty         850 Stretch Down Hooded Jacket from?
	Real Answer: The DownTek collection
	Predicted Answer: The Ultra-Lofty 850 Stretch Down Hooded Jacket is from the DownTek collection.
	Predicted Grade: CORRECT
	
	Example 2:
	Question: What is the weight of the Women's Campside Oxfords per pair?
	Real Answer: The approximate weight of the Women's Campside Oxfords per pair is 1 lb.1 oz.
	Predicted Answer: The Women's Campside Oxfords weigh approximately 1 lb. 1 oz. per pair.
	Predicted Grade: CORRECT
	
	Example 3:
	Question: What are the dimensions of the small and medium sizes of the Recycled Waterhog Dog Mat, Chevron Weave?
	Real Answer: The small size has dimensions of 18" x 28" and the medium size has dimensions of 22.5" x 34.5".
	Predicted Answer: The small size of the Recycled Waterhog Dog Mat, Chevron Weave has dimensions of 18" x 28", and the medium size has dimensions of 22.5" x 34.5".
	Predicted Grade: CORRECT
	
	Example 4:
	Question: What features does the Infant and Toddler Girls' Coastal Chill Swimsuit have?
	Real Answer: The swimsuit has bright colors, ruffles, exclusive whimsical prints, four-way-stretch, chlorine-resistant fabric, UPF 50+ rated fabric, crossover no-slip straps, fully lined bottom, and provides maximum coverage. It is machine washable and should be line dried for best results.
	Predicted Answer: The Infant and Toddler Girls' Coastal Chill Swimsuit is a two-piece swimsuit with bright colors, ruffles, and exclusive whimsical prints. It has four-way-stretch and chlorine-resistant fabric that keeps its shape and resists snags. The UPF 50+ rated fabric provides the highest rated sun protection possible, blocking 98% of the sun's harmful rays. The crossover no-slip straps and fully lined bottom ensure a secure fit and maximum coverage. It is machine washable and should be line dried for best results.
	Predicted Grade: CORRECT
	
	Example 5:
	Question: What is the fabric composition of the Refresh Swimwear, V-Neck Tankini Contrasts?
	Real Answer: The Refresh Swimwear, V-Neck Tankini Contrasts is made of 82% recycled nylon with 18% Lycra® spandex for the body and 90% recycled nylon with 10% Lycra® spandex for the lining.
	Predicted Answer: The Refresh Swimwear, V-Neck Tankini Contrasts is made of 82% recycled nylon with 18% Lycra® spandex for the body and 90% recycled nylon with 10% Lycra® spandex for the lining.
	Predicted Grade: CORRECT
	
	Example 6:
	Question: What is the new technology used in EcoFlex 3L Storm Pants?
	Real Answer: The new technology used in EcoFlex 3L Storm Pants is TEK O2 technology which offers the most breathability they have ever tested.
	Predicted Answer: The new technology used in EcoFlex 3L Storm Pants is TEK O2 technology, which makes the pants more breathable and waterproof.
	Predicted Grade: CORRECT
  

```python

graded_outputs[0]

```

  

#### LangChain evaluation platform

  

The LangChain evaluation platform, LangChain Plus, can be accessed here https://www.langchain.plus/.

Use the invite code `lang_learners_2023`


## Agents

```python
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

import warnings
warnings.filterwarnings("ignore")
```

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

#### Built-in LangChain tools

```python
from langchain.agents.agent_toolkits import create_python_agent
from langchain.agents import load_tools, initialize_agent
from langchain.agents import AgentType
from langchain.tools.python.tool import PythonREPLTool
from langchain.python import PythonREPL
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0, model=llm_model)
tools = load_tools(["llm-math","wikipedia"], llm=llm)
agent= initialize_agent(
    tools, 
    llm, 
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
    verbose = True)

agent("What is the 25% of 300?")
```

> 	Entering new AgentExecutor chain...
	Thought: We need to calculate 25% of 300, which means we need to multiply 300 by 0.25.
	
	Action:
	```
	{
	  "action": "Calculator",
	  "action_input": "300*0.25"
	}
	```
	
	Retrying langchain.chat_models.openai.ChatOpenAI.completion_with_retry.<locals>._completion_with_retry in 1.0 seconds as it raised APIError: HTTP code 500 from API (500 error
	).
	
	Observation: Answer: 75.0
	Thought:The calculator tool returned the correct answer of 75.0.
	
	Final Answer: 25% of 300 is 75.0.
	
> 	Finished chain.
	
	{'input': 'What is the 25% of 300?', 'output': '25% of 300 is 75.0.'}

#### Wikipedia Example

```python
question = "Tom M. Mitchell is an American computer scientist \
and the Founders University Professor at Carnegie Mellon University (CMU)\
what book did he write?"
result = agent(question) 
```

	
> 	Entering new AgentExecutor chain...
	Thought: I should use Wikipedia to find the answer to this question.
	
	Action:
	```
	{
	  "action": "Wikipedia",
	  "action_input": "Tom M. Mitchell"
	}
	```
	
	Observation: Page: Tom M. Mitchell
	Summary: Tom Michael Mitchell (born August 9, 1951) is an American computer scientist and the Founders University Professor at Carnegie Mellon University (CMU). He is a founder and former Chair of the Machine Learning Department at CMU. Mitchell is known for his contributions to the advancement of machine learning, artificial intelligence, and cognitive neuroscience and is the author of the textbook Machine Learning. He is a member of the United States National Academy of Engineering since 2010. He is also a Fellow of the American Academy of Arts and Sciences, the American Association for the Advancement of Science and a Fellow and past President of the Association for the Advancement of Artificial Intelligence. In October 2018, Mitchell was appointed as the Interim Dean of the School of Computer Science at Carnegie Mellon.
	
	Page: Oren Etzioni
	Summary: Oren Etzioni (born 1964) is an American entrepreneur, Professor Emeritus of computer science, and founding CEO of the Allen Institute for Artificial Intelligence (AI2). On June 15, 2022, he announced that he will step down as CEO of AI2 effective September 30, 2022. After that time, he will continue as a board member and advisor. Etzioni will also take the position of Technical Director of the AI2 Incubator.
	Thought:I should look for the book "Machine Learning" by Tom M. Mitchell.
	
	Action:
	```
	{
	  "action": "Wikipedia",
	  "action_input": "Machine Learning Tom M. Mitchell"
	}
	```
	
	Observation: Page: Tom M. Mitchell
	Summary: Tom Michael Mitchell (born August 9, 1951) is an American computer scientist and the Founders University Professor at Carnegie Mellon University (CMU). He is a founder and former Chair of the Machine Learning Department at CMU. Mitchell is known for his contributions to the advancement of machine learning, artificial intelligence, and cognitive neuroscience and is the author of the textbook Machine Learning. He is a member of the United States National Academy of Engineering since 2010. He is also a Fellow of the American Academy of Arts and Sciences, the American Association for the Advancement of Science and a Fellow and past President of the Association for the Advancement of Artificial Intelligence. In October 2018, Mitchell was appointed as the Interim Dean of the School of Computer Science at Carnegie Mellon.
	
	Page: Machine learning
	Summary: Machine learning (ML) is a field of study in artificial intelligence concerned with the development and study of statistical algorithms that can learn from data and generalize to unseen data, and thus perform tasks without explicit instructions. Recently, generative artificial neural networks have been able to surpass many previous approaches in performance.Machine learning approaches have been applied to many fields including large language models (LLM), computer vision, speech recognition, email filtering, agriculture, and medicine, where it is too costly to develop algorithms to perform the needed tasks. ML is known in its application across business problems under the name predictive analytics. Although not all machine learning is statistically based, computational statistics is an important source of the field's methods.
	The mathematical foundations of ML are provided by mathematical optimization (mathematical programming) methods. Data mining is a related (parallel) field of study, focusing on exploratory data analysis (EDA) through unsupervised learning. From a theoretical point of view Probably approximately correct (PAC) learning provides a framework for describing machine learning.
	
	Page: Outline of machine learning
	Summary: The following outline is provided as an overview of and topical guide to machine learning:
	Machine learning – subfield of soft computing within computer science that evolved from the study of pattern recognition and computational learning theory in artificial intelligence. In 1959, Arthur Samuel defined machine learning as a "field of study that gives computers the ability to learn without being explicitly programmed". Machine learning explores the study and construction of algorithms that can learn from and make predictions on data. Such algorithms operate by building a model from an example training set of input observations in order to make data-driven predictions or decisions expressed as outputs, rather than following strictly static program instructions.
	Thought:The book "Machine Learning" was written by Tom M. Mitchell.
	
	Final Answer: Tom M. Mitchell wrote the book "Machine Learning".
	
> 	Finished chain.


#### Python Agent

```python
agent = create_python_agent(
    llm,
    tool=PythonREPLTool(),
    verbose=True
)
customer_list = [["Harrison", "Chase"], 
                 ["Lang", "Chain"],
                 ["Dolly", "Too"],
                 ["Elle", "Elem"], 
                 ["Geoff","Fusion"], 
                 ["Trance","Former"],
                 ["Jen","Ayai"]
                ]

agent.run(f"""Sort these customers by \
last name and then first name \
and print the output: {customer_list}""") 
```

	
> 	Entering new AgentExecutor chain...
	I can use the sorted() function to sort the list of customers by last name and then first name. I will need to provide a key function to sorted() that returns a tuple of the last name and first name in that order.
	Action: Python REPL
	Action Input:
	```
	customers = [['Harrison', 'Chase'], ['Lang', 'Chain'], ['Dolly', 'Too'], ['Elle', 'Elem'], ['Geoff', 'Fusion'], ['Trance', 'Former'], ['Jen', 'Ayai']]
	sorted_customers = sorted(customers, key=lambda x: (x[1], x[0]))
	for customer in sorted_customers:
	    print(customer)
	```
	Observation: ['Jen', 'Ayai']
	['Lang', 'Chain']
	['Harrison', 'Chase']
	['Elle', 'Elem']
	['Trance', 'Former']
	['Geoff', 'Fusion']
	['Dolly', 'Too']
	Thought:The customers have been sorted by last name and then first name, and the output has been printed. 
	Final Answer: [['Jen', 'Ayai'], ['Lang', 'Chain'], ['Harrison', 'Chase'], ['Elle', 'Elem'], ['Trance', 'Former'], ['Geoff', 'Fusion'], ['Dolly', 'Too']]
	
> 	Finished chain.
	
	"[['Jen', 'Ayai'], ['Lang', 'Chain'], ['Harrison', 'Chase'], ['Elle', 'Elem'], ['Trance', 'Former'], ['Geoff', 'Fusion'], ['Dolly', 'Too']]"


#### Define your own tool

```python
#!pip install DateTime
from langchain.agents import tool
from datetime import date

@tool
def time(text: str) -> str:
    """Returns todays date, use this for any \
    questions related to knowing todays date. \
    The input should always be an empty string, \
    and this function will always return todays \
    date - any date mathmatics should occur \
    outside this function."""
    return str(date.today())
```

```python
try:
    result = agent("whats the date today?") 
except: 
    print("exception on external access")
```


> 	Entering new AgentExecutor chain...
	Thought: I need to use the `time` tool to get today's date.
	Action:
	```
	{
	  "action": "time",
	  "action_input": ""
	}
	```
	Observation: 2024-03-03
	Thought:I successfully used the `time` tool to get today's date.
	Final Answer: Today's date is 2024-03-03.
	
> 	Finished chain.