# Gemini SQL Query Generator

A Streamlit app that uses Google's Gemini API to convert natural language questions into SQL queries and retrieve data from an SQLite database.

## Setup

1. **Install Dependencies**:
   ```bash
   pip install streamlit python-dotenv google-generativeai

   Set Up Environment Variables:

Create a .env file in the root directory of your project.

Add your Google API key to the .env file:

plaintext
Copy
GOOGLE_API_KEY=your_google_api_key_here
Replace your_google_api_key_here with your actual Google API key.

Prepare the Database:

Ensure you have an SQLite database named student.db with a table STUDENT containing the following columns:

NAME (TEXT)

CLASS (TEXT)

SECTION (TEXT)

MARKS (INTEGER)

Usage
Run the App:

bash
Copy
streamlit run app.py
Ask Questions:

Enter a natural language question in the input box (e.g., "How many students are in class X?").

Click the "Ask the question" button.

View the generated SQL query and the retrieved data.

Example Questions
"How many students are in class X?"

"List all students with marks greater than 80."

"Tell me all the students in section A."
