import streamlit as st
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.callbacks import get_openai_callback
load_dotenv()

st.set_page_config(page_title="Ask your CSV!")
st.header("Ask your CSV")

csv=st.file_uploader("Upload your csv",type="csv")

if csv is not None:
    
    user_question= st.text_input("Ask a question")

    llm= OpenAI(temperature=0)
    agent= create_csv_agent(llm,csv,verbose=True)

    if user_question is not None and user_question != "":
        with get_openai_callback() as cb:
            response=agent.run(user_question)
            print(cb)
        st.write(response)

