import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.set_page_config(
    page_title="Data Kependudukan",
    page_icon=":family:",
)

#this is the header
t1, t2 = st.columns((0.25,1))

t1.image('https://www.desawisata-cibiruwetan.com/wp-content/uploads/2024/09/icon-logo-dewi-warna-600x721.png', width = 100)
t2.title("Desa Cibiru Wetan")
t2.markdown(" **Halaman Data Kependudukan Desa Cibiru Wetan, Cileunyi, Kab. Bandung** ")

#this is content
st.write("# Penduduk Berdasarkan Jenis Kelamin dan Kelompok Usia")
pilih1 = st.radio('Tahun :',[2024,2023])

##data penduduk
### Import tahun 2024
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

#Import data 2023
url3 = 'https://docs.google.com/spreadsheets/d/196eZm3CzaY1FIapq0nnWBc18dFz0yXxtPrxtlYaqRLc/edit?usp=sharing'
datap2023 = conn.read(spreadsheet=url3)
datap2023 = pd.DataFrame(datap2023)                       #convert ke panda df
jp2023=datap2023.iloc[0:16,1:3].sum().sum()

datapiramida2 = datap2023.iloc[0:16,1:3]
jk = list(["Laki-laki","Perempuan"])
datapiramida2.iloc[0:16,0]=-datapiramida2.iloc[0:16,0]
datapiramida2.index = list(datap2023.iloc[0:16,0])
datapiramida2.columns = jk

import altair as alt
# Convert wide-form data to long-form
# See: https://altair-viz.github.io/user_guide/data.html#long-form-vs-wide-form-data
if pilih1 ==2024:
    data = pd.melt(datapiramida.reset_index(), id_vars=["index"])
    # Horizontal stacked bar chart
    chart = (
        alt.Chart(data)
        .mark_bar()
        .encode(
            x=alt.X("value", type="quantitative", title="",axis=alt.Axis(labels=False)),
            y=alt.Y("index", type="nominal", title="",sort="descending"),
            color=alt.Color("variable", type="nominal", title=""),
        )
    )

    st.altair_chart(chart, use_container_width=True)   #bikin piramida chart
    st.write("Total Penduduk:",int(jp2024)," | Penduduk Laki-laki:",int(datap2024.iloc[0:16,1].sum().sum())," | Penduduk Perempuan:",int(datap2024.iloc[0:16,2].sum().sum()))
    with st.expander("lihat tabel"):
        st.dataframe(datap2024.iloc[0:16,0:3], use_container_width=True, hide_index=True)   #menampilkan data
elif pilih1==2023:
    # Convert wide-form data to long-form
    data2 = pd.melt(datapiramida2.reset_index(), id_vars=["index"])
    chart2 = (
        alt.Chart(data2)
        .mark_bar()
        .encode(
            x=alt.X("value", type="quantitative", title="",axis=alt.Axis(labels=False)),
            y=alt.Y("index", type="nominal", title="",sort="descending"),
            color=alt.Color("variable", type="nominal", title=""),
        )
    )
    st.altair_chart(chart2, use_container_width=True)   #bikin piramida chart
    st.write("Total Penduduk:",jp2023," | Penduduk Laki-laki:",int(datap2023.iloc[0:16,1].sum().sum())," | Penduduk Perempuan:",int(datap2023.iloc[0:16,2].sum().sum()))
    with st.expander("lihat tabel"):
        st.dataframe(datap2023.iloc[0:16,0:3], use_container_width=True, hide_index=True)   #menampilkan data

#data pekerjaan
url4 = 'https://docs.google.com/spreadsheets/d/1wjTtBvxU2a-x0LGEfkX7IaQcN1DhkzJ4ZqRk1DYO8Yw/edit?usp=sharing'
kerja23 = conn.read(spreadsheet=url4)
kerja23 = pd.DataFrame(kerja23)
stkerja23 = kerja23.iloc[16:18,0:4]
kerja23 = kerja23.iloc[0:13,0:4]

st.write('# Jumlah Angkatan Kerja Berdasarkan Status Pekerjaan Tahun 2023')
stkerja23.index = list(stkerja23.iloc[0:2,0])
stkerja23 = stkerja23.iloc[0:2,1:4]
#######
pilih2 = st.radio("Pilih Jenis Kelamin:",['Laki & Perempuan','Laki-laki','Perempuan'],key="status kerja")
if pilih2 =='Laki & Perempuan':
    datatp1 = stkerja23.iloc[0:2,2]
elif pilih2 == 'Laki-laki':
    datatp1 = stkerja23.iloc[0:2,0]
elif pilih2 == 'Perempuan':
    datatp1 = stkerja23.iloc[0:2,1]
datatp1 = pd.melt(datatp1.reset_index(), id_vars=["index"])
charttp1 = (
    alt.Chart(datatp1,title=alt.TitleParams(pilih2, anchor='middle'))
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index", type="nominal", title="",sort="descending"),
        color=alt.Color("variable", type="nominal", title="",legend=None),
    )
)
text1 = charttp1.mark_text(
    align='left',
    baseline='middle',
    dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='value'
)
charttp1 = (charttp1 + text1)
st.altair_chart(charttp1,use_container_width=True)
with st.expander("lihat tabel"):
    st.dataframe(stkerja23,use_container_width=True)

st.write('# Jumlah Penduduk Berdasarkan Jenis Pekerjaan Tahun 2023')
kerja23.index = list(kerja23.iloc[0:13,0])
kerja23 = kerja23.iloc[0:13,1:4]
#######
pilih3 = st.radio('Pilih Jenis Kelamin: ',['Laki & Perempuan','Laki-laki','Perempuan'],key="pekerjaan")
if pilih3 =='Laki & Perempuan':
    datatp2 = kerja23.iloc[0:13,2]
elif pilih3 == 'Laki-laki':
    datatp2 = kerja23.iloc[0:13,0]
elif pilih3 == 'Perempuan':
    datatp2 = kerja23.iloc[0:13,1]
datatp2 = pd.melt(datatp2.reset_index(), id_vars=["index"])
charttp2 = (
    alt.Chart(datatp2,title=alt.TitleParams(pilih3, anchor='middle'))
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index", type="nominal", title="",sort="descending"),
        color=alt.Color("variable", type="nominal", title="",legend=None),
    )
)
text2 = charttp2.mark_text(
    align='left',
    baseline='middle',
    dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='value'
)
charttp2 = (charttp2 + text2)
st.altair_chart(charttp2,use_container_width=True)
with st.expander("lihat tabel"):
    st.dataframe(kerja23,use_container_width=True)

st.write('# Pendidikan Tenaga Kerja Tahun 2023')
url5 = 'https://docs.google.com/spreadsheets/d/1BaFB0sFvKIv_e3G8LX_6su-vwDUJKhZLWeE1knU5bT8/edit?usp=sharing'
pdik23 = conn.read(spreadsheet=url5)
pdik23 = pd.DataFrame(pdik23)
pdik23 = pdik23.iloc[0:6,0:4]
pdik23.index = list(pdik23.iloc[0:6,0])
pdik23 = pdik23.iloc[0:6,1:4]
pilih4 = st.radio("Pilih Jenis Kelamin: ",['Laki & Perempuan','Laki-laki','Perempuan'],key="pendidikan")
if pilih4 =='Laki & Perempuan':
    datatp3 = pdik23.iloc[0:6,2]
elif pilih4 == 'Laki-laki':
    datatp3 = pdik23.iloc[0:6,0]
elif pilih4 == 'Perempuan':
    datatp3 = pdik23.iloc[0:6,1]

datatp3 = pd.melt(datatp3.reset_index(), id_vars=["index"])
charttp3 = (
    alt.Chart(datatp3,title=alt.TitleParams(pilih4, anchor='middle'))
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index", type="nominal", title="",sort="descending"),
        color=alt.Color("variable", type="nominal", title="",legend=None),
    )
)
text3 = charttp3.mark_text(
    align='left',
    baseline='middle',
    dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='value'
)
charttp3 = (charttp3 + text3)

st.altair_chart(charttp3,use_container_width=True)
with st.expander("lihat tabel"):
    st.dataframe(pdik23,use_container_width=True)

st.write('# Jumlah Penduduk Menurut Etnis Tahun 2023')
url6 = 'https://docs.google.com/spreadsheets/d/1lrJgC7IgzaYUElTEzhix6m2Wz-u-ThN1WXsGRHgMv8s/edit?usp=sharing'
et23 = conn.read(spreadsheet=url6)
et23 = pd.DataFrame(et23)
et23.index = list(et23.iloc[0:21,0])
et23 = et23.iloc[0:20,1:4]
pilih5 = st.radio("Pilih Jenis Kelamin: ",['Laki & Perempuan','Laki-laki','Perempuan'],key="etnis")
if pilih5 =='Laki & Perempuan':
    datatp4 = et23.iloc[0:20,2]
elif pilih5 == 'Laki-laki':
    datatp4 = et23.iloc[0:20,0]
elif pilih5 == 'Perempuan':
    datatp4 = et23.iloc[0:20,1]
datatp4 = pd.melt(datatp4.reset_index(), id_vars=["index"])
charttp4 = (
    alt.Chart(datatp4,title=alt.TitleParams(pilih5, anchor='middle'))
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index", type="nominal", title="",sort="descending"),
        color=alt.Color("variable", type="nominal", title="",legend=None),
    )
)
text4 = charttp4.mark_text(
    align='left',
    baseline='middle',
    dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='value'
)
charttp4 = (charttp4 + text4)
st.altair_chart(charttp4,use_container_width=True)
with st.expander("lihat tabel"):
    st.dataframe(et23,use_container_width=True)

st.write('# Jumlah Penduduk Menurut Agama Tahun 2023')
url7 = 'https://docs.google.com/spreadsheets/d/1dUtknRWJL7X_5qOs0zLF4zbFH2B4qPjyjkI6SMUxzwY/edit?usp=sharing'
agam23 = conn.read(spreadsheet=url7)
agam23 = pd.DataFrame(agam23)
agam23.index = list(agam23.iloc[0:9,0])
agam23 = agam23.iloc[0:8,1:4]
pilih6 = st.radio("Pilih Jenis Kelamin: ",['Laki & Perempuan','Laki-laki','Perempuan'],key="agama")
if pilih6 =='Laki & Perempuan':
    datatp5 = agam23.iloc[0:8,2]
elif pilih6 == 'Laki-laki':
    datatp5 = agam23.iloc[0:8,0]
elif pilih6 == 'Perempuan':
    datatp5 = agam23.iloc[0:8,1]
datatp5 = pd.melt(datatp5.reset_index(), id_vars=["index"])
charttp5 = (
    alt.Chart(datatp5,title=alt.TitleParams(pilih6, anchor='middle'))
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index", type="nominal", title="",sort="descending"),
        color=alt.Color("variable", type="nominal", title="",legend=None),
    ).facet().resolve_scale(
        y='independent')
)
text5 = charttp5.mark_text(
    align='left',
    baseline='middle',
    dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='value'
)
charttp5 = (charttp5 + text5)
st.altair_chart(charttp5,use_container_width=True)
with st.expander("lihat tabel"):
    st.dataframe(agam23,use_container_width=True)

with st.sidebar:
    st.image('https://www.bpskotabaru.com/desacantik/public/images/Logo%20DESCAN_1_002.png',width=100)
    st.header("Dashboard Data Penduduk Desa Cibiru Wetan")
    st.caption("""Data kependudukan ini menyediakan data jumlah penduduk berdasarkan usia, jenis kelamin, serta data tingkat pendidikan dan status pendidikan angkatan kerja (penduduk usia 18-56 tahun) di Desa Cibiru Wetan, Kecamatan Cileunyi, Kabupaten Bandung, Jawa Barat.""")
