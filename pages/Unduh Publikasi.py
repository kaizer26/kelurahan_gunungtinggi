import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
import geopandas as gpd
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Unduh Publikasi",
    page_icon="📚",
)

urlbuku = 'https://docs.google.com/spreadsheets/d/1iVqggywv8FP8yYlW844D4y5IHQMJagPtdjQCfUucP9M/edit?usp=sharing'
conn  = st.connection("gsheets", type=GSheetsConnection)
publikasi = conn.read(spreadsheet=urlbuku)
publikasi = pd.DataFrame(publikasi)                       #convert ke panda df
#this is the header
t1, t2 = st.columns((0.25,1))

t1.image('logo pemkab tanbu.png', width = 100)
t2.title("Kelurahan Cantik Gunung Tinggi")
t2.markdown(" **Halaman Unduh Publikasi Kelurahan Gunung Tinggi** ")
# Inisialisasi i
i = 0

# Loop melalui data publikasi
while i < len(publikasi):
    # Buat tiga kolom untuk setiap iterasi
    pd1, pd2, pd3 = st.columns((1, 1, 1))

    # Cek untuk kolom pertama
    if i < len(publikasi):
        pd1.image(str(publikasi.iloc[i, 3]))
        pd1.write(str(publikasi.iloc[i, 0]))
        pd1.write("[Unduh](%s)" % str(publikasi.iloc[i, 1]))
    else:
        pd1.write('')

    # Cek untuk kolom kedua
    if i + 1 < len(publikasi):
        pd2.image(str(publikasi.iloc[i + 1, 3]))
        pd2.write(str(publikasi.iloc[i + 1, 0]))
        pd2.write("[Unduh](%s)" % str(publikasi.iloc[i + 1, 1]))
    else:
        pd2.write('')

    # Cek untuk kolom ketiga
    if i + 2 < len(publikasi):
        pd3.image(str(publikasi.iloc[i + 2, 3]))
        pd3.write(str(publikasi.iloc[i + 2, 0]))
        pd3.write("[Unduh](%s)" % str(publikasi.iloc[i + 2, 1]))
    else:
        pd3.write('')

    # Increment i untuk memproses tiga item sekaligus
    i += 3
    
with st.sidebar:
    st.image('desa_cantik.png',width=100)
    st.header("Dashboard Unduh Publikasi Kelurahan Gunung Tinggi")
    st.caption("""Menu Unduh Publikasi menyediakan publikasi yang berisikan kompilasi informasi dan data di Kelurahan Gunung Tinggi, Kecamatan Batulicin, Kabupaten Tanah Bumbu, Kalimantan Selatan.""")
