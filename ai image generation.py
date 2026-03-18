from numpy import place
import streamlit as st
from PIL import Image
from io import BytesIO
import urllib.parse
import requests
import re

block_words = [
    "suicide","kill","murder","self harm","violence","abuse","bomb","terrorism","drugs","weapon","knife","shoot","gun","explosive","assault","gore","blood","nazi","racism","hate","discrimination","harassment","bullying"
]

block_patterns= [
    r"/b(kill|murder|suicide|self\s*harm|violence)\b/i",
    r"/b(abuse|bomb|terrorism|drugs|weapon|knife|shoot|gun)\b/i",
    r"/b(explosive|assault|gore|blood|nazi|racism|hate)\b/i",
    r"/b(discrimination|harassment|bullying)\b/i"
]

def is_safe_prompt(prompt):
    p = prompt.lower()
    for words in block_words:
        if words in p:
            return False, f"Prompt contains blocked word: {words}"
    for pattern in block_patterns:
        if re.search(pattern, p):
            return False, f"Prompt matches blocked pattern: {pattern}"
        
    return True, "Prompt is safe."

def generate_image(prompt):
    ok ,reason = is_safe_prompt(prompt)
    if not ok:
        return None, f"Prompt blocked: {reason}"
    
    try:
        encoded_prompt = urllib.parse.quote(prompt)
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"
        response = requests.get(url)
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            return image, "Image generated successfully."
        else:
            return None, f"Failed to generate image. Status code: {response.status_code}"

    except Exception as e:
        return None, f"Error generating image: {str(e)}"
    
def main():
    st.set_page_config(page_title="AI Image Generation")
    st.title("AI IMAGE GENERATION")
    st.info("Enter a prompt to generate an image. Please avoid inappropriate content. AND SOME CONTENTS LIKE SUICIDE, KILL, VIOLENCE OR ETC.")
    prompt = st.text_area("ENTER YOUR IMAGE PROMPT HERE")

    with st.form("image_form"):
        raw = st.text_area("IMAGE DESCRIPTION", height = 120, placeholder = "FOR EXAMPLE: A beautiful landscape with mountains and a lake.")

        submit = st.form_submit_button("GENERATE IMAGE")

        if submit:
            if not raw.strip():
                st.warning("Please enter a description for the image.")
                return
            
            with st.spinner("Generating image..."):
                image, err = generate_image(raw)

            if err:
                st.error(err)
                return
            st.image(image, caption="Generated Image", use_column_width=True)
            st.session_state.generated_image = image

            image = st.session_state.get("generated_image")

            if image:
                buf = BytesIO()
                image.save(buf, format="PNG")
                buf.seek(0)

            st.download_button(
                label="Download Image",
                data=buf,
                file_name="generated_image.png",
                mime="image/png"
            )

if __name__ == "__main__":
    main()
