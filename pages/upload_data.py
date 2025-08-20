import streamlit as st
import pandas as pd
import folium


def show():
    st.subheader("📁 Upload Dataset Penggunaan Listrik")
    uploaded_file = st.file_uploader("Upload file CSV Anda", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        # Ubah index agar mulai dari 1
        df.index = range(1, len(df) + 1)

        st.success("Data berhasil diupload!")
        st.dataframe(df)

        # Simpan ke session state
        st.session_state["uploaded_data"] = df

        # Tampilkan total jumlah data (baris)
        st.info(f"🔢 Total data: **{len(df)} baris**")
