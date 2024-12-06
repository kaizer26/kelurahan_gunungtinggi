# -- coding: utf-8 --
"""
Created on Wed Oct  4 11:54:31 2023

@author: Asus
"""

import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.set_page_config(
    page_title="Dashboard Data Desa Cibiru Wetan",
    page_icon="🏠",
)

#this is the header


t1, t2 = st.columns((0.25,1))

t1.image('cibiruwetan.png', width = 100)
t2.title("Desa Cantik Cibiru Wetan")
t2.markdown(" **Halaman Utama Dashboard Data Desa Cibiru Wetan** ")


#this is content
 #st.image('https://www.desawisata-cibiruwetan.com/wp-content/uploads/2023/01/branding-cibiru-wetan-WISATA-1-800x197.png')
### Import Data Lengkap
url = 'https://docs.google.com/spreadsheets/d/10TvMMPQnOEKG8gABZZw2LXAK1XDHsU17oGsXkhiORdA/edit?usp=sharing'
conn  = st.connection("gsheets", type=GSheetsConnection)
datadesa = conn.read(spreadsheet=url)
datadesa = pd.DataFrame(datadesa)                       #convert ke panda df
st.write("# Rekap Data Desa Cibiru Wetan")

url2='https://docs.google.com/spreadsheets/d/16AtuoSRO-7SwU8E6jJDNzdoX6S0DyRFkpaduxBhZ748/edit?usp=sharing'
datap2024 = conn.read(spreadsheet=url2)
datap2024 = pd.DataFrame(datap2024)                       #convert ke panda df
jp2024=datap2024.iloc[0:16,1:3].sum().sum()

datapiramida = datap2024.iloc[0:16,1:3]
jk = list(["Laki-laki","Perempuan"])
datapiramida.iloc[0:16,0]=-datapiramida.iloc[0:16,0]
datapiramida.index = list(datap2024.iloc[0:16,0])
datapiramida.columns = jk

pd2024laki = int(datap2024.iloc[0:16,1:2].sum().sum())
pd2024pere = int(datap2024.iloc[0:16,2:3].sum().sum())
lakipere2024 = pd.DataFrame({"laki":[pd2024laki],"perempuan":[pd2024pere]})
lakipere2024.columns = list(["Laki-laki","Perempuan"])

m1, m2, m3 = st.columns((1,1,1))
m1.write("")
m2.metric(label = 'Total KK',value = "📋"+str(int(datap2024.iloc[18,1])))
m3.write("")

m1, m2, m3 = st.columns((1,1,1))
m1.write("")
m2.metric(label ='Total Penduduk (jiwa)',value = "🚻"+str(int(jp2024)))
m3.write("")

m1, m2, m3, m4 = st.columns((1,1,1,1))
m1.write("")
m2.metric(label ='Penduduk Laki-laki',value = "🚹"+str(int(pd2024laki)))
m3.metric(label = 'Penduduk Perempuan',value = "🚺"+str(int(pd2024pere)))
m4.write("")
st.write("Berdasarkan data Kementerian Dalam Negeri (Kemendagri), jumlah kartu keluarga (KK) yang terdaftar di Desa Cibiru Wetan pada tahun ",str(int(datadesa.iloc[20,1]))," sebanyak ",str(int(datap2024.iloc[18,1])),". Jumlah penduduk pada periode tersebut sebanyak ",str(int(jp2024))," jiwa dengan penduduk laki-laki sebanyak ",str(int(pd2024laki))," jiwa dan penduduk perempuan sebanyak",str(pd2024pere)," jiwa.")

url9='https://docs.google.com/spreadsheets/d/1Skt6QdDL1_EKQJ3MgdJG53-FtCevRv56pRZNOyBf4lI/edit?usp=sharing'
fas23 = conn.read(spreadsheet=url9)
fas23 = pd.DataFrame(fas23)                       #convert ke panda df
fas23 = fas23.iloc[1:94,0:3]
sd=int(fas23.iloc[2,1]);mi=int(fas23.iloc[14,1]);sdt=int(fas23.iloc[2,1]+fas23.iloc[14,1])
smp=int(fas23.iloc[3,1]);mts=int(fas23.iloc[15,1]);smpt=int(fas23.iloc[3,1]+fas23.iloc[15,1])
sma=int(fas23.iloc[4,1]);ma=int(fas23.iloc[16,1]);smat=int(fas23.iloc[4,1]+fas23.iloc[16,1])

pd1,pd2,pd3,pd4,pd5 = st.columns((1,1,1,1,1))
pd1.write("")
pd2.metric(label='SD',value="🎒"+str(sdt))
pd3.metric(label='SMP',value="🏫"+str(smpt))
pd4.metric(label='SMA/K',value="📘"+str(smat))
pd5.write("")
st.write("Berdasarkan data Kementerian Pendidikan dan Budaya (Kemendikbud) dan Kementerian Agama, jumlah sekolah yang terdaftar di Desa Cibiru Wetan pada tahun ",str(int(datadesa.iloc[21,1])),", antara lain SD/sederajat sebanyak ",str(sdt)," (termasuk ",str(mi)," Madrasah Ibtidaiyah/MI), SMP/sederajat sebanyak ",str(smpt)," (termasuk ",str(mts)," Madrasah Tsanawiyah/MTs), dan SMA/SMK/sederajat sebanyak ",str(smat)," (termasuk ",str(ma)," Madrasah Aliyah/MA).")

url10='https://docs.google.com/spreadsheets/d/15sfFQbVZUmseAfOv70EXI4pe3wUusL9OvfeOex43ueg/edit?usp=sharing'
conn  = st.connection("gsheets", type=GSheetsConnection)
pt23 = conn.read(spreadsheet=url10)
pt23 = pd.DataFrame(pt23)                       #convert ke panda df
pt23 = pt23.iloc[0:65,0:4]
pt23.index = list(pt23.iloc[0:65,0])
pt23 = pt23.iloc[0:65,1:4]
p1,p2 = st.columns((1,1))
p1.metric(label='Hasil panen Kopi (Ton/Ha)',value="☕"+str(int(pt23.iloc[60,1])))
p2.metric(label='Hasil Panen Padi Sawah (Ton/Ha)',value="🌾"+str(int(pt23.iloc[7,1])))
st.write("Pada tahun ",str(int(datadesa.iloc[22,1])),", perkebunan kopi di Desa Cibiru Wetan yang memiliki luas ",str(int(pt23.iloc[60,0]))," hektar (Ha) menghasilkan panen sebanyak ",str(int(pt23.iloc[60,1]))," Ton untuk setiap hektarnya. Selain itu, lahan sawah padi di Cibiru Wetan yang memiliki luas ",str(int(pt23.iloc[7,0]))," hektar (Ha) memiliki hasil panen sebanyak ",str(int(pt23.iloc[7,1]))," Ton untuk setiap hektarnya.")

import pydeck as pdk
st.write("# Profil Desa Cibiru Wetan")
with st.sidebar:
    st.image('desa_cantik.png',width=100)
    st.header("Dashboard Desa Cibiru Wetan")
    st.caption("""Dashboard ini menyediakan data kewilayahan dan karakteristik penduduk di Desa Cibiru Wetan, Kecamatan Cileunyi, Kabupaten Bandung, Jawa Barat.""")


datadesa1 = pd.DataFrame(datadesa.iloc[0:12,0:2])                       #convert ke panda df
desa = datadesa1.style.hide(axis=0).hide(axis=1)                     #menyembunyikan nomor tabel dan header                                   #menyembunyikan header
st.image('https://i.ytimg.com/vi/fw8YWKACQ00/maxresdefault.jpg')
st.write(desa.to_html(),unsafe_allow_html=True,use_container_width=True)         #menyembunyikan nomor tabel dari .to_html sampe True)

st.write("# Peta Lokasi Desa Cibiru Wetan")
mapimage = 'https://www.google.com/maps/vt/data=ZXYT48-fmLw7vEGYqBAWelAfa34jOHxmz4wg8me2i8GFgqBVM8DqF42inRiTkwkiEO5Ev9VeTOmWNwKyGW8xgj8VsclxjChGnOqXTjpZ1f3y_7H5Qq7P9BYST4nGLG1tkm32T0C7Zem8Azyk7WaIy0isvhrG4dsX8GccMm1hFQq6eVMK4mICuCk2IbaiybMbF7EbHVtURq7C19E7jMT9JL6VHUudZs8UfBs5xcEzfMBnkx2KRh1ug6bkxGHCjrYao4EaI_mOLko0BOMYoOlFqGtLwbUFjJ_DACUAxTXBOx0fciiD'
urlmaps = 'https://maps.app.goo.gl/EqKfyTcDpfHrS4pa8'
st.markdown(
    f'<a href="{urlmaps}" target="_blank">'
    f'<img src="{mapimage}" alt="Clickable Image" style="width: 100%;" title="Klik untuk membukanya di Maps">'
    f'</a>',
    unsafe_allow_html=True
)
st.write("Desa Cibiru Wetan, Kecamatan Cileunyi, Kabupaten Bandung, Jawa Barat")

datadesa2 = pd.DataFrame(datadesa.iloc[12:18,0:2])                       #convert ke panda df
desa2 = datadesa2.style.hide(axis=0).hide(axis=1)                        #menyembunyikan header dan nomor tabel
st.write(desa2.to_html(),unsafe_allow_html=True,use_container_width=True)         #menyembunyikan nomor tabel dari .to_html sampe True)

st.write("# Kunjungi Kami")
ig = "https://cdn4.iconfinder.com/data/icons/social-messaging-ui-color-shapes-2-free/128/social-instagram-new-circle-512.png"
yt = 'https://www.pngkey.com/png/full/3-32240_logo-youtube-png-transparent-background-youtube-icon.png'
web = 'https://cdn-icons-png.flaticon.com/512/5339/5339181.png'
url_ig = 'https://www.instagram.com/desa_cibiruwetan?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=='
url_yt = 'https://youtube.com/@desa_cibiruwetan?si=js2kX36jVxCMI64F'
url_web = 'https://cibiruwetan.desa.id'
#st.write("[instagram](%s)" % url_ig," | [youtube](%s)" % url_yt," | [website](%s)" % url_web)
pd1,pd2,pd3,pd4,pd5 = st.columns((1,1,1,1,1))

# Menggunakan HTML untuk membuat gambar yang dapat diklik
pd1.write('')
pd2.markdown(f'<a href="{url_ig}" target="_blank"><img src="{ig}" alt="Clickable Image" style="width:80px;"></a>', unsafe_allow_html=True)
pd3.markdown(f'<a href="{url_yt}" target="_blank"><img src="{yt}" alt="Clickable Image" style="width:80px;"></a>', unsafe_allow_html=True)
pd4.markdown(f'<a href="{url_web}" target="_blank"><img src="{web}" alt="Clickable Image" style="width:80px;"></a>', unsafe_allow_html=True)
pd5.write('')
st.write("**📧: desawisatacibiruwetan@gmail.com**")
urlkantor = 'https://maps.app.goo.gl/4Swdj5bh4YfkTmn76'
st.write("🏢: **[Jl. Cibangkonol No.28, Cibiru Wetan, Kec. Cileunyi, Kabupaten Bandung, Jawa Barat 40625](%s)**"%urlkantor)

