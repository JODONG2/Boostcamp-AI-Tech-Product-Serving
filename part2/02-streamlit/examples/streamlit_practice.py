import streamlit as st
from streamlit import cache
import pandas as pd 
import numpy as np 
import time 

st.title("Title")
st.header("Header")
st.subheader("subheader") 

st.write("Write Something")

if st.button("if you click this button"):
    st.write("watch this")

if st.button("if you click this button2"):
    st.write("watch this twice")
    st.write("watch this twice")

checkbox_btn = st.checkbox('checkbox button')

if checkbox_btn:
    st.write("CHECK!")

checkbox_btn2= st.checkbox('checkbox button2 default = check', value = True)
if checkbox_btn2:
    st.write("when did you see this?")

#st.write:보여줄 수 있는것이면 어떤 것이든 보여줌 ?! 

df = pd.DataFrame({
    'first column':[1,2,3,4], 
    'second column' : [10,20,30,40,] 
})

st.markdown("=====")

st.write(df)
st.dataframe(df)
st.table(df)

st.dataframe(df.style.highlight_max(axis=0)) 
st.dataframe(df.style.highlight_max(axis=1)) 

st.table(df.style.highlight_max(axis=0)) 


st.metric("My metric",42,2)
st.metric("My second metric", 40,-2)
st.json(df.to_json()) 


chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
    )

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000,2)/[50,50],
    columns=['lat','lon'] 
)

st.map(map_data)

selected_item = st.radio("Radio part", ("A",'B','C')) 

if selected_item == "A" :
    st.write("you select A")

elif selected_item == "B" :
    st.write("you select B")

elif selected_item == "C" :
    st.write("you select C")

option_selected = st.selectbox("Please select in selectbox!", ('J','H','D')) 

st.write("you selected: ", option_selected)

multi_select = st.multiselect('Please select something in multi selectbox!', ['A','B','C','D','E']) 

st.write("you selected :", multi_select)

values = st.slider("select a range of values", 0.0, 100.0 ,(50.0,52.0))
st.write("Values:", (values[-1]+values[0]) /2)


text_input = st.text_input("텍스트를 입력해주세요")
st.write(text_input) 
password_input = st.text_input("암호를 입력해주세요", type = "password")
st.write(password_input)
number_input = st.number_input("숫자를 입력해주세요") 
st.write(number_input) 
st.date_input("날짜를 입력하세요") 
st.time_input("시간을 입력하세요") 
st.caption("This is caption")
st.code("a=123")
st.latex("\int a x^2 \,dx") 

#원래 있던 메소드에 sidebar를 적용하면 sidebar에 보이게 됨 
sidebar_button = st.sidebar.button("sidebar button!")
if sidebar_button :
    st.sidebar.write("Hello Sidebar!")

col1, col2, col3, col4 = st.columns(4) 

col1.write("hello i'm co1")
col2.write("hello i'm co2")
col3.write("hello i'm co3")
col4.write("hello i'm co4")

with st.sidebar.expander("please click here!"):
    with st.spinner("Please wait.."):
        time.sleep(5) 
        st.write("Thank you")

st.success("Success")
st.info("Info")
st.warning("Warning")
st.error("Error message") 

with st.form(key="입력 form"):
    username = st.text_input("User name") 
    password = st.text_input("password", type="password") 
    st.form_submit_button("login") 

st.write(username , password)

st.title('Counter Example without session state') 

count_value = 0 
increment = st.button("Increment")
if increment:
    count_value+=1
decrement = st.button('Decrement') 
if decrement:
    count_value-=1 

st.write("Count: ", count_value)


st.title('Counter Example with session state') 

if 'count' not in st.session_state:
    st.session_state.count = 0
increment2 = st.button("Increment2")
if increment2:
    st.session_state.count+=1
decrement2 = st.button('Decrement2') 
if decrement2:
    st.session_state.count-=1 

st.write("Count: ", st.session_state.count)


DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data= pd.read_csv(DATA_URL, nrows=nrows)
    lowercase=lambda x : str(x).lower()
    data.rename(lowercase,axis='columns', inplace=True) 
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

load_data(1000)