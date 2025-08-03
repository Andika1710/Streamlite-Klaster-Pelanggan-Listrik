import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

def show():
    st.title("Hasil Clustering")
    if "uploaded_data" not in st.session_state:
        st.warning("Silakan upload data terlebih dahulu di menu 'Upload Data'.")
    else:
        df = st.session_state["uploaded_data"]
        numeric_cols = df.select_dtypes(include='number').columns.tolist()

        if len(numeric_cols) < 2:
            st.error("Data harus memiliki setidaknya dua kolom numerik.")
        else:
            st.write("📌 Kolom yang digunakan untuk clustering:", ", ".join(numeric_cols))

            X = df[numeric_cols]
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)

            # === Langsung tampilkan grafik Elbow ===
            st.markdown("### 📈 Grafik Elbow (Menentukan Jumlah Cluster Optimal)")
            wcss = []
            max_k = 10
            for i in range(1, max_k + 1):
                kmeans_temp = KMeans(n_clusters=i, random_state=0)
                kmeans_temp.fit(X_scaled)
                wcss.append(kmeans_temp.inertia_)

            fig_elbow, ax_elbow = plt.subplots()
            ax_elbow.plot(range(1, max_k + 1), wcss, marker='o', linestyle='--')
            ax_elbow.set_title("Metode Elbow")
            ax_elbow.set_xlabel("Jumlah Cluster (K)")
            ax_elbow.set_ylabel("WCSS")
            st.pyplot(fig_elbow)

            st.info("Perhatikan titik tekukan ('elbow') pada grafik di atas untuk memilih jumlah cluster yang optimal.")

            # === Slider K ===
            k = st.slider("Pilih jumlah cluster (K):", min_value=2, max_value=10, value=3)

            kmeans = KMeans(n_clusters=k, random_state=0)
            df["Cluster"] = kmeans.fit_predict(X_scaled)

            # Urutkan hasil clustering berdasarkan kolom 'Cluster'
            df_sorted = df.sort_values(by="Cluster").reset_index(drop=True)

            # Ubah index agar mulai dari 1
            df_sorted.index = range(1, len(df_sorted) + 1)

            st.success(f"Clustering berhasil dilakukan dengan {k} klaster.")
            st.dataframe(df_sorted)

            st.session_state["clustered_data"] = df_sorted

            # ======== Silhouette Score =========
            score = silhouette_score(X_scaled, df["Cluster"])
            st.info(f"🔎 Silhouette Score untuk K = {k}: **{score:.4f}**")

            if score > 0.7:
                interpretasi = "struktur klaster sangat baik"
            elif score > 0.5:
                interpretasi = "struktur klaster cukup jelas"
            elif score > 0.25:
                interpretasi = "struktur klaster lemah"
            else:
                interpretasi = "struktur klaster buruk atau tumpang tindih"

            st.write(f"📝 Interpretasi: {interpretasi.capitalize()}.")
