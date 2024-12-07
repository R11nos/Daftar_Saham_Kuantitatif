import streamlit as st
import pandas as pd
from openpyxl import load_workbook

# Judul aplikasi
st.title('Pendaftaran Aplikasi')

# Fungsi untuk mencatat data ke file Excel
def catat_ke_excel(nama, email, nomor_wa):
    file_path = "pendaftaran.xlsx"
    
    # Cek apakah file sudah ada
    try:
        # Membaca file Excel jika sudah ada
        workbook = load_workbook(file_path)
        sheet = workbook.active
        # Menambahkan data baru ke baris berikutnya
        sheet.append([nama, email, nomor_wa])
        workbook.save(file_path)
    except FileNotFoundError:
        # Membuat file baru jika belum ada
        data = {"Nama Lengkap": [nama], "Email": [email], "Nomor WhatsApp": [nomor_wa]}
        df = pd.DataFrame(data)
        df.to_excel(file_path, index=False, engine='openpyxl')

# Formulir Pendaftaran
with st.form(key='registration_form'):
    nama = st.text_input('Nama Lengkap')
    email = st.text_input('Email')
    nomor_wa = st.text_input('Nomor WhatsApp')
    
    # Tombol Kirim Formulir
    submit_button = st.form_submit_button(label='Daftar')

# Menampilkan informasi biaya pendaftaran setelah formulir dikirim
if submit_button:
    if nama and email and nomor_wa:  # Validasi input
        # Catat data ke file Excel
        catat_ke_excel(nama, email, nomor_wa)
        
        # Tampilkan pesan sukses
        st.success(f"Terima kasih {nama} telah mendaftar!")
        st.write("Biaya pendaftaran: Rp 250,000 (Harga Promo)")
        st.write("Rekening Mandiri: 1170006154728 a/n Rio Reynaldo Tanos")
        st.write("Kirim bukti transfer ke Nomor WA Admin: 081299398708")
        st.write("Setelah transfer, Link Aplikasi akan diberikan melalui WA")
    else:
        st.error("Harap isi semua kolom pada formulir!")
