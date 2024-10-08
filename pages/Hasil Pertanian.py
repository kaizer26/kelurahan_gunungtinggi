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
pt23 = pt23.iloc[0:65,0:4]
pt23.index = list(pt23.iloc[0:65,0])
pt23 = pt23.iloc[0:65,1:4]

import altair as alt
st.write('# Luas Lahan Pertanian dan Perkebunan Berdasarkan Jenis Produksi')
data = pd.melt(lahan23.reset_index(), id_vars=["index"])
# Horizontal stacked bar chart
chart = (
    alt.Chart(data)
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index", type="nominal", title="",sort="descending"),
        color=alt.Color("variable", type="nominal", title=""),
    )
)
st.altair_chart(chart, use_container_width=True)   

st.write('# Luas Lahan Tanaman Pangan Berdasarkan Komoditas')
datatp1 = pt23.iloc[0:30,0]
datatp1 = pd.melt(datatp1.reset_index(), id_vars=["index"])
# Horizontal stacked bar chart
charttp1 = (
    alt.Chart(datatp1)
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index", type="nominal", title="",sort="descending"),
        color=alt.Color("variable", type="nominal", title=""),
    )
)
datatp2 = pt23.iloc[0:30,1]
datatp2 = pd.melt(datatp2.reset_index(), id_vars=["index"])
# Horizontal stacked bar chart
charttp2 = (
    alt.Chart(datatp2)
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index", type="nominal", title="",sort="descending"),
        color=alt.Color("variable", type="nominal", title=""),
    )
)

tp1,tp2 = st.columns((1,1))
tp1.altair_chart(charttp1)   
tp2.altair_chart(charttp2)   

with st.sidebar:
    st.image('https://www.bpskotabaru.com/desacantik/public/images/Logo%20DESCAN_1_002.png',width=100)
    st.header("Dashboard Data Fasilitas Umum Desa Cibiru Wetan")
    st.caption("""Data fasilitas umum ini menyediakan data fasilitas yang dapat diakses masyarakat, meliputi fasilitas pendidikan, kesehatan, perbankan, dan lainnya di Desa Cibiru Wetan, Kecamatan Cileunyi, Kabupaten Bandung, Jawa Barat.""")
