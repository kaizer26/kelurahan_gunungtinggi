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
#t2.markdown(" **website:** https://cibiruwetan.desa.id **| email:** desawisatacibiruwetan@gmail.com")


#this is content
st.write("# Struktur Penduduk Tahun 2024")

##data penduduk
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

st.write("# Struktur Penduduk Tahun 2023")
url3 = 'https://docs.google.com/spreadsheets/d/196eZm3CzaY1FIapq0nnWBc18dFz0yXxtPrxtlYaqRLc/edit?usp=sharing'
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

#data pekerjaan
url4 = 'https://docs.google.com/spreadsheets/d/1wjTtBvxU2a-x0LGEfkX7IaQcN1DhkzJ4ZqRk1DYO8Yw/edit?usp=sharing'
kerja23 = conn.read(spreadsheet=url4)
kerja23 = pd.DataFrame(kerja23)
stkerja23 = kerja23.iloc[16:18,0:4]
kerja23 = kerja23.iloc[0:13,0:4]

st.write('# Status Pekerjaan Angkatan Kerja Tahun 2023')
stkerja23.index = list(stkerja23.iloc[0:2,0])
stkerja23 = stkerja23.iloc[0:2,1:4]

datatp1 = stkerja23.iloc[0:2,0]
datatp1 = pd.melt(datatp1.reset_index(), id_vars=["index"])
# Horizontal stacked bar chart
charttp1 = (
    alt.Chart(datatp1,title=alt.TitleParams('Laki-laki', anchor='middle'))
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index", type="nominal", title="",sort="descending"),
        color=alt.Color("variable", type="nominal", title="",legend=None),
    )
)
datatp2 = stkerja23.iloc[0:2,1]
datatp2 = pd.melt(datatp2.reset_index(), id_vars=["index"])
# Horizontal stacked bar chart
charttp2 = (
    alt.Chart(datatp2,title=alt.TitleParams('Perempuan', anchor='middle'))
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index", type="nominal", title="",sort="descending"),
        color=alt.Color("variable", type="nominal", title="",legend=None),
    )
)

tp1,tp2 = st.columns((1,1))
tp1.altair_chart(charttp1)   
tp2.altair_chart(charttp2)   

st.dataframe(stkerja23,use_container_width=True)

st.write('# Pekerjaan Penduduk Tahun 2023')
kerja23.index = list(kerja23.iloc[0:13,0])
kerja23 = kerja23.iloc[0:13,1:4]
#st.bar_chart(kerja23.iloc[0:13,0].T)

datatp1 = kerja23.iloc[0:13,0]
datatp1 = pd.melt(datatp1.reset_index(), id_vars=["index"])
# Horizontal stacked bar chart
charttp1 = (
    alt.Chart(datatp1,title=alt.TitleParams('Laki-laki', anchor='middle'))
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index", type="nominal", title="",sort="descending"),
        color=alt.Color("variable", type="nominal", title="",legend=None),
    )
)
datatp2 = kerja23.iloc[0:13,1]
datatp2 = pd.melt(datatp2.reset_index(), id_vars=["index"])
# Horizontal stacked bar chart
charttp2 = (
    alt.Chart(datatp2,title=alt.TitleParams('Perempuan', anchor='middle'))
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index", type="nominal", title="",sort="descending"),
        color=alt.Color("variable", type="nominal", title="",legend=None),
    )
)

tp1,tp2 = st.columns((1,1))
tp1.altair_chart(charttp1)   
tp2.altair_chart(charttp2)   

st.dataframe(kerja23,use_container_width=True)

st.write('# Pendidikan Tenaga Kerja Tahun 2023')
url5 = 'https://docs.google.com/spreadsheets/d/1BaFB0sFvKIv_e3G8LX_6su-vwDUJKhZLWeE1knU5bT8/edit?usp=sharing'
pdik23 = conn.read(spreadsheet=url5)
pdik23 = pd.DataFrame(pdik23)
pdik23 = pdik23.iloc[0:6,0:3]
pdik23.index = list(pdik23.iloc[0:6,0])
pdik23 = pdik23.iloc[0:6,1:3]

datatp1 = pdik23.iloc[0:6,0]
datatp1 = pd.melt(datatp1.reset_index(), id_vars=["index"])
# Horizontal stacked bar chart
charttp1 = (
    alt.Chart(datatp1,title=alt.TitleParams('Laki-laki', anchor='middle'))
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index", type="nominal", title="",sort="descending"),
        color=alt.Color("variable", type="nominal", title="",legend=None),
    )
)
datatp2 = pdik23.iloc[0:6,1]
datatp2 = pd.melt(datatp2.reset_index(), id_vars=["index"])
# Horizontal stacked bar chart
charttp2 = (
    alt.Chart(datatp2,title=alt.TitleParams('Perempuan', anchor='middle'))
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index", type="nominal", title="",sort="descending"),
        color=alt.Color("variable", type="nominal", title="",legend=None),
    )
)

tp1,tp2 = st.columns((1,1))
tp1.altair_chart(charttp1)   
tp2.altair_chart(charttp2)   

st.dataframe(pdik23,use_container_width=True)

st.write('# Etnis Penduduk Tahun 2023')
url6 = 'https://docs.google.com/spreadsheets/d/1lrJgC7IgzaYUElTEzhix6m2Wz-u-ThN1WXsGRHgMv8s/edit?usp=sharing'
et23 = conn.read(spreadsheet=url6)
et23 = pd.DataFrame(et23)
et23.index = list(et23.iloc[0:21,0])
et23 = et23.iloc[0:21,1:3]

datatp1 = et23.iloc[0:21,0]
datatp1 = pd.melt(datatp1.reset_index(), id_vars=["index"])
# Horizontal stacked bar chart
charttp1 = (
    alt.Chart(datatp1,title=alt.TitleParams('Laki-laki', anchor='middle'))
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index", type="nominal", title="",sort="descending"),
        color=alt.Color("variable", type="nominal", title="",legend=None),
    )
)
datatp2 = et23.iloc[0:21,1]
datatp2 = pd.melt(datatp2.reset_index(), id_vars=["index"])
# Horizontal stacked bar chart
charttp2 = (
    alt.Chart(datatp2,title=alt.TitleParams('Perempuan', anchor='middle'))
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index", type="nominal", title="",sort="descending"),
        color=alt.Color("variable", type="nominal", title="",legend=None),
    )
)

tp1,tp2 = st.columns((1,1))
tp1.altair_chart(charttp1)   
tp2.altair_chart(charttp2)   

st.dataframe(et23,use_container_width=True)

st.write('# Agama Penduduk Tahun 2023')
url7 = 'https://docs.google.com/spreadsheets/d/1dUtknRWJL7X_5qOs0zLF4zbFH2B4qPjyjkI6SMUxzwY/edit?usp=sharing'
agam23 = conn.read(spreadsheet=url7)
agam23 = pd.DataFrame(agam23)
agam23.index = list(agam23.iloc[0:9,0])
agam23 = agam23.iloc[0:8,1:4]

datatp1 = agam23.iloc[0:8,0]
datatp1 = pd.melt(datatp1.reset_index(), id_vars=["index"])
# Horizontal stacked bar chart
charttp1 = (
    alt.Chart(datatp1,title=alt.TitleParams('Laki-laki', anchor='middle'))
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index", type="nominal", title="",sort="descending"),
        color=alt.Color("variable", type="nominal", title="",legend=None),
    )
)
datatp2 = agam23.iloc[0:8,1]
datatp2 = pd.melt(datatp2.reset_index(), id_vars=["index"])
# Horizontal stacked bar chart
charttp2 = (
    alt.Chart(datatp2,title=alt.TitleParams('Perempuan', anchor='middle'))
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index", type="nominal", title="",sort="descending"),
        color=alt.Color("variable", type="nominal", title="",legend=None),
    )
)

tp1,tp2 = st.columns((1,1))
tp1.altair_chart(charttp1)   
tp2.altair_chart(charttp2)   

st.dataframe(agam23,use_container_width=True)

with st.sidebar:
    st.image('https://www.bpskotabaru.com/desacantik/public/images/Logo%20DESCAN_1_002.png',width=100)
    st.header("Dashboard Data Penduduk Desa Cibiru Wetan")
    st.caption("""Data kependudukan ini menyediakan data jumlah penduduk berdasarkan usia, jenis kelamin, serta data tingkat pendidikan dan status pendidikan angkatan kerja (penduduk usia 18-56 tahun) di Desa Cibiru Wetan, Kecamatan Cileunyi, Kabupaten Bandung, Jawa Barat.""")
