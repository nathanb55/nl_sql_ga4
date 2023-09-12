#---------- 0 i. import libraries
# general 
import pandas as pd
import streamlit as st

st.write("Test")

# langchain
from langchain.chat_models import ChatOpenAI 
#from langchain.document_loaders import BigQueryLoader
#from langchain.schema import HumanMessage
#from langchain.prompts import PromptTemplate
#from langchain.prompts.chat import (
#    ChatPromptTemplate,
#    SystemMessagePromptTemplate,
#    HumanMessagePromptTemplate,
#)
#from langchain.chains import LLMChain
#from langchain.memory import ConversationBufferMemory
#from langchain.tools import BaseTool
#from langchain.agents import initialize_agent
#from langchain.agents import Tool
#from langchain.agents import AgentType
#from langchain.agents import OpenAIFunctionsAgent
#from langchain.agents import AgentExecutor

# data connections
#from google.cloud import bigquery
#import google.auth
#from google.auth.transport.requests import Request
#from google.auth.compute_engine import _metadata

#import local scripts
#import tools 
#from tools import Directory, Table, Query, Dataframe

#---------- 0 ii. establish BigQuery API
# define BigQuery client, using application default credentials
#bigquery_client = bigquery.Client(
#    location="US", 
#    project='can-bq-training'
#)