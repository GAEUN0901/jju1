# -*- coding: utf-8 -*-
"""OutputFixingParser.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1j8j0V2s3XLZXlgSA2SLCO3TtxPkmbNbv
"""

!pip install -qU langchain_openai

from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from langchain.output_parsers import OutputFixingParser
from typing import List

class Actor(BaseModel):
  name: str = Field(description = "name of an actor")
  film_names: List[str] = Field(description = "List of 5 Movies They Appeared In")

actor_query = "Generate the filmography for a random actor."

parser = PydanticOutputParser(pydantic_object = Actor)

base_Actor = "{'name': 'Tom Hanks', 'film_names': ['Forrest Gump']}"

parser.parse(base_Actor)

"""# OutputFixingParser 사용"""

# Initialize ChatOpenAI with the `gpt-4-turbo` model
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# Create the OutputFixingParser
fixing_parser = OutputFixingParser.from_llm(parser=parser, llm=llm)

# Example invalid JSON input
base_actor = "{'name': 'Tom Hanks', 'film_names': ['Forrest Gump']}"

# Parse the input
result = fixing_parser.parse(base_actor)

# Print the result
print(result)