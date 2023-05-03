import streamlit as st
from utils import  generate_sql, max_response
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

st.set_page_config(page_title="SQL Generator",layout='wide')
#,page_icon='assets/logo.png'
dbtypeSelected=None
with st.sidebar:
    #st.image('assets/logo.png',width=270,use_column_width=False)
    st.title("About Me:")
    st.subheader("Hi, I am Rafay :wave:")
    st.write("I am a software engineer and a ML enthusiast. I am passionate about building products and solving problems.")
    st.write("Find me on [Github](https://github.com/rafayqayyum) and [LinkedIn](https://www.linkedin.com/in/rafayqayyum/)")
    st.write("This is a simple text summarizer app built using [OpenAI](https://openai.com/) and [Streamlit](https://streamlit.io/).")
    st.write("You can find the source code [here](https://github.com/Rafayqayyum/Text-Summarizer)")

with st.container():
    st.title("SQL Generator")
    st.subheader("This app generates SQL queries from natural language.")
    
    db_type=None
    db_type = st.selectbox("Select the database type: ",["MySQL","PostgreSQL","SQL Server","Oracle",'MariaDB','SQLite'])
    
    # take schema from file
    file=st.file_uploader("Upload schema file:",type=['sql','txt'],key='schemaFile')
    
    
    text = st.text_area(label='Enter the natural language query:',height=100,key='inputText')
    
    if st.button("Generate SQL"):
        if db_type!=None and file!=None and file!="" and text!="":
            filename=convert_to_file(file)
            schema=read_file(filename)
            # generate sql highlight code and sql keywords
            status,sql,token_discarded= generate_sql("Schema: "+schema+"\n"+text,db_type)
            if status:
                # display sql query and highlight code and sql keywords
                st.subheader("SQL Query:")
                # show sql query and format it as Select, From, Where, Group By, Order By etc on new lines
                sql_formatted=sql.replace('SELECT','\nSELECT').replace('FROM','\nFROM').replace('WHERE','\nWHERE').replace('GROUP BY','\nGROUP BY').replace('ORDER BY','\nORDER BY').replace('LIMIT','\nLIMIT').replace('HAVING','\nHAVING')

                st.code(sql_formatted,language='sql')
            elif sql==None:
                st.error("Error generating SQL query.")
            else:
                st.error(sql)
        elif db_type==None:
            st.error("Please provide Database type.")
        elif file==None or file=="":
            st.error("Please provide schema file.")
        elif text=="":
            st.error("Please provide natural language query.")
        else:   
            st.error("Error generating SQL query.")
            

