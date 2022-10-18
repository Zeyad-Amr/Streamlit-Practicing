import streamlit as st
import pandas as pd
import time
from matplotlib import pyplot as plt
import numpy as np

# Data Visualizer

st.markdown("<h1 style='text-align: center;'>Data Visualizer</h1>", unsafe_allow_html=True)
files_names = list()
figure = plt.figure()


def date_converter(date_col):
    result = list()
    values = date_col.values
    for value in values:
        result.append(str(value).split("T")[0])
    return result;


# file upload
files = st.file_uploader("Upload Mulitple Files", type=["xlsx"], accept_multiple_files=True)
if files:
    for file in files:
        files_names.append(file.name)
    selected_files = st.multiselect("Select Files", options=files_names)
    if selected_files:
        option = st.radio("Select Entity Against Date", options=["None", "GPU", "CPU", "Mouse", "Keyboard", "Casing"])
        if option != "None":
            for file in files:
                if file.name in selected_files:
                    data = pd.read_excel(file, index_col=0)
                    item = list(data[option])
                    dates = date_converter(data["Date"])
                    index = np.arange(len(dates))
                    plt.xticks(index, dates)
                    plt.gcf().autofmt_xdate()
                    plt.xlabel("Date")
                    plt.ylabel(option)
                    plt.title(option + " Chart")
                    plt.grid(True)
                    plt.plot(index, item, label=file.name, color="black", )
                    plt.scatter(index, item, marker='o', edgecolors="red", color="yellow")
            st.write(figure)

st.write("---")


# Call Backs properties
def printer(name):
    print(name)


input_val = st.text_input("Enter your name")
s_btn = st.button("Submit")
if s_btn:
    st.checkbox("Want to display your name?", on_change=printer,
                args={input_val, })  # passing args in callback function

st.write("---")

# Session State
st.write("Session State")
text = "😍"
if "click" not in st.session_state:  # for creating "click" variable
    st.session_state.click = False
else:
    if not st.session_state.click:  # checking click
        text = "🤑"
        st.session_state.click = True  # toggling click variable
    else:
        text = "😍"
        st.session_state.click = False  # toggling click variable

st.button(text)

st.write("---")

# caching
st.write("Caching")


@st.cache(suppress_st_warning=True)
def printer():
    st.write("Running")
    time.sleep(5)
    return "Message"


st.write(printer())
