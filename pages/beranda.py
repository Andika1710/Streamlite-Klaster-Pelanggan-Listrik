import streamlit as st

def show():
    st.title("Analisis Klaster Jumlah Pelanggan Listrik 💡  Kabupaten Sukabumi Menggunakan Metode K-Means Clustering")
    st.subheader("Priode (2019–2023)")
    st.image("img2.jpg", use_column_width=True)
    st.markdown("""
        Aplikasi ini digunakan untuk melakukan analisis klaster terhadap penggunaan listrik di Kabupaten Sukabumi.
        Gunakan menu "Upload Data" untuk memasukkan data Anda dan melihat hasil clustering serta visualisasi.
    """)
