import streamlit as st
import requests

st.set_page_config(page_title="MyGrammarAI - Text Correction", page_icon="📝", layout="centered")
st.title("📝 MyGrammarAI - Text Correction")
st.write("Enter your text below and get spelling and grammar corrections.")

text = st.text_area("Enter your text here:")

if st.button("Correct Text") and text:
    try:
        response = requests.post(
            "http://localhost:8081/v2/check",
            data={
                "text": text,
                "language": "en-US"
            }
        )

        print("Raw response:", response.text)

        result = response.json()
        matches = result.get("matches", [])

        if not matches:
            st.success("✅ No errors found!")
        else:
            for match in matches:
                message = match.get("message", "")
                offset = match.get("offset", 0)
                length = match.get("length", 0)
                context_text = text[offset:offset + length]
                replacements = match.get("replacements", [])

                replacement = replacements[0]["value"] if replacements else "No suggestion"
                st.error(f"❌ {context_text} → ✅ {replacement} — {message}")

    except requests.exceptions.JSONDecodeError:
        st.error("❌ Couldn't decode JSON. Make sure the LanguageTool server is running and returning proper data.")
    except Exception as e:
        st.error(f"❌ Unexpected error: {str(e)}")
