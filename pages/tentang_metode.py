import streamlit as st
from PIL import Image

def show():
   
    st.markdown("### 📌 Metode yang Digunakan")
    st.markdown("""
    - **K-Means Clustering**  
      Merupakan metode *unsupervised learning* yang bekerja dengan membagi data ke dalam sejumlah cluster berdasarkan kedekatan nilai fitur.
    
    - **StandardScaler**  
      Digunakan untuk menstandarisasi data sebelum proses clustering, agar semua fitur memiliki skala yang setara (mean = 0 dan standar deviasi = 1).
    
    - **Elbow Method**  
      Teknik ini digunakan untuk membantu menentukan jumlah klaster optimal dengan cara melihat titik tekuk (elbow) pada grafik WCSS.
    """)

    st.markdown("### 🧠 Cara Kerja Singkat K-Means:")
    st.markdown("""
    1. Tentukan jumlah klaster (K).
    2. Pilih centroid awal secara acak.
    3. Hitung jarak setiap data ke centroid dan kelompokkan ke klaster terdekat.
    4. Perbarui posisi centroid.
    5. Ulangi proses hingga konvergen (tidak ada perubahan signifikan).
    """)

    st.markdown("### 🎯 Tujuan:")
    st.markdown("""
    Dengan menggunakan metode ini, kita dapat mengidentifikasi kelompok pelanggan listrik dengan karakteristik yang serupa, 
    yang sangat berguna untuk perencanaan distribusi energi, analisis beban wilayah, dan kebijakan efisiensi listrik.
    """)

    st.success("📊 Analisis ini membantu dalam pengambilan keputusan berbasis data oleh pemerintah atau pihak penyedia energi.")
