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
.css-2ykyy6.egzxvld0
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

st.write("---")

# markdown elements
st.markdown("**Hello**, *World!*")
st.markdown("> # **Hello**, *World!*")
st.markdown("1. First")
st.markdown("2. Second")
st.markdown("---")
st.markdown("[Click Me](https://www.youtube.com/)")

st.write("---")

# latex element (latex syntax) => all symbols & math functions
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")

st.write("---")

# json element
json = {"name": "Zeyad Amr", "Age": 23, "Salary": "20,000$"}
st.json(json)

st.write("---")

# code element
code = """
print(Hello, World!)
def fun(a,b):
    return a+b;
    """
st.code(code, language="python")

st.write("---")

# write allow you to put any of the above formulas (markdown, code, latex, etc..)
st.write("### write() func")

st.write("---")

# tabel
tabel = pd.DataFrame(
    {"Column 1": [1, 2, 3, 4, 5, 6, 7, 8, 9], "Column 2": ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],
     "Column 3": ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii'],
     "Column 4": ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']})
st.table(tabel)
st.dataframe(tabel)

st.write("---")

# image
st.image("./samples/img.jpg", caption="This is my image", width=500)

st.write("---")

# audio
st.audio("./samples/audio.mp3")

st.write("---")

# video
st.video("./samples/video.mp4")

st.write("---")


# checkbox
def on_change_checkbox():
    print("changed, ")


state = st.checkbox("Checkbox 1", value=True, on_change=on_change_checkbox, key="checker")

if state:
    st.write("Checked")
else:
    pass

st.write("---")

# radio
radio_btn = st.radio("select from radio", options=(1, 2, 3))
st.write(radio_btn)

st.write("---")

# select
select_box_val = st.selectbox("select from radio", options=(1, 2, 3))
st.write(select_box_val)

st.write("---")

# multi select
multiselect_val = st.multiselect("select from radio", options=(1, 2, 3))
st.write(multiselect_val)

st.write("---")


# button
def btn_click():
    print("Button Clicked")


st.button("Click Me", on_click=btn_click())

st.write("---")

# file upload
images = st.file_uploader("Upload file", type=["png", "jpg"], accept_multiple_files=True)
if images is not None:
    for i in images:
        st.image(i)

st.write("---")

# slider
slider_val = st.slider("This is slider", min_value=50, max_value=150, value=100)
st.write(slider_val)

st.write("---")

# text input
txt_input_val = st.text_input("Enter your course title", max_chars=100)
st.write(txt_input_val)

st.write("---")

# text area
txt_area_val = st.text_area("Enter in the txt area")
st.write(txt_area_val)

st.write("---")

# date
date_val = st.date_input("Enter date")
st.write(date_val)

st.write("---")

# time
time_val = st.time_input("Enter time")
st.write(time_val)

st.write("---")

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

st.write("---")

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

st.write("---")

# warning, success, error
st.warning("Warning!")
st.success("Success!")
st.error("Error")

# sidebar
# st.sidebar.write("This is sidebar")
# radio_bar_val=st.sidebar.radio("Select any graph", options=("Line", "Bar", "H-Bar"))
st.write("---")

slider_val = st.slider("This is slider", min_value=0, max_value=50, value=0)

st.write("---")
# graph
fig = plt.figure()
plt.style.use("https://raw.githubusercontent.com/dhaitz/matplotlib-stylesheets/master/pitayasmoothie-dark.mplstyle")
x = np.linspace(0, slider_val, 200)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x), '--')
st.write(fig)

st.write("---")

# Columns
st.write("Columns")
col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12 = st.columns(12)
col3.write("Hi,")
col5.write("Zeyad")
col7.write("Amr")
col9.write("Fekry")

st.write("---")

#### Data Visualizer ####
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
