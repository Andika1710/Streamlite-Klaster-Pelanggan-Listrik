import streamlit as st

def show():
    st.subheader("📌 Kesimpulan Hasil Clustering")

    if "clustered_data" in st.session_state:
        df = st.session_state["clustered_data"]
        total_cluster = df["Cluster"].nunique()

        st.markdown(f"""
        Berdasarkan hasil clustering terhadap data penggunaan listrik di Kabupaten Sukabumi (2019–2023), 
        terbentuk **{total_cluster} klaster**.  
        Tiap klaster merepresentasikan kelompok kecamatan dengan karakteristik penggunaan listrik yang serupa.
        """)

        nama_kolom_kecamatan = [col for col in df.columns if "kec" in col.lower()]
        if nama_kolom_kecamatan:
            kolom_kec = nama_kolom_kecamatan[0]
            cluster_summary = df[[kolom_kec, "Cluster"]].sort_values(by="Cluster")
            cluster_summary = cluster_summary.rename(columns={kolom_kec: "Kecamatan"})
        else:
            cluster_summary = df.copy().sort_values(by="Cluster")

        # ====== Tambahan: ubah index menjadi mulai dari 1 ======
        cluster_summary = cluster_summary.reset_index(drop=True)
        cluster_summary.index = range(1, len(cluster_summary) + 1)

        st.markdown("### 📊 Tabel Hasil Klastering:")
        st.dataframe(cluster_summary, use_container_width=True)

        st.markdown("### 📝 Penjelasan Setiap Klaster:")
        for i in range(total_cluster):
            cluster_df = df[df["Cluster"] == i]
            n_data = len(cluster_df)

            if nama_kolom_kecamatan:
                kecamatan_list = cluster_df[kolom_kec].tolist()
                kecamatan_display = ", ".join(kecamatan_list[:5]) + ("..." if len(kecamatan_list) > 5 else "")
            else:
                kecamatan_display = "(nama kecamatan tidak tersedia)"

            means = cluster_df.select_dtypes(include='number').drop(columns="Cluster").mean()
            mean_global = df.select_dtypes(include='number').drop(columns="Cluster").mean().mean()

            st.markdown(f"""
            #### 🔹 Klaster {i}
            - Jumlah Kecamatan: **{n_data}**
            - Rata-rata:
                - {', '.join([f"{col}: {round(val,2)}" for col, val in means.items()])}
            - Contoh kecamatan: *{kecamatan_display}*

            **Analisis**:  
            Klaster {i} menggambarkan wilayah dengan penggunaan listrik yang {'tinggi' if means.mean() > mean_global else 'rendah atau sedang'}.  
            Cocok untuk strategi energi yang {'fokus pada efisiensi dan penguatan infrastruktur' if means.mean() > mean_global else 'berbasis penghematan dan pengendalian konsumsi'}.
            """)

        st.info("📌 Hasil klaster ini berguna untuk merencanakan distribusi energi, identifikasi kebutuhan listrik, dan pengambilan kebijakan daerah.")
    else:
        st.warning("Silakan lakukan proses clustering terlebih dahulu untuk melihat kesimpulan.")
