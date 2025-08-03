import streamlit as st
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd

def show():
    if "clustered_data" not in st.session_state:
        st.warning("Silakan lakukan clustering terlebih dahulu.")
    else:
        df = st.session_state["clustered_data"]
        
        # ========= SCATTER PLOT BERDASARKAN FITUR =========
        st.subheader("📉 Visualisasi Klaster Berdasarkan Fitur yang Dipilih")
        st.markdown(
            """
            <div style='font-size: 16px; color: #444;'>
            Grafik ini menampilkan penyebaran data berdasarkan dua fitur (misalnya tahun 2019 dan 2020) 
            yang dipilih pengguna. Setiap titik mewakili satu data, dan warna menunjukkan hasil klasterisasi 
            dengan algoritma K-Means. Anda bisa memilih fitur berbeda untuk melihat pola lain.
            </div>
            """, unsafe_allow_html=True
        )

        numeric_cols = df.select_dtypes(include='number').drop(columns=["Cluster"]).columns.tolist()
        if 'tahun' in df.columns and df['tahun'].dtype != 'object':
            if 'tahun' not in numeric_cols:
                numeric_cols.append('tahun')

        cluster_col = "Cluster"

        col1 = st.selectbox("🟦 Pilih fitur untuk sumbu X /jumlah pelanggan listrik tahun :", numeric_cols, index=0)
        col2 = st.selectbox("🟨 Pilih fitur untuk sumbu Y:", numeric_cols, index=1 if len(numeric_cols) > 1 else 0)

        fig1, ax1 = plt.subplots()
        ax1.scatter(df[col1], df[col2], c=df[cluster_col], cmap="viridis", s=100)
        ax1.set_xlabel(col1)
        ax1.set_ylabel(col2)
        ax1.set_title("Visualisasi Klaster (Scatter Plot)")
        st.pyplot(fig1)

        st.caption("🔎 Semakin dekat titik-titik, semakin mirip datanya. Warna berbeda menunjukkan klaster berbeda.")

        st.markdown("---")

        # ========= PCA VISUALIZATION =========
        st.subheader("📊 Visualisasi Klaster dengan PCA (Semua Fitur)")
        st.markdown(
            """
            <div style='font-size: 16px; color: #444;'>
            PCA (Principal Component Analysis) adalah teknik reduksi dimensi yang membantu menyederhanakan 
            data berdimensi banyak menjadi hanya 2 dimensi agar mudah divisualisasikan. 
            Setiap titik adalah representasi data setelah disederhanakan, dan warnanya menunjukkan klaster.
            </div>
            """, unsafe_allow_html=True
        )

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(df[numeric_cols])

        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(X_scaled)

        df_pca = pd.DataFrame(X_pca, columns=["PCA 1", "PCA 2"])
        df_pca["Cluster"] = df[cluster_col].values

        fig2, ax2 = plt.subplots()
        scatter = ax2.scatter(df_pca["PCA 1"], df_pca["PCA 2"], c=df_pca["Cluster"], cmap="viridis", s=50)
        legend = ax2.legend(*scatter.legend_elements(), title="Cluster")
        ax2.add_artist(legend)
        ax2.set_xlabel("PCA 1")
        ax2.set_ylabel("PCA 2")
        ax2.set_title("Visualisasi Hasil Clustering (PCA 2D)")
        st.pyplot(fig2)

        st.caption("📌 PCA menyederhanakan fitur menjadi 2 dimensi untuk melihat penyebaran antar klaster.")
