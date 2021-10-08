import speech_recognition as sr
import docx
import librosa
import librosa.display
import IPython.display as ipd
import matplotlib.pyplot as plt
import streamlit as st
from datetime import datetime
import time


st.header('Audio Transcribe')

d = datetime.now()
st.write('Date:  ', d.strftime('%Y-%m-%d %H:%M:%S'))

audio_file = st.file_uploader(label='Load file', type="wav")

st.subheader('Listening To An Audio File')
st.audio(audio_file, format='audio/wav')

if audio_file != None:
    def recognizeAudio_google(filename, duration=None):
        r = sr.Recognizer()
        with sr.AudioFile(filename) as source:
          audio = r.record(source, duration=duration)

        return r.recognize_google(audio, language='en')

    res = recognizeAudio_google(audio_file)

    
    sleep_duration = 0
    percent_complete = 0
    progress_bar = st.progress(percent_complete)
    percent_complete += sleep_duration
    time.sleep(sleep_duration)
    progress_bar.progress(percent_complete)
    result = res

    sleep_duration = 0.025

    progress_text = st.empty()
    for percent in range(percent_complete, 101):
        time.sleep(sleep_duration)
        progress_bar.progress(percent)
        progress_text.text(f'Done: {percent}%')
    
    st.header('Transcibed Text')
    st.markdown(res)

file_name = st.text_input(label='File Name For Save :')

if st.button('Save To WORD'):
    mydoc = docx.Document()
    mydoc.add_paragraph(res)
    mydoc.save(f'e:/Transcribe/{file_name}.docx')
    st.subheader('File Saved')
