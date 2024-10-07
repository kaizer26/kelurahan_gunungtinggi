import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.set_page_config(
    page_title="Data Kependudukan",
    page_icon=":family:",
)

#this is the header
t1, t2 = st.columns((0.25,1))

t1.image('https://www.desawisata-cibiruwetan.com/wp-content/uploads/2024/09/icon-logo-dewi-warna-600x721.png', width = 120)
t2.title("Desa Cibiru Wetan")
t2.write("**Data Kependudukan**")
t2.markdown(" **website:** https://cibiruwetan.desa.id **| email:** desawisatacibiruwetan@gmail.com")


#this is content
 #st.image('https://www.desawisata-cibiruwetan.com/wp-content/uploads/2023/01/branding-cibiru-wetan-WISATA-1-800x197.png')
st.write("# Piramida Penduduk Tahun 2024")

### Import Data Lengkap
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

st.altair_chart(chart, use_container_width=True)   #bikin piramida chart

st.dataframe(datap2024.iloc[0:16,0:3], use_container_width=True, hide_index=True)   #menampilkan data
### Opsi Download Data
@st.cache_data
def convert_df(datap2024):
    return datap2024.to_csv().encode('utf-8')
csv = convert_df(datap2024)
st.download_button(
    label = "Unduh Data",
    data = csv,
    file_name='download_cibiruwetan.csv',
    mime='text/csv',
    )

url3 = 'https://docs.google.com/spreadsheets/d/196eZm3CzaY1FIapq0nnWBc18dFz0yXxtPrxtlYaqRLc/edit?usp=sharing'
conn  = st.connection("gsheets", type=GSheetsConnection)
datap2023 = conn.read(spreadsheet=url3)
datap2023 = pd.DataFrame(datap2023)                       #convert ke panda df
jp2023=datap2023.iloc[0:16,1:3].sum().sum()

datapiramida2 = datap2023.iloc[0:16,1:3]
jk = list(["Laki-laki","Perempuan"])
datapiramida2.iloc[0:16,0]=-datapiramida2.iloc[0:16,0]
datapiramida2.index = list(datap2023.iloc[0:16,0])
datapiramida2.columns = jk

# Convert wide-form data to long-form
# See: https://altair-viz.github.io/user_guide/data.html#long-form-vs-wide-form-data
data2 = pd.melt(datapiramida2.reset_index(), id_vars=["index"])

# Horizontal stacked bar chart
chart2 = (
    alt.Chart(data2)
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index", type="nominal", title="",sort="descending"),
        color=alt.Color("variable", type="nominal", title=""),
    )
)

st.altair_chart(chart2, use_container_width=True)   #bikin piramida chart

st.dataframe(datap2023.iloc[0:16,0:3], use_container_width=True, hide_index=True)   #menampilkan data
### Opsi Download Data
@st.cache_data
def convert_df(datap2023):
    return datap2023.to_csv().encode('utf-8')
csv2 = convert_df(datap2023)
st.download_button(
    label = "Unduh Data",
    data = csv2,
    file_name='download_cibiruwetan.csv',
    mime='text/csv',
    )
