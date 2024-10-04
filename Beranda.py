# -- coding: utf-8 --
"""
Created on Wed Oct  4 11:54:31 2023

@author: Asus
"""

import streamlit as st
import pandas as pd
import numpy as np
from streamlit_gsheets import GSheetsConnection

st.set_page_config(
    page_title="Beranda",
    page_icon="🏠",
)
st.title("# Desa Cibiru Wetan")
st.caption("""Dashboard ini menyediakan data kewilayahan dan karakteristik penduduk di Desa Cibiru Wetan, Kecamatan Cileunyi, Kabupaten Bandung, Jawa Barat."""
            )
st.write("## Selamat datang! 👋")
st.write("## Profil Desa Cibiru Wetan")

import pydeck as pdk

with st.sidebar:
    st.header("Gatau")
    st.caption("""hai""")
    chart_data = pd.DataFrame(
       np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
       columns=['lat', 'lon'])

    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=-6.921365801298824,
            longitude=107.72940295582379,
            zoom=14,
            pitch=50,
    )
    )
    )




### Import Data Lengkap
url = 'https://docs.google.com/spreadsheets/d/10TvMMPQnOEKG8gABZZw2LXAK1XDHsU17oGsXkhiORdA/edit?usp=sharing'
conn  = st.experimental_connection("gsheets", type=GSheetsConnection)
datadesa = conn.read(spreadsheet=url)
datadesa = pd.DataFrame(datadesa)                       #convert ke panda df
desa = datadesa.style.hide_index()                      #menyembunyikan nomor tabel
desa.hide_columns()                                     #menyembunyikan header
st.write(desa.to_html(),unsafe_allow_html=True)         #menyembunyikan nomor tabel dari .to_html sampe True)


import folium

# center on Liberty Bell, add marker
m = folium.Map(location=[-6.921365801298824, 107.72940295582379], zoom_start=16)
folium.Marker(
    [-6.921365801298824, 107.72940295582379], popup="Kantor Desa Cibiru Wetan", tooltip="Kantor Desa Cibiru Wetan"
).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m,width=725)

st.write("👈 Pilih menu yang diinginkan.")
