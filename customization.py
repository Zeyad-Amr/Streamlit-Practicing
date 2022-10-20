import json

import streamlit as st
import streamlit.components.v1 as com
from streamlit_lottie import st_lottie

# custom HTML & CSS
with open("style.css") as source:
    style = source.read()
    st.markdown(f"<style>{style}</style>", unsafe_allow_html=True)
com.html(f"""
<style>
{style}
</style>
<div>
    <h1 class="heading">
    This is my header
    </h1>
    <p>
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.Lorem Ipsum is simply dummy text of the printing and typesetting industry.
    </p>
</div>
""", height=400, scrolling=True)

st.markdown("<h1>Title of the article</h1>", unsafe_allow_html=True)
st.text("It's on Friday")
st.markdown("<h1>Title of the article</h1>", unsafe_allow_html=True)

# animations
com.iframe("https://embed.lottiefiles.com/animation/123159")

with open("./samples/123760-cat-sneaking.json") as source:
    animation=json.load(source)

st_lottie(animation)