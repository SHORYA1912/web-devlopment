import io
from shlex import join
from urllib import response
import streamlit as st
import cohere
import config

co = cohere.Client(config.COHERE_API_KEY)

def generate_response(prompt,temperature=0.3, max_tokens= 300):

    try:
        
     response = co.chat(
        model='c4ai-aya-expanse-8b',
        prompt=prompt,
        max_tokens=300,
        temperature=0.5
     )
        
     return response.text.strip()
    except Exception as e:
     return f"Error: {str(e)}"

CSS = """
<style>
.history_wrap {max-height: 420px; overflow-y: auto; padding: right: 6px;}
.qa-card{border: 1px #6e6e6e solid;
        border-radius: 8px;
        padding: 14px-16px;
        margin-bottom: 10px;
        background-color: #f5f5f5;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);

q.{font-weight: 700; color: #0a6abd; margin-bottom: 8px;}} 
a.{white-space: pre-wrap; color: #333; line-height: 1.5 }
</style>
"""

def export_bytes(history):
    text = join([f"Q{i} {h['QUESTION']}\nA: {h['ANSWER']}\n\n"
    for i, h in enumerate(history, 1)
    ])
    return io.BytesIO(text.encode('utf-8'))

def setup_UI():
    st.set_page_config(page_title="AI ASSISTANT", )

    



