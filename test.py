import chunk
import streamlit as st
from pydub import AudioSegment, silence

uploaded_file = st.file_uploader("Audio", type=['.mp3', '.wav'])

if uploaded_file:
    # To read file as bytes:
    # bytes_data = uploaded_file.read()
    # st.write(bytes_data)

    # # # Can be used wherever a "file-like" object is accepted:
    # dataframe = pd.read_csv(uploaded_file, delim_whitespace=True)
    # audio_segment = AudioSegment.from_file(uploaded_file)
    # chunks = silence.split_on_silence(
    #     audio_segment, min_silence_len=500, silence_thresh=audio_segment.dBFS-20, keep_silence=100)
    # for chunk in chunks:
    #     print(chunk)
    audio_bytes = uploaded_file.read()
    st.audio(audio_bytes, format='audio/wav')

    # play = st.checkbox("Play")
    # x = st.slider("secs", min_value=0, max_value=269)
    # if play:
    #     # audio
    #     st.audio(audio_segment,   format="audio/wav", start_time=x)
    # else:
    #     # audio
    #     st.audio("./samples/250-milliseconds-of-silence.mp3",
    #              format="audio/wav", start_time=x)

    # st.write(audio_segment)
