# Gemini SQL Query Generator

A Streamlit app to convert natural language questions into SQL queries using Google's Gemini API.

## Setup

1. Install dependencies:
   ```bash
   pip install streamlit python-dotenv google-generativeai
Add your Google API key to .env:

plaintext
Copy
GOOGLE_API_KEY=your_google_api_key_here
Ensure student.db has a STUDENT table with columns: NAME, CLASS, SECTION, MARKS.

Usage
Run the app:

bash
Copy
streamlit run app.py
Ask questions like:

"How many students are in class X?"

"List students with marks > 80."
