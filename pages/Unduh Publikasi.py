import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.set_page_config(
    page_title="Unduh Publikasi",
    page_icon="📚",
)

urlbuku = 'https://docs.google.com/spreadsheets/d/1QmIOm1JnY9I9TkEUMlWXtZjs-igTHMfU45F1KLzAO8g/edit?usp=sharing'
conn  = st.connection("gsheets", type=GSheetsConnection)
publikasi = conn.read(spreadsheet=urlbuku)
publikasi = pd.DataFrame(publikasi)                       #convert ke panda df
#this is the header
t1, t2 = st.columns((0.25,1))

t1.image('https://www.desawisata-cibiruwetan.com/wp-content/uploads/2024/09/icon-logo-dewi-warna-600x721.png', width = 100)
t2.title("Desa Cantik Cibiru Wetan")
t2.markdown(" **Halaman Unduh Publikasi Desa Cibiru Wetan** ")

pd1,pd2,pd3 = st.columns((1,1,1))
pd1.image(str(publikasi.iloc[0,3]))
pd1.write(str(publikasi.iloc[0,0]))
pd1.write("[Unduh](%s)"%str(publikasi.iloc[0,1]))
pd2.image(str(publikasi.iloc[1,3]))
pd2.write(str(publikasi.iloc[1,0]))
pd2.write("[Unduh](%s)"%str(publikasi.iloc[1,1]))
pd3.image(str(publikasi.iloc[2,3]))
pd3.write(str(publikasi.iloc[2,0]))
pd3.write("[Unduh](%s)"%str(publikasi.iloc[2,1]))

pd1,pd2,pd3 = st.columns((1,1,1))
pd1.image(str(publikasi.iloc[3,3]))
pd1.write(str(publikasi.iloc[3,0]))
pd1.write("[Unduh](%s)"%str(publikasi.iloc[3,1]))
pd2.write('')
pd2.write("")
pd3.write('')
pd3.write("")


with st.sidebar:
    st.image('https://www.bpskotabaru.com/desacantik/public/images/Logo%20DESCAN_1_002.png',width=100)
    st.header("Dashboard Unduh Publikasi Desa Cibiru Wetan")
    st.caption("""Menu Unduh Publikasi menyediakan publikasi yang berisikan kompilasi informasi dan data di Desa Cibiru Wetan, Kecamatan Cileunyi, Kabupaten Bandung, Jawa Barat.""")
