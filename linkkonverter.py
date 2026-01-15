import streamlit as st
import re

def extract_spreadsheet_id(url):
    # Regex untuk mengambil ID dari URL Google Sheets
    pattern = r"/spreadsheets/d/([a-zA-Z0-9-_]+)"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

# Konfigurasi Halaman
st.set_page_config(page_title="Google Sheets ImportRange Generator", page_icon="📊")

st.title("📊 ImportRange Generator")
st.markdown("Alat sederhana untuk membuat rumus `IMPORTRANGE` Google Sheets tanpa ribet.")

# Input Form
with st.container():
    st.subheader("Input Data")
    url_input = st.text_input("1. Masukkan URL Google Sheets Sumber:", 
                              placeholder="https://docs.google.com/spreadsheets/d/...")
    
    col1, col2 = st.columns(2)
    with col1:
        sheet_name = st.text_input("2. Nama Sheet:", placeholder="Sheet1")
    with col2:
        cell_range = st.text_input("3. Lokasi Cell/Range:", placeholder="A1:Z100")

# Logika Pembuatan Rumus
if st.button("Generate Rumus"):
    if url_input and sheet_name and cell_range:
        spreadsheet_id = extract_spreadsheet_id(url_input)
        
        if spreadsheet_id:
            # Menyusun rumus
            final_formula = f'=IMPORTRANGE("{spreadsheet_id}", "{sheet_name}!{cell_range}")'
            
            st.success("Berhasil dibuat!")
            st.code(final_formula, language="excel")
            
            st.info("""
            **Tips:** * Pastikan spreadsheet tujuan sudah diberikan izin akses (Allow Access) setelah menempelkan rumus ini.
            * Pastikan nama sheet sesuai (termasuk spasi dan kapitalisasi).
            """)
        else:
            st.error("URL tidak valid. Pastikan Anda memasukkan URL Google Sheets yang benar.")
    else:
        st.warning("Mohon isi semua kolom terlebih dahulu.")

# Footer
st.divider()
st.caption("Dibuat untuk mempercepat alur kerja spreadsheet Anda.")
