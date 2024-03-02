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

  
  
  
  

	{'gift': False, 'delivery_days': 5, 'price_value': 'pretty affordable!'}

  
  
  
  

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

  