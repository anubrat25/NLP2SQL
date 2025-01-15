Gemini SQL Query Generator
A Streamlit app that uses Google's Gemini API to convert natural language questions into SQL queries and retrieve data from an SQLite database.

Setup
Install Dependencies:

bash
Copy
pip install streamlit python-dotenv google-generativeai
Set Up Environment Variables:

Create a .env file and add your Google API key:

plaintext
Copy
GOOGLE_API_KEY=your_google_api_key_here
Prepare the Database:

Ensure you have an SQLite database named student.db with a table STUDENT containing columns: NAME, CLASS, SECTION, and MARKS.

Usage
Run the App:

bash
Copy
streamlit run app.py
Ask Questions:

Enter a question (e.g., "How many students are in class X?").

View the generated SQL query and results.

Example Questions
"List all students in section A."

"Show students with marks greater than 80."
