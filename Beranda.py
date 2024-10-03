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

st.title("Desa Cibiru Wetan")

st.write("## Selamat datang! 👋")

st.write("Dashboard ini menyediakan data kewilayahan dan karakteristik penduduk di Desa Cibiru Wetan, Kecamatan Cileunyi, Kabupaten Bandung, Jawa Barat.")

st.write("## Profil Desa Cibiru Wetan")

### Import Data Lengkap
url = 'https://docs.google.com/spreadsheets/d/10TvMMPQnOEKG8gABZZw2LXAK1XDHsU17oGsXkhiORdA/edit?gid=0#gid=0'
conn  = st.experimental_connection("gsheets", type=GSheetsConnection)
datadesa = conn.read(spreadsheet=url)
type(datadesa)
st.dataframe("datadesa")

import pydeck as pdk

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

st.write("👈 Pilih menu yang diinginkan.")
