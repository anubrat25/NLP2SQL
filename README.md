# SQL Query Assistant with Gemini AI

This application is a Streamlit-based web interface that converts natural language questions into SQL queries using Google's Gemini AI. Users can ask questions in plain English about student data, and the app will generate and execute the appropriate SQL query.

## Features

- Natural language to SQL query conversion using Gemini AI
- Interactive web interface built with Streamlit
- SQLite database integration
- Pre-configured student database with sample data

## Prerequisites

- Python 3.7 or higher
- Google Cloud API key with Gemini AI access

## Installation

1. Clone the repository:
```bash
git clone <https://github.com/anubrat25/NLP2SQL.git>
cd <NLP2SQL>
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your Google API key:
```
GOOGLE_API_KEY=your_api_key_here
```

## Database Setup

1. Run the SQL setup script to create and populate the sample database:
```bash
python sql.py
```

This will create a `student.db` file with sample student records.

## Project Structure

- `app.py`: Main Streamlit application file
- `sql.py`: Database initialization script
- `requirements.txt`: List of Python dependencies
- `student.db`: SQLite database file (created after running sql.py)

## Database Schema

The STUDENT table contains the following columns:
- Name (varchar)
- Class (varchar)
- Section (varchar)
- Marks (int)

## Running the Application

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

## Usage

1. Enter your question in natural language in the input field
2. Click the "Ask the question" button
3. The app will:
   - Convert your question to SQL using Gemini AI
   - Execute the query on the database
   - Display the results

Example questions:
- "How many entries of records are present?"
- "Tell me all the students studying in X class?"
- "Show me students who scored above 80 marks"

## Dependencies

- streamlit
- google-generativeai
- python-dotenv
- sqlite3 (built into Python)

## Notes

- The application uses a simple SQLite database for demonstration purposes
- The Gemini AI model is configured to understand questions about the specific student database schema
- Make sure to keep your API key secure and never commit it to version control

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

This project is available under the MIT License.
