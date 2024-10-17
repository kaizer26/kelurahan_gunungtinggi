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
# Inisialisasi i
i = 0

# Loop melalui data publikasi
while i < len(publikasi):
    # Buat tiga kolom untuk setiap iterasi
    pd1, pd2, pd3 = st.columns((1, 1, 1))

    # Cek untuk kolom pertama
    if i < len(publikasi):
        pd1.image(str(publikasi.iloc[i, 3]))
        pd1.write(str(publikasi.iloc[i, 0]))
        pd1.write("[Unduh](%s)" % str(publikasi.iloc[i, 1]))
    else:
        pd1.write('')

    # Cek untuk kolom kedua
    if i + 1 < len(publikasi):
        pd2.image(str(publikasi.iloc[i + 1, 3]))
        pd2.write(str(publikasi.iloc[i + 1, 0]))
        pd2.write("[Unduh](%s)" % str(publikasi.iloc[i + 1, 1]))
    else:
        pd2.write('')

    # Cek untuk kolom ketiga
    if i + 2 < len(publikasi):
        pd3.image(str(publikasi.iloc[i + 2, 3]))
        pd3.write(str(publikasi.iloc[i + 2, 0]))
        pd3.write("[Unduh](%s)" % str(publikasi.iloc[i + 2, 1]))
    else:
        pd3.write('')

    # Increment i untuk memproses tiga item sekaligus
    i += 3
    
with st.sidebar:
    st.image('desa_cantik.png',width=100)
    st.header("Dashboard Unduh Publikasi Desa Cibiru Wetan")
    st.caption("""Menu Unduh Publikasi menyediakan publikasi yang berisikan kompilasi informasi dan data di Desa Cibiru Wetan, Kecamatan Cileunyi, Kabupaten Bandung, Jawa Barat.""")
