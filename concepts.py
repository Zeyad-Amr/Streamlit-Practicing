import streamlit as st
import time


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
