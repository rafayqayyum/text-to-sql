# Text to SQL Converter App
This app allows users to convert text to SQL queries using the OpenAI GPT3-turbo. It also features a user-friendly interface built with Streamlit. 

# Installation
1. Clone the repository
```git clone https://github.com/Rafayqayyum/text-to-sql```
2. Install the requirements
```pip install -r requirements.txt```
3. Sign up for an OpenAI API key [here](https://platform.openai.com/signup/)
4. Add your OpenAI API key to the environment variable by exporting it in your terminal:
``` export OPENAI_API_KEY='YOUR_API_KEY'```

# Usage
1. Run the app
```streamlit run main.py```
2. Select the database type you want to query
3. Provide the schema of the database
4. Provide the text you want to convert to SQL
5. Click the button to convert the text to SQL

