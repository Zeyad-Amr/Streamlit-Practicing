import streamlit as st
import pandas as pd
import time
from matplotlib import pyplot as plt
import numpy as np

# Custom Style (Removing Hamburger & Footer)
st.markdown("""
<style>
.css-1rs6os.edgvbvh3
{
    visibility: hidden;
}
.css-1lsmgbg.egzxvld0
{
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# paragraphs elements
st.title("Zeyad Amr")
st.header("Software Engineer")
st.subheader("Mobile App Developer")
st.text("Hello, World!")

# markdown elements
st.markdown("**Hello**, *World!*")
st.markdown("> # **Hello**, *World!*")
st.markdown("1. First")
st.markdown("2. Second")
st.markdown("`code`")
st.markdown("---")
st.markdown("[Click Me](https://www.youtube.com/)")

# latex element (latex syntax) => all symbols & math functions
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")

# json element
json = {"name": "Zeyad Amr", "Age": 23, "Salary": "20,000$"}
st.json(json)

# code element
code = """
print(Hello, World!)
def fun(a,b):
    return a+b;
    """
st.code(code, language="python")

# write allow you to put any of the above formulas (markdown, code, latex, etc..)
st.write("### Header")

# tabel
tabel = pd.DataFrame(
    {"Column 1": [1, 2, 3, 4, 5, 6, 7, 8, 9], "Column 2": ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],
     "Column 3": ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii'],
     "Column 4": ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']})
st.table(tabel)
st.dataframe(tabel)

# image
st.image("img.jpg", caption="This is my image", width=500)

# audio
st.audio("audio.mp3")

# video
st.video("video.mp4")


# checkbox
def on_change_checkbox():
    print("changed, ")


state = st.checkbox("Checkbox 1", value=True, on_change=on_change_checkbox, key="checker")

if state:
    st.write("Checked")
else:
    pass

# radio
radio_btn = st.radio("select from radio", options=(1, 2, 3))
st.write(radio_btn)

# select
select_box_val = st.selectbox("select from radio", options=(1, 2, 3))
st.write(select_box_val)

# multi select
multiselect_val = st.multiselect("select from radio", options=(1, 2, 3))
st.write(multiselect_val)


# button
def btn_click():
    print("Button Clicked")


st.button("Click Me", on_click=btn_click())

# file upload
images = st.file_uploader("Upload file", type=["png", "jpg"], accept_multiple_files=True)
if images is not None:
    for i in images:
        st.image(i)
# slider
slider_val = st.slider("This is slider", min_value=50, max_value=150, value=100)
st.write(slider_val)

# text input
txt_input_val = st.text_input("Enter your course title", max_chars=100)
st.write(txt_input_val)

# text area
txt_area_val = st.text_area("Enter in the txt area")
st.write(txt_area_val)

# date
date_val = st.date_input("Enter date")
st.write(date_val)

# time
time_val = st.time_input("Enter time")
st.write(time_val)

# progress bar
bar = st.progress(10)
# for i in range(10):
#     bar.progress((i + 1) * 10)
#     time.sleep(1)

# form
form = st.form("Form 1")
form.text_input("Name")
form.text_input("Age")
form.form_submit_button("Submit")

# custom form
with st.form("Form 2"):
    col1, col2 = st.columns(2)
    col1.text_input("Name")
    col2.text_input("Age")
    day, month, year = st.columns(3)
    day.text_input("day")
    month.text_input("month")
    year.text_input("year")
    s_state = st.form_submit_button("Submit")

# warning, success, error
st.warning("Warning!")
st.success("Success!")
st.error("Error")

# sidebar
# st.sidebar.write("This is sidebar")
# radio_bar_val=st.sidebar.radio("Select any graph", options=("Line", "Bar", "H-Bar"))

# graph
fig = plt.figure()
plt.style.use("https://raw.githubusercontent.com/dhaitz/matplotlib-stylesheets/master/pitayasmoothie-dark.mplstyle")
x = np.linspace(0, 10, 200)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x), '--')
st.write(fig)

# Columns
col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12 = st.columns(12)
col3.write("Hi,")
col5.write("Zeyad")
col7.write("Amr")
col9.write("Fekry")
