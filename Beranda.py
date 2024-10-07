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

#this is the header


t1, t2 = st.columns((0.25,1))

t1.image('https://www.desawisata-cibiruwetan.com/wp-content/uploads/2024/09/icon-logo-dewi-warna-600x721.png', width = 120)
t2.title("Desa Cibiru Wetan")
t2.markdown(" **website:** https://cibiruwetan.desa.id **| email:** desawisatacibiruwetan@gmail.com")


#this is content
 #st.image('https://www.desawisata-cibiruwetan.com/wp-content/uploads/2023/01/branding-cibiru-wetan-WISATA-1-800x197.png')
st.write("# Rekap Penduduk Desa Cibiru Wetan")

url2='https://docs.google.com/spreadsheets/d/16AtuoSRO-7SwU8E6jJDNzdoX6S0DyRFkpaduxBhZ748/edit?usp=sharing'
conn  = st.connection("gsheets", type=GSheetsConnection)
datap2024 = conn.read(spreadsheet=url2)
datap2024 = pd.DataFrame(datap2024)                       #convert ke panda df
jp2024=datap2024.iloc[0:16,1:3].sum().sum()

datapiramida = datap2024.iloc[0:16,1:3]
jk = list(["Laki-laki","Perempuan"])
datapiramida.iloc[0:16,0]=-datapiramida.iloc[0:16,0]
datapiramida.index = list(datap2024.iloc[0:16,0])
datapiramida.columns = jk
#st.bar_chart(datapiramida)

import altair as alt
# Convert wide-form data to long-form
# See: https://altair-viz.github.io/user_guide/data.html#long-form-vs-wide-form-data
data = pd.melt(datapiramida.reset_index(), id_vars=["index"])

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

#st.altair_chart(chart, use_container_width=True)   #bikin piramida chart

pd2024laki = int(datap2024.iloc[0:16,1:2].sum().sum())
pd2024pere = int(datap2024.iloc[0:16,2:3].sum().sum())
lakipere2024 = pd.DataFrame({"laki":[pd2024laki],"perempuan":[pd2024pere]})
lakipere2024.columns = list(["Laki-laki","Perempuan"])

m1, m2, m3, m4 = st.columns((1,1,1,1))
m1.metric(label = 'Total KK',value = int(datap2024.iloc[20,1]))
m2.metric(label ='Total Penduduk (jiwa)',value = str(int(jp2024)))
m3.metric(label ='Penduduk Laki-laki',value = "🚹"+str(int(pd2024laki)))
m4.metric(label = 'Penduduk Perempuan',value = "🚺"+str(int(pd2024pere)))
m1.write('')

#import matplotlib.pyplot as plt
#st.pyplot(lakipere2024)

st.write("Berdasarkan data Kementerian Dalam Negeri (Kemendagri), jumlah penduduk Desa Cibiru Wetan pada tahun 2024 semester 1 sebanyak ",int(jp2024)," jiwa dengan penduduk laki-laki sebanyak ",int(pd2024laki)," jiwa dan penduduk perempuan sebanyak",pd2024pere," jiwa.")

import pydeck as pdk
st.write("# Profil Desa Cibiru Wetan")
with st.sidebar:
    st.image('https://www.bpskotabaru.com/desacantik/public/images/Logo%20DESCAN_1_002.png',width=100)
    st.header("Dashboard Desa Cibiru Wetan")
    st.caption("""Dashboard ini menyediakan data kewilayahan dan karakteristik penduduk di Desa Cibiru Wetan, Kecamatan Cileunyi, Kabupaten Bandung, Jawa Barat.""")




### Import Data Lengkap
url = 'https://docs.google.com/spreadsheets/d/10TvMMPQnOEKG8gABZZw2LXAK1XDHsU17oGsXkhiORdA/edit?usp=sharing'
conn  = st.connection("gsheets", type=GSheetsConnection)
datadesa = conn.read(spreadsheet=url)
datadesa1 = pd.DataFrame(datadesa.iloc[0:12,0:2])                       #convert ke panda df
desa = datadesa1.style.hide()                      #menyembunyikan nomor tabel
#desa.hide_columns()                                     #menyembunyikan header
st.write(desa.to_html(),unsafe_allow_html=True)         #menyembunyikan nomor tabel dari .to_html sampe True)

st.write("# Peta Lokasi Desa Cibiru Wetan")
mapdata = pd.DataFrame([
    {
        'site': 'Big Ben',
        'attraction_type': 'Clock Tower',
        'lat': -6.921365801298824,
        'lng': 107.72940295582379
    }
])
color_lookup = pdk.data_utils.assign_random_colors(mapdata['attraction_type'])
# Assign a color based on attraction_type
mapdata['color'] = mapdata.apply(lambda row: color_lookup.get(row['attraction_type']), axis=1)

st.pydeck_chart(pdk.Deck(
       map_style="road",
       initial_view_state=pdk.ViewState(
           latitude=-6.921365801298824,
            longitude=107.72940295582379,
            zoom=14,
            pitch=50,
)
)
)

datadesa2 = pd.DataFrame(datadesa.iloc[12:18,0:2])                       #convert ke panda df
desa2 = datadesa2.style.hide()                      #menyembunyikan nomor tabel
#desa2.hide_columns()                                     #menyembunyikan header
st.write(desa2.to_html(),unsafe_allow_html=True)         #menyembunyikan nomor tabel dari .to_html sampe True)

st.write("# Kunjungi Kami")
url_ig = 'https:/instagram.com/desa_cibiruwetan'
url_yt = 'https://youtube.com/@desa_cibiruwetan?si=js2kX36jVxCMI64F'
st.write(" **instagram** : [desa_cibiruwetan](%s)" % url_ig)
st.write(" **youtube** : [Humas Desa Cibiru Wetan](%s)" % url_yt)



