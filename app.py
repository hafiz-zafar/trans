# Import necessary libraries
import streamlit as st
from transformers import pipeline

# Define a function to translate text using multiple models
def translate_text(text, model_name):
    if model_name == "Helsinki-NLP/opus-mt-en-ar":
        translator = pipeline("translation_en_to_ar", model=model_name)
    elif model_name == "facebook/m2m100_418M":
        translator = pipeline("translation", model=model_name, src_lang="en", tgt_lang="ar")
    else:
        raise ValueError("Unsupported model name")
    
    translation = translator(text)
    return translation[0]['translation_text']

# Streamlit app
def main():
    st.title("English to Arabic Translation using Multiple Models")
    
    # Text input
    text_to_translate = st.text_area("Enter English text to translate:", "Hello, how are you?")
    
    # Model selection
    model_name = st.selectbox("Choose a translation model:", ["Helsinki-NLP/opus-mt-en-ar", "facebook/m2m100_418M"])
    
    # Translate button
    if st.button("Translate"):
        if text_to_translate:
            translated_text = translate_text(text_to_translate, model_name)
            st.success(f"Translated Text: {translated_text}")
        else:
            st.warning("Please enter some text to translate.")

if __name__ == "__main__":
    main()