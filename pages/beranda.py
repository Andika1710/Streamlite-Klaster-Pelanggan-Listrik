import streamlit as st

def show():
    st.title("ANALISIS KLASTER PELANGGAN LISTRIK BERDASARKAN PERILAKU KONSUMSI DI KOTA SUKABUMI Metode K-Means Clustering")
    st.image("img2.jpg", use_column_width=True)
    st.markdown("""
        Aplikasi ini digunakan untuk melakukan analisis klaster terhadap penggunaan listrik di Kabupaten Sukabumi.
        Gunakan menu "Upload Data" untuk memasukkan data Anda dan melihat hasil clustering serta visualisasi.
    """)
