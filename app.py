import streamlit as st
import os

st.set_page_config(
    page_title="Saham Kuantitatif",
    page_icon="Hello",
)

st.title("Home")
st.sidebar.success("Pilih halaman diatas")

# Tambahkan CSS untuk styling
st.markdown(
    """
    <style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f4f8fb;
        margin: 0;
        padding: 0;
    }
    header {
        background-color: #ffffff;
        padding: 10px 20px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    header .logo {
        display: flex;
        align-items: center;
    }
    header .logo img {
        height: 50px;
        margin-right: 10px;
    }
    header nav a {
        text-decoration: none;
        margin-left: 20px;
        font-weight: bold;
        color: #007BFF;
    }
    .hero-section {
        text-align: center;
        padding: 50px 20px;
    }
    .hero-section h1 {
        color: #007BFF;
    }
    .hero-section p {
        color: #555;
        max-width: 600px;
        margin: 0 auto;
    }
    .content-section {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        margin: 20px auto;
        padding: 20px;
        gap: 20px;
    }
    .card {
        background-color: #fff;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        text-align: center;
        padding: 20px;
        width: 300px;
    }
    .card img {
        max-width: 50px;
        margin-bottom: 20px;
    }
    .card h3 {
        color: #007BFF;
    }
    footer {
        text-align: center;
        padding: 20px;
        background-color: #007BFF;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
# Hero Section
st.markdown(
    """
    <div class="hero-section">
        <h1>Automated Investment Manager</h1>
    </div>
    """,
    unsafe_allow_html=True
)
st.image("Saham Kuantitatif.jpg", use_column_width=True)
st.markdown(
    """
        <p>
            Saham Kuantitatif adalah Aplikasi Manajer Investasi Otomatis dalam Trading dan Investasi Saham yang dimotori oleh Artificial Intelligence (AI) dan Machine Learning berdasarkan analisa Kuantitatif & Statistik.
        </p>
    """,
    unsafe_allow_html=True
)

# Mengapa Kami Section
st.markdown(
    """
    <section class="content-section">
        <div class="card">
            <h3>Trusted</h3>
            <p>Terpercaya karena algoritma kami didasari oleh pengetahuan kuantitatif trading yang melihat dari analisa fundamental & teknikal serta performa statistik.</p>
        </div>
        <div class="card">
            <h3>Transparent</h3>
            <p>Aplikasi kami menggunakan data real-time yang up-to-date. Analisa AI kami juga memiliki akurasi tinggi hingga 80%.</p>
        </div>
        <div class="card">
            <h3>Up Scale</h3>
            <p>Aplikasi kami meningkatkan probabilitas dengan analisa yang mampu meningkatkan pertumbuhan portofolio Anda secara konsisten.</p>
        </div>
    </section>
    """,
    unsafe_allow_html=True
)

# Footer
st.markdown(
    """
    <footer>
        &copy; 2024 Saham Kuantitatif. All rights reserved.
    </footer>
    """,
    unsafe_allow_html=True
)
