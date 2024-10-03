import streamlit as st
import pandas as pd

### Import Data
dataumkm = pd.read_excel("C:/Users/wella/Documents/Asha/SMT7/magang/DESA SEKARWANGI/Data UMKM Sekarwangi_ready.xlsx")
type(dataumkm)
dataumkm["NIK"] = dataumkm["NIK"].astype("string")
dataumkm["No HP"] = dataumkm["No HP"].astype("string")
dataumkm['RW'] = dataumkm['ALAMAT'].str[-5:]
dataumkm['RT'] = dataumkm['ALAMAT'].str[-11:]
df = pd.DataFrame(dataumkm)

### Pivot Table
st.subheader("Pivot Table")

a = st.sidebar.radio('Jumlah Karakteristik yang Ingin Ditampilkan:', [1, 2])

if a == 1:
    kolom_1 = st.selectbox("Pilih Karakteristik", dataumkm.columns, index=7)
    pivot = df.pivot_table(index = [kolom_1],
                             values = ['NAMA PEMILIK'],
                             aggfunc = "count"
                             )
    pivot.rename(columns = {'NAMA PEMILIK':'JUMLAH'}, inplace = True)
    st.write(pivot)
elif a== 2:
    kolom_1 = st.selectbox("Pilih Karakteristik Pertama", dataumkm.columns, index=7)
    kolom_2 = st.selectbox("Pilih Karakteristik Kedua", dataumkm.columns, index=17)
    pivot = df.pivot_table(index = [kolom_1,kolom_2],
                             values = ['NAMA PEMILIK'],
                             aggfunc = "count"
                             )
    pivot.rename(columns = {'NAMA PEMILIK':'JUMLAH'}, inplace = True)
    st.write(pivot)

@st.cache_data
def convert_df(pivot):
    return pivot.to_csv().encode('utf-8')
csv = convert_df(pivot)
st.download_button(
    label = "Unduh Tabel",
    data = csv,
    file_name='download_sekarwangi.csv',
    mime='text/csv',
    )
