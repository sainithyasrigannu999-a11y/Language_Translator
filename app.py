import streamlit as st
from deep_translator import GoogleTranslator

# Page Title
st.set_page_config(page_title="Language Translator", page_icon="🌍")

st.title("🌍 Language Translation Tool")
st.write("Translate text into multiple languages instantly")

# User Input
text = st.text_area("Enter text to translate")

# Multiple Languages
languages = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Bengali": "bn",
    "Urdu": "ur",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Chinese": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar",
    "Turkish": "tr",
    "Dutch": "nl",
    "Greek": "el",
    "Thai": "th",
    "Vietnamese": "vi",
    "Indonesian": "id",
    "Polish": "pl",
    "Swedish": "sv",
    "Finnish": "fi"
}

# Language Selection
source_lang = st.selectbox(
    "Select Source Language",
    list(languages.keys())
)

target_lang = st.selectbox(
    "Select Target Language",
    list(languages.keys())
)

# Translate Button
if st.button("Translate"):

    if text.strip() == "":
        st.warning("⚠ Please enter some text")

    else:
        try:
            # Translation
            translated = GoogleTranslator(
                source='auto',
                target=languages[target_lang]
            ).translate(text)

            st.success("✅ Translation Completed")

            # Output
            st.text_area(
                "Translated Text",
                translated,
                height=150
            )

            # Copy Section
            st.code(translated)

        except Exception as e:
            st.error(f"Error: {e}")

# Footer
st.markdown("---")
st.write("Made with ❤️ using Streamlit & Google Translator")