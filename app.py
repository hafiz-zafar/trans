# Import necessary libraries
import streamlit as st
from transformers import pipeline

# Define a function for bidirectional translation using a selected model
def translate_text(text, model_name):
    # Detect if the input is English or Arabic (basic detection)
    if any(char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" for char in text):
        # Translate English to Arabic
        if model_name == "Helsinki-NLP/opus-mt-en-ar":
            translator = pipeline("translation_en_to_ar", model=model_name)
        elif model_name == "facebook/m2m100_418M":
            translator = pipeline("translation", model=model_name, src_lang="en", tgt_lang="ar")
    else:
        # Translate Arabic to English
        if model_name == "Helsinki-NLP/opus-mt-ar-en":
            translator = pipeline("translation_ar_to_en", model=model_name)
        elif model_name == "facebook/m2m100_418M":
            translator = pipeline("translation", model=model_name, src_lang="ar", tgt_lang="en")

    translation = translator(text)
    return translation[0]['translation_text']

# Streamlit app
def main():
    st.title("Bidirectional English ↔ Arabic Translation with Model Selection")

    # Text input
    text_to_translate = st.text_area("Enter text to translate:", "Hello, how are you?")

    # Model selection dropdown
    model_name = st.selectbox(
        "Choose a translation model:",
        ["Helsinki-NLP/opus-mt-en-ar", "Helsinki-NLP/opus-mt-ar-en", "facebook/m2m100_418M"]
    )

    # Translate button
    if st.button("Translate"):
        if text_to_translate:
            translated_text = translate_text(text_to_translate, model_name)
            st.success(f"Translated Text: {translated_text}")
        else:
            st.warning("Please enter some text to translate.")

if __name__ == "__main__":
    main()