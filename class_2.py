import streamlit as st
import pandas as pd
import pickle


st.set_page_config(layout = "wide", page_title= 'Spam Text Classifier')

def Intro(About):
    st.header()
def data(dataframe):
    st.header()
    
def stats(dataframe):
    st.header('Data Statistics')
    st.write(df.describe())
    st.header('Data Shape')
    st.write(df.shape)
def mod(model):
    model = pickle.load(open('model.pkl', 'rb'))
   

st.sidebar.title('Navigation')
st.sidebar.image('Mail.png', caption = 'Welcome Dear User')
options = st.sidebar.radio('Pages', options = ['Home','Raw Data','Statistics','Model'])
df =pd.read_csv('SPAM text message 20170820 - Data.csv', encoding ='ISO-8859-1')
model = pickle.load(open('model.pkl', 'rb'))


if options == 'Home':
    st.title('Message Classifier App for Spam Detection')
    st.image('Spamtext ima.png', width = 150)
    st.write("The Python-based spam text message classifier highlights the effectiveness of merging natural language processing methods with machine learning algorithms, specifically Support Vector Machines (SVM), to address practical challenges. By accurately distinguishing between spam and authentic messages, this classifier significantly enhances user communication safety and security.Its role in countering the risks linked with spam messages is paramount in today's digital realm, exemplifying its crucial contribution to fostering a safer online environment.")

elif options == 'Raw Data':
    st.title('Data')
    df =pd.read_csv('SPAM text message 20170820 - Data.csv', encoding ='ISO-8859-1')
    st.dataframe(df,use_container_width = True)
   
elif options == 'Statistics':
    stats(df)
    st.write(' This data has 2 columns and 5572 rows')
    
    
elif options == 'Model':
    message = st.text_input('Enter a message')
    click = st.button('Predict message')

# Model Prediction

    if click:
        predicted = model.predict([message])

        if predicted[0]== 'spam':
            st.warning(f'This message is spam: Defend your inbox')
            st.image('spam mail.png', width = 50)
        else:
            st.success(f'This message is authentic (Ham)')
            st.image('Ham mail.png', width = 50)

st.balloons()
