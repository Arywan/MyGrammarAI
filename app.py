import streamlit as st
from utils.text_cleaner import clean_text
from utils.spell_checker import correct_spelling
from utils.grammar_checker import correct_grammar

st.title("📝 MyGrammarAI - Text Correction")
st.write("Enter your text below and get spelling and grammar corrections.")

user_input = st.text_area("Enter your text here:", "")

if st.button("Correct Text"):
    cleaned_text = clean_text(user_input)
    spelling_corrected = correct_spelling(cleaned_text)
    grammar_corrected = correct_grammar(spelling_corrected)

    st.subheader("✅ Corrected Text:")
    st.write(grammar_corrected)
