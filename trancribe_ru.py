import speech_recognition as sr
import docx
import librosa
import librosa.display
import IPython.display as ipd
import matplotlib.pyplot as plt
import streamlit as st
from datetime import datetime
import time


st.header('Расшифровка аудио')

d = datetime.now()
st.write('Дата:  ', d.strftime('%Y-%m-%d %H:%M:%S'))

audio_file = st.file_uploader(label='Загрузите файл', type="wav")

st.subheader('Прослушивание аудио файла')
st.audio(audio_file, format='audio/wav')

if audio_file != None:
    def recognizeAudio_google(filename, duration=None):
        r = sr.Recognizer()
        with sr.AudioFile(filename) as source:
          audio = r.record(source, duration=duration)

        return r.recognize_google(audio, language='ru')

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
        progress_text.text(f"Выполнено: {percent}%")
    
    st.header('Расшифрованный текст')
    st.markdown(res)

file_name = st.text_input(label='Название файла для сохранения:')

if st.button('СОХРАНИТЬ В WORD'):
    mydoc = docx.Document()
    mydoc.add_paragraph(res)
    mydoc.save(f'e:/Transcribe/{file_name}.docx')
    st.subheader('Файл сохранен')
