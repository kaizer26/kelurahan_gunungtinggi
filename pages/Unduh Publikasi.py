import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.set_page_config(
    page_title="Unduh Publikasi",
    page_icon="📚",
)

url = 'https://docs.google.com/spreadsheets/d/10TvMMPQnOEKG8gABZZw2LXAK1XDHsU17oGsXkhiORdA/edit?usp=sharing'
conn  = st.connection("gsheets", type=GSheetsConnection)
datadesa = conn.read(spreadsheet=url)
datadesa = pd.DataFrame(datadesa)                       #convert ke panda df
#this is the header
t1, t2 = st.columns((0.25,1))

t1.image('https://www.desawisata-cibiruwetan.com/wp-content/uploads/2024/09/icon-logo-dewi-warna-600x721.png', width = 100)
t2.title("Desa Cantik Cibiru Wetan")
t2.markdown(" **Halaman Unduh Publikasi Desa Cibiru Wetan** ")

urlmono23 = 'https://drive.google.com/file/d/1wqu3XjSCo_ro7pV_xgxJF5WNlBYAW3rb/view?usp=sharing'
urlstat23 = 'https://drive.google.com/file/d/1hTDGnTyuNZt0_n6CyZXk4ZzO6yKyaMSs/view?usp=sharing'
urlprof24 = 'https://drive.google.com/file/d/1T75Q0mMxDhrK234yPxjvSKsHexCCjQuC/view?usp=sharing'

pd1,pd2,pd3 = st.columns((1,1,1))
pd1.image('cover_publikasi/profil2024.png')
pd1.write("[Unduh](%s)"%urlprof24)
pd2.image('cover_publikasi/monografi2023.png')
pd2.write("[Unduh](%s)"%urlmono23)
pd3.image('cover_publikasi/statistik2023.png')
pd3.write("[Unduh](%s)"%urlstat23)

with st.sidebar:
    st.image('https://www.bpskotabaru.com/desacantik/public/images/Logo%20DESCAN_1_002.png',width=100)
    st.header("Dashboard Unduh Publikasi Desa Cibiru Wetan")
    st.caption("""Menu Unduh Publikasi menyediakan publikasi monografi dan statistik daerah yang berisikan kompilasi data di Desa Cibiru Wetan, Kecamatan Cileunyi, Kabupaten Bandung, Jawa Barat.""")
