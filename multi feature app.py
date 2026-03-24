import io
import re
import cohere
from typer import prompt
import config
import streamlit as st

co = cohere.Client(api_key=config.COHERE_API_KEY)

system_prompt = " YOU ARE A MATHS MASTER-MIND, YOU CAN SOLVE ANY PROBLEM,AND EXPLAIN IT TO THE USER , SOLVE IT WITH CORRECT NOTATION AND GIVE THE FINAL ANSWER STEP BY STEP, AND BREIF THE FOLLOWING ANSWER GIVEN BY YOU"

def generate(prompt, temperature = 0.3, tokens=1000):
    try:
        r = co.chat(
            model = "c4ai-aya-expanse-8b",
            message = prompt,
            temperature = temperature,
            max_tokens = tokens
        )
    
        return r.text.strip()
    except Exception as e:
        return f"Error generating response: {str(e)}"
    
def looks_incomplete(prompt):
    return not text.strip().endswith(('.', '!', '?', '...'))

def generate_complete():
    ans = generate(system_prompt + "\n\n" + prompt)

    if looks_incomplete(ans):
        cont = generate((system_prompt + "\n\n" + prompt + "\n\n CONTINUE THE ANSWER FROM THE LAST WORDS GIVEN BY YOU")
        temperature = 0.3
        tokens = 1000
    )
        ans = ans + "\n\n" + cont

    return ans

def export_txt(content):
    for i in enumerate(HISTORY_1):
        with open(f"answer_{i+1}.txt", "w") as f:
            f.write(content[i])
    return io.BytesIO(content.encode())

def run_ai_teaching_assistant():
        st.title("AI TEACHING ASSISTANT")
        st.session_state.setdefault("HISTORY_1", [])

        temp = st.slider("TEMPERATURE", 0.0, 1.0, 0.3, step=0.1)
        tokens = st.slider("MAX TOKENS", 100, 4000, 1000, step=100)
        memory = st.checkbox("MEMORY", value=True)

        col1 ,col2 = st.columns(2)
        if col1.button("CLEAR HISTORY"):
            st.session_state.HISTORY_1 = []
            st.rerun()

        if col2.button("EXPORT HISTORY"):
            if not st.session_state.HISTORY_1:
                st.warning("No history to export.")
                return
            content = "\n\n".join(st.session_state.HISTORY_1)
            txt_file = export_txt(content)
            st.download_button("DOWNLOAD HISTORY", data=txt_file, file_name="history.txt", mime="text/plain")

            q = st.text_area("ENTER YOUR QUESTION HERE")
            if st.button("ASK"):
                if not q.strip():
                    st.warning("Please enter a question.")
                    return

                with st.spinner("Generating answer..."):
                    ans = generate_complete()

                st.session_state.HISTORY_1.append(f"Q: {q}\nA: {ans}")
                st.markdown(f"**Q:** {q}\n\n**A:** {ans}")

            else:
                with st.spinner("Thinking..."):
                    ans = generate_complete()
                    q = prompt


            