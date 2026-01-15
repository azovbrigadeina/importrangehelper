import streamlit as st
import re

def extract_spreadsheet_id(url):
    pattern = r"/spreadsheets/d/([a-zA-Z0-9-_]+)"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

st.set_page_config(page_title="Anjab Bagor - ImportRange", page_icon="📊")

# --- CSS PERBAIKAN FINAL (Kontras Placeholder & Input) ---
st.markdown("""
    <style>
    /* Latar belakang halaman gradasi Biru-Kuning */
    .stApp {
        background: linear-gradient(180deg, #0057B7 0%, #FFD700 100%);
    }

    /* Kotak Input: Putih, Teks HITAM */
    div[data-baseweb="input"], .stTextInput input {
        background-color: #ffffff !important;
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
    }
    
    /* MEMPERBAIKI PLACEHOLDER (Teks Contoh) agar lebih gelap/kelihatan */
    input::placeholder {
        color: #444444 !important; /* Abu-abu tua agar kontras di putih */
        opacity: 1 !important;
    }
    
    /* Untuk browser lain seperti Firefox/Edge */
    ::-webkit-input-placeholder { color: #444444 !important; opacity: 1 !important; }
    ::-moz-placeholder { color: #444444 !important; opacity: 1 !important; }
    :-ms-input-placeholder { color: #444444 !important; opacity: 1 !important; }

    /* Container form */
    div[data-testid="stVerticalBlock"] > div {
        background-color: rgba(255, 255, 255, 0.15);
        padding: 20px;
        border-radius: 15px;
    }

    /* Label Input (Kuning) */
    label {
        color: #FFD700 !important;
        font-weight: bold !important;
        text-shadow: 1px 1px #000000;
    }

    /* Tombol */
    .stButton>button {
        background-color: #FFD700 !important;
        color: #0057B7 !important;
        font-weight: 800;
        border: 2px solid #ffffff;
        border-radius: 10px;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #0057B7 !important;
        color: #FFD700 !important;
        border: 2px solid #FFD700;
    }

    /* Footer */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #003a7a;
        color: #FFD700;
        text-align: center;
        padding: 8px;
        font-weight: bold;
        z-index: 999;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ISI APLIKASI ---
st.markdown("<h1 style='text-align: center; color: white; text-shadow: 2px 2px #000;'>🇺🇦 ImportRange Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white; font-weight: bold;'>Tim Anjab Bagor - Kab. Muaro Jambi</p>", unsafe_allow_html=True)

with st.container():
    url_input = st.text_input("🔗 Link URL Google Sheets Sumber:", placeholder="Tempel link spreadsheet di sini...")
    
    col1, col2 = st.columns(2)
    with col1:
        sheet_name = st.text_input("📄 Nama Sheet:", placeholder="Misal: Data_Pegawai")
    with col2:
        cell_range = st.text_input("🎯 Lokasi Cell:", placeholder="Misal: G12")

    # Checkbox Label Putih
    st.markdown("<style>div.stCheckbox > label > div[data-testid='stMarkdownContainer'] > p {color: white !important; font-weight: bold; font-size: 16px;}</style>", unsafe_allow_html=True)
    only_numbers = st.checkbox("🔢 Ambil Angka Saja (Auto-Extract)", value=True)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🚀 GENERATE RUMUS"):
    if url_input and sheet_name and cell_range:
        spreadsheet_id = extract_spreadsheet_id(url_input)
        if spreadsheet_id:
            # Menggunakan TO_TEXT agar aman jika sel sumber sudah angka murni
            base_import = f'IMPORTRANGE("{spreadsheet_id}", "{sheet_name}!{cell_range}")'
            if only_numbers:
                final_formula = f'=VALUE(REGEXEXTRACT(TO_TEXT({base_import}), "\\d+"))'
            else:
                final_formula = f'={base_import}'
            
            st.success("✨ Rumus Anda Berhasil Dibuat!")
            st.code(final_formula, language="excel")
        else:
            st.error("❌ Link URL tidak valid. Pastikan itu link Google Sheets.")
    else:
        st.warning("⚠️ Harap lengkapi Link, Nama Sheet, dan Cell.")

# --- FOOTER ---
st.markdown("""
    <div class="footer">
        Dibuat dengan ❤️ oleh Tim Anjab Bagor Kab Muaro Jambi
    </div>
    """, unsafe_allow_html=True)
