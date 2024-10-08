import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.set_page_config(
    page_title="Hasil Pertanian",
    page_icon="🌴",
)

#this is the header
t1, t2 = st.columns((0.25,1))

t1.image('https://www.desawisata-cibiruwetan.com/wp-content/uploads/2024/09/icon-logo-dewi-warna-600x721.png', width = 120)
t2.title("Desa Cibiru Wetan")
t2.write("**Hasil Pertanian dan Perkebunan**")
t2.markdown(" **website:** https://cibiruwetan.desa.id **| email:** desawisatacibiruwetan@gmail.com")

url10='https://docs.google.com/spreadsheets/d/15sfFQbVZUmseAfOv70EXI4pe3wUusL9OvfeOex43ueg/edit?usp=sharing'
conn  = st.connection("gsheets", type=GSheetsConnection)
pt23 = conn.read(spreadsheet=url10)
pt23 = pd.DataFrame(pt23)                       #convert ke panda df
lahan23 = pt23.iloc[68:73,0:2]
lahan23.index = list(lahan23.iloc[0:3,0])
#lahan23.columns = "luas"
lahan23 = lahan23.iloc[0:3,1:2]
pt23 = pt23.iloc[0:65,0:3]

st.write(sizes)
st.write(label)

import matplotlib.pyplot as plt
#label = list((lahan23.index))
#sizes = list(lahan23.iloc[0:3,0])
import matplotlib.pyplot as plt

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels)

#st.bar_chart(lahan23)


with st.sidebar:
    st.image('https://www.bpskotabaru.com/desacantik/public/images/Logo%20DESCAN_1_002.png',width=100)
    st.header("Dashboard Data Fasilitas Umum Desa Cibiru Wetan")
    st.caption("""Data fasilitas umum ini menyediakan data fasilitas yang dapat diakses masyarakat, meliputi fasilitas pendidikan, kesehatan, perbankan, dan lainnya di Desa Cibiru Wetan, Kecamatan Cileunyi, Kabupaten Bandung, Jawa Barat.""")
