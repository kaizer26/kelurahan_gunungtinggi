import streamlit as st
import pandas as pd
import plotly.express as px

### Import Data
dataumkm = pd.read_excel("C:/Users/wella/Documents/Asha/SMT7/magang/DESA SEKARWANGI/Data UMKM Sekarwangi_ready.xlsx")
type(dataumkm)
dataumkm["NIK"] = dataumkm["NIK"].astype("string")
dataumkm["No HP"] = dataumkm["No HP"].astype("string")
dataumkm['RW'] = dataumkm['ALAMAT'].str[-5:]
dataumkm['RT'] = dataumkm['ALAMAT'].str[-11:]
df = dataumkm

st.markdown("# Grafik")

a = st.sidebar.radio('Jumlah Karakteristik yang Ingin Divisualisasikan:', [1, 2])

if a==1:
    #Dropdown Menu
    kolom_1 = st.selectbox("Pilih Karakteristik", dataumkm.columns, index=7)

    ###Bar Chart
    st.subheader("Grafik Batang")
    tes = dataumkm.pivot_table(index=dataumkm[kolom_1],values='NIK',aggfunc='count')
    st.bar_chart(data = tes, height = 700)

    st.subheader("Scatter Plot")
    st.write("Grafik ini menunjukkan pelaku UMKM di Desa Sekarwangi menurut besarnya modal usaha dan pendapatan usaha per bulan.")

    fig = px.scatter(
        data_frame=dataumkm, x="BESARNYA MODAL USAHA", y="PENDAPATAN PER BULAN",color=kolom_1,symbol=kolom_1)
    st.plotly_chart(fig)

elif a==2:
    #Dropdown Menu
    kolom_1 = st.selectbox("Pilih Karakteristik Pertama", dataumkm.columns, index=7)
    kolom_2 = st.selectbox("Pilih Karakteristik Kedua", dataumkm.columns, index=17)

    ###Bar Chart
    st.subheader("Grafik Batang")
    tes = pd.crosstab(dataumkm[kolom_1],dataumkm[kolom_2])
    st.bar_chart(data = tes, height = 700)

    st.subheader("Scatter Plot")
    st.write("Grafik ini menunjukkan pelaku UMKM di Desa Sekarwangi menurut besarnya modal usaha dan pendapatan usaha per bulan.")

    fig = px.scatter(
        data_frame=dataumkm, x="BESARNYA MODAL USAHA", y="PENDAPATAN PER BULAN",color=kolom_1,symbol=kolom_2)
    st.plotly_chart(fig)
