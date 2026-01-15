import streamlit as st
import re

# Fungsi untuk mengambil ID Spreadsheet
def extract_spreadsheet_id(url):
    pattern = r"/spreadsheets/d/([a-zA-Z0-9-_]+)"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="ImportRange Generator - Muaro Jambi", page_icon="📊")

# --- CUSTOM CSS (Nuansa Ukraina: Biru & Kuning) ---
st.markdown("""
    <style>
    /* Mengubah warna background header */
    .stApp {
        background-color: #ffffff;
    }
    /* Warna judul utama (Biru) */
    h1 {
        color: #0057B7 !important;
        border-bottom: 5px solid #FFD700;
        padding-bottom: 10px;
    }
    /* Warna sub-header */
    h3 {
        color: #0057B7 !important;
    }
    /* Gaya tombol */
    .stButton>button {
        background-color: #FFD700 !important;
        color: #0057B7 !important;
        font-weight: bold;
        border: 2px solid #0057B7 !important;
        border-radius: 10px;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #0057B7 !important;
        color: #FFD700 !important;
    }
    /* Footer */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0057B7;
        color: #FFD700;
        text-align: center;
        padding: 10px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ISI APLIKASI ---
st.title("📊 ImportRange Generator")
st.markdown("Alat bantu ekstraksi data otomatis untuk efisiensi pelaporan.")

with st.container():
    st.subheader("📍 Input Data Sumber")
    url_input = st.text_input("Link URL Google Sheets:", 
                              placeholder="Tempel link di sini...")
    
    col1, col2 = st.columns(2)
    with col1:
        sheet_name = st.text_input("Nama Sheet:", placeholder="Contoh: Sheet1")
    with col2:
        cell_range = st.text_input("Lokasi Cell:", placeholder="Contoh: A1")

    st.subheader("⚙️ Pengaturan")
    only_numbers = st.checkbox("Ekstrak Angka Saja (Default Aktif)", value=True)
    
st.markdown("---")

if st.button("🚀 GENERATE RUMUS SEKARANG"):
    if url_input and sheet_name and cell_range:
        spreadsheet_id = extract_spreadsheet_id(url_input)
        
        if spreadsheet_id:
            base_import = f'IMPORTRANGE("{spreadsheet_id}", "{sheet_name}!{cell_range}")'
            
            if only_numbers:
                # Rumus dengan proteksi TO_TEXT dan VALUE
                final_formula = f'=VALUE(REGEXEXTRACT(TO_TEXT({base_import}), "\\d+"))'
            else:
                final_formula = f'={base_import}'
            
            st.success("✅ Rumus Berhasil Dibuat!")
            st.code(final_formula, language="excel")
            st.info("Salin rumus di atas dan tempelkan pada Google Sheets Anda.")
        else:
            st.error("❌ Link URL tidak valid! Pastikan link benar.")
    else:
        st.warning("⚠️ Mohon isi semua kolom terlebih dahulu.")

# --- FOOTER ---
st.markdown("""
    <div class="footer">
        Dibuat dengan ❤️ oleh Tim Anjab Bagor Kab Muaro Jambi
    </div>
    """, unsafe_allow_html=True)
