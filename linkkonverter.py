import streamlit as st
import re

def extract_spreadsheet_id(url):
    pattern = r"/spreadsheets/d/([a-zA-Z0-9-_]+)"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

st.set_page_config(page_title="Anjab Bagor - ImportRange", page_icon="📊")

# --- CSS UNTUK NUANSA UKRAINA ---
st.markdown("""
    <style>
    /* Latar belakang halaman (Biru) */
    .stApp {
        background: linear-gradient(180deg, #0057B7 50%, #FFD700 100%);
    }

    /* Kotak Putih Transparan untuk Input agar tulisan terbaca jelas */
    .stTextInput, .stCheckbox, .stButton, div[data-testid="stVerticalBlock"] > div {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 10px;
    }

    /* Judul Utama */
    h1 {
        color: #FFD700 !important;
        text-shadow: 2px 2px #000000;
        text-align: center;
    }

    /* Label Input */
    label {
        color: #0057B7 !important;
        font-weight: bold !important;
    }

    /* Tombol */
    .stButton>button {
        background-color: #0057B7 !important;
        color: #FFD700 !important;
        border-radius: 10px;
        border: 2px solid #FFD700;
        height: 3em;
        width: 100%;
    }

    /* Footer */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #002d5e;
        color: #FFD700;
        text-align: center;
        padding: 5px;
        font-size: 14px;
        z-index: 100;
    }
    </style>
    """, unsafe_allow_html=True)

# --- KONTEN ---
st.title("🇺🇦 ImportRange Generator")
st.markdown("<p style='text-align: center; color: white;'>Memudahkan administrasi data di Kab. Muaro Jambi</p>", unsafe_allow_html=True)

with st.container():
    url_input = st.text_input("🔗 Link URL Google Sheets Sumber:", placeholder="Paste link di sini...")
    
    col1, col2 = st.columns(2)
    with col1:
        sheet_name = st.text_input("📄 Nama Sheet:", placeholder="Contoh: Sheet1")
    with col2:
        cell_range = st.text_input("🎯 Lokasi Cell:", placeholder="Contoh: A1")

    only_numbers = st.checkbox("🔢 Ambil Angka Saja (Auto-Clean)", value=True)

if st.button("🚀 BUAT RUMUS"):
    if url_input and sheet_name and cell_range:
        spreadsheet_id = extract_spreadsheet_id(url_input)
        if spreadsheet_id:
            base_import = f'IMPORTRANGE("{spreadsheet_id}", "{sheet_name}!{cell_range}")'
            if only_numbers:
                final_formula = f'=VALUE(REGEXEXTRACT(TO_TEXT({base_import}), "\\d+"))'
            else:
                final_formula = f'={base_import}'
            
            st.success("✅ Salin rumus ini ke sheet Anda:")
            st.code(final_formula, language="excel")
        else:
            st.error("Link tidak valid.")
    else:
        st.warning("Data belum lengkap.")

# --- FOOTER ---
st.markdown("""
    <div class="footer">
        Dibuat dengan ❤️ oleh Tim Anjab Bagor Kab Muaro Jambi
    </div>
    """, unsafe_allow_html=True)
