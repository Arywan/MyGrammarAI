## 📄 README.md:


# 📝 MyGrammarAI - Text Correction

**MyGrammarAI** is an AI-powered web application that helps you detect and correct **spelling** and **grammar** mistakes in English text using the power of [LanguageTool](https://languagetool.org/) and Python.

## 🚀 Features

- ✅ Grammar correction using LanguageTool
- ✅ Spelling correction with PySpellChecker
- ✅ Clean and user-friendly web interface using Streamlit
- ✅ Fast, local text checking (no cloud dependency)
- ✅ Easy to install and run

## 🧠 How it works

The app:
1. Takes user input through a Streamlit form
2. Sends the text to a locally running LanguageTool server (`http://localhost:8081/v2/check`)
3. Displays grammar and spelling corrections inline
4. Uses helper functions to clean and process text

## 🛠️ Project Structure



MyGrammarAI/
│
├── app.py                 # Main Streamlit app
├── requirements.txt       # All Python dependencies
│
├── utils/
│   ├── grammar\_checker.py # Grammar correction logic
│   ├── spell\_checker.py   # Spelling correction logic
│   └── text\_cleaner.py    # Text cleaning utilities

````

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Arywan/MyGrammarAI.git
cd MyGrammarAI
````

### 2. Install the dependencies

Use a virtual environment (optional but recommended):

```bash
pip install -r requirements.txt
```

### 3. Run the LanguageTool server

> Make sure you downloaded the LanguageTool server JAR first.

```bash
java "-Djdk.xml.totalEntitySizeLimit=0" -cp languagetool-server.jar org.languagetool.server.HTTPServer --port 8081
```

### 4. Run the app

```bash
streamlit run app.py
```

---

## 📌 Notes

* Make sure Java is installed and added to your system path.
* Works offline with no data sent to external APIs.

## 📄 License

MIT License
© Arywan 2025

