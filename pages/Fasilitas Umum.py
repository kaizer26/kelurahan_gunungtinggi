import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.set_page_config(
    page_title="Fasilitas Umum",
    page_icon=":cityscape:",
)

#this is the header
t1, t2 = st.columns((0.25,1))

t1.image('https://www.desawisata-cibiruwetan.com/wp-content/uploads/2024/09/icon-logo-dewi-warna-600x721.png', width = 100)
t2.title("Desa Cibiru Wetan")
t2.markdown(" **Halaman Data Fasilitas Umum Desa Cibiru Wetan, Cileunyi, Kab. Bandung** ")
t2.write(" **Tahun 2023** ")

url9='https://docs.google.com/spreadsheets/d/1Skt6QdDL1_EKQJ3MgdJG53-FtCevRv56pRZNOyBf4lI/edit?usp=sharing'
conn  = st.connection("gsheets", type=GSheetsConnection)
fas23 = conn.read(spreadsheet=url9)
fas23 = pd.DataFrame(fas23)                       #convert ke panda df
fas23 = fas23.iloc[1:94,0:3]

#this is content
st.write("# Fasilitas Pendidikan")
s_ag = st.checkbox("termasuk sekolah keagamaan",value=True)           #dengan sekolah agama

if s_ag:
    tka=fas23.iloc[13,1]
    sda=fas23.iloc[14,1]
    smpa=fas23.iloc[15,1]
    smaa=fas23.iloc[16,1]
    pta=fas23.iloc[18,1]
else:
    tka=0;sda=0;smpa=0;smaa=0;pta=0
pd1,pd2,pd3,pd4,pd5 = st.columns((1,1,1,1,1))
pd1.metric(label='TK',value="🚸"+str(int(fas23.iloc[1,1]+tka)))
pd2.metric(label='SD',value="🎒"+str(int(fas23.iloc[2,1]+sda)))
pd3.metric(label='SMP',value="🏫"+str(int(fas23.iloc[3,1]+smpa)))
pd4.metric(label='SMA',value="📘"+str(int(fas23.iloc[4,1]+smaa)))
pd5.metric(label='PT',value="🎓"+str(int(fas23.iloc[5,1]+fas23.iloc[6,1]+pta)))

st.write("# Fasilitas Kesehatan")
ks1,ks2,ks3,ks4,ks5 = st.columns((1,1,1,1,1))
ks1.metric(label='Poliklinik/Balai Kes.',value="🏥"+str(int(fas23.iloc[24,1])))
ks2.metric(label='Apotek',value="💊"+str(int(fas23.iloc[25,1])))
ks3.metric(label='Posyandu',value="👶🏼"+str(int(fas23.iloc[26,1])))
ks4.metric(label='Prak. Dokter',value="🧑🏼‍⚕️"+str(int(fas23.iloc[30,1])))
ks5.metric(label='Prak. Bidan',value="👩🏼‍⚕️"+str(int(fas23.iloc[34,1])))

st.write("# Fasilitas Keagamaan/Peribadatan")
ag1,ag2,ag3,ag4 = st.columns((1,1,1,1))
ag1.metric(label='Masjid',value="🕌"+str(int(fas23.iloc[86,1])))
ag2.metric(label='Mushola',value="🕌"+str(int(fas23.iloc[87,1])))
ag3.metric(label='Gereja Kristen',value="⛪"+str(int(fas23.iloc[88,1])))
ag4.metric(label='Gereja Katholik',value="⛪"+str(int(fas23.iloc[89,1])))
ag5,ag6,ag7 = st.columns((1,1,1))
ag5.metric(label='Wihara',value="🛕"+str(int(fas23.iloc[90,1])))
ag6.metric(label='Pura',value="☸️"+str(int(fas23.iloc[91,1])))
ag7.metric(label='Klenteng',value="☯️"+str(int(fas23.iloc[92,1])))

st.write("# Fasilitas Koperasi, Perbankan, dan Lembaga Keuangan")
pb1,pb2,pb3,pb4,pb5 = st.columns((1,1,1,1,1))
pb1.metric(label='KUD',value="🏠"+str(int(fas23.iloc[37,1])))
pb2.metric(label='KSP',value="💵"+str(int(fas23.iloc[38,1])))
pb3.metric(label='Bumdes',value="🏢"+str(int(fas23.iloc[40,1])))
pb4.metric(label='Pegadaian',value="⚖️"+str(int(fas23.iloc[44,1])))
pb5.metric(label='Bank Pemerintah',value="🏦"+str(int(fas23.iloc[45,1])))

st.write("# Fasilitas Jasa dan Perdagangan")
pg1,pg2,pg3 = st.columns((1,1,1))
pg1.metric(label='Toko/Kios',value="🛍️"+str(int(fas23.iloc[50,1])))
pg2.metric(label='Swalayan',value="🏪"+str(int(fas23.iloc[51,1])))
pg3.metric(label='Toko Kelontong',value="🧃"+str(int(fas23.iloc[53,1])))

st.write("# Fasilitas Akomodasi")
ak1,ak2,ak3 = st.columns((1,1,1))
ak1.metric(label='Rumah Kontrakan',value="🏠"+str(int(fas23.iloc[68,1])))
ak2.metric(label='Hotel',value="🏨"+str(int(fas23.iloc[70,1])))
ak3.metric(label='Villa',value="🏡"+str(int(fas23.iloc[72,1])))

st.write("# Fasilitas Olahraga")
or1,or2,or3,or4,or5 = st.columns((1,1,1,1,1))
or1.metric(label='Lap. Sepakbola',value="⚽"+str(int(fas23.iloc[76,1])))
or2.metric(label='Lap. Bulutangkis',value="🏸"+str(int(fas23.iloc[77,1])))
or3.metric(label='Lap. Voli',value="🏐"+str(int(fas23.iloc[80,1])))
or4.metric(label='Meja Pingpong',value="🏓"+str(int(fas23.iloc[78,1])))
or5.metric(label='Lap. Basket',value="🏀"+str(int(fas23.iloc[83,1])))

### Import Data Lengkap
st.write('# Fasilitas Selengkapnya')
st.dataframe(fas23,use_container_width=True)

with st.sidebar:
    st.image('https://www.bpskotabaru.com/desacantik/public/images/Logo%20DESCAN_1_002.png',width=100)
    st.header("Dashboard Data Fasilitas Umum Desa Cibiru Wetan")
    st.caption("""Data fasilitas umum ini menyediakan data fasilitas yang dapat diakses masyarakat, meliputi fasilitas pendidikan, kesehatan, perbankan, dan lainnya di Desa Cibiru Wetan, Kecamatan Cileunyi, Kabupaten Bandung, Jawa Barat.""")
