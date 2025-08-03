
import streamlit as st
from streamlit_option_menu import option_menu


# Konfigurasi halaman
st.set_page_config(page_title="Clustering Penggunaan Listrik", page_icon="💡", layout="centered")
import streamlit as st

# CSS untuk menyembunyikan default sidebar
hide_default_sidebar = """
    <style>
        [data-testid="stSidebarNav"] {
            display: none;
        }
    </style>
"""
st.markdown(hide_default_sidebar, unsafe_allow_html=True)

# Navigasi
with st.sidebar:
    selected = option_menu(
        menu_title="Navigasi",
        options=["Beranda", "Upload Data", "Hasil Clustering", "Visualisasi", "Tentang Metode", "Kesimpulan"],
        icons=["house", "upload", "table", "bar-chart-line", "info-circle", "check-circle"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical",
        styles={
            "container": {"padding": "5px", "background-color": "#e6f0ff"},
            "icon": {"color": "blue", "font-size": "18px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "5px", "--hover-color": "#cce0ff"},
            "nav-link-selected": {"background-color": "#3399ff", "color": "white"},
        }
    )

# Routing berdasarkan pilihan menu

if selected == "Beranda":
    from pages.beranda import show
    show()

elif selected == "Upload Data":
    from pages.upload_data import show
    show()

elif selected == "Hasil Clustering":
    from pages.hasil_clustering import show
    show()

elif selected == "Visualisasi":
    from pages.visualisasi import show
    show()

elif selected == "Tentang Metode":
    from pages.tentang_metode import show
    show()

elif selected == "Kesimpulan":
    from pages.kesimpulan import show
    show()
