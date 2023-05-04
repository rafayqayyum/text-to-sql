import streamlit as st
from utils import  generate_schema, max_response
from sql_keywords import reserved_words
import random
# convert ByteIO to file


def convert_to_file(file):
    with open(file.name, "wb") as f:
        f.write(file.getbuffer())
    return file.name

def read_file(filename):
    with open(filename, "r") as f:
        return f.read()

st.set_page_config(page_title="Schema Generator",layout='wide')
#,page_icon='assets/logo.png'
dbtypeSelected=None
with st.sidebar:
    #st.image('assets/logo.png',width=270,use_column_width=False)
    st.title("About Me:")
    st.subheader("Hi, I am Rafay :wave:")
    st.write("I am a software engineer and a ML enthusiast. I am passionate about building products and solving problems.")
    st.write("Find me on [Github](https://github.com/rafayqayyum) and [LinkedIn](https://www.linkedin.com/in/rafayqayyum/)")
    st.write("This is a simple text summarizer app built using [OpenAI](https://openai.com/) and [Streamlit](https://streamlit.io/).")
    st.write("You can find the source code [here](https://github.com/Rafayqayyum/text-to-sql)")

with st.container():
    st.title("Schema Generator")
    st.subheader("This app generates Database Schemas from natural language.")
    db_type=None
    db_type = st.selectbox("Select the database type: ",["MySQL","PostgreSQL","SQL Server","Oracle",'MariaDB','SQLite'],key='db_type_schema')
    text = st.text_area(label='Explain in detail what database schema you want to generate:',key='text_schema')

    
    if st.button("Generate SQL",key='generate_sql_schema'):
        if db_type!=None and text!="":
            # generate sql highlight code and sql keywords
            status,schema,tokens_discarded=generate_schema(text,dbtype=db_type)
            if status:
                # display sql query and highlight code and sql keywords
                st.subheader("SQL Query to generate schema:")
                # show sql query and format it as Select, From, Where, Group By, Order By etc on new lines
                st.code(schema,language='sql')
            elif schema==None:
                st.error("Error generating SQL query.")
            else:
                st.error(schema)
        elif db_type==None:
            st.error("Please provide Database type.")
        elif text=="":
            st.error("Please provide natural language query.")
        else:   
            st.error("Error generating SQL query.")
                

# Footer section    
with st.container():
    st.markdown("<h4><details><summary>Example</summary><p><ul><li>" + "I want to create a database schema for a blog website. The blog website has users, posts, comments, and tags. A user can have many posts and comments. A post can have many comments and tags. A comment can have many tags. A tag can have many posts and comments."+ "</li></ul></p></details></h4>", unsafe_allow_html=True)
    
    
    
    
