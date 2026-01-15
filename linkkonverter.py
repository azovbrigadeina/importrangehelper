import streamlit as st
import re

def extract_spreadsheet_id(url):
    pattern = r"/spreadsheets/d/([a-zA-Z0-9-_]+)"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

st.set_page_config(page_title="Anjab Bagor - ImportRange", page_icon="📊")

# --- CSS PERBAIKAN (Placeholder Hide on Focus) ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(180deg, #0057B7 0%, #FFD700 100%);
    }

    /* Kotak Input */
    div[data-baseweb="input"], .stTextInput input {
        background-color: #ffffff !important;
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
        font-weight: 500;
    }
    
    /* Placeholder standar (Abu-abu Tua) */
    input::placeholder {
        color: #444444 !important;
        opacity: 1 !important;
    }
    
    /* MENGHILANGKAN PLACEHOLDER SAAT DIKLIK (FOCUS) */
    input:focus::placeholder {
        color: transparent !important;
        -webkit-text-fill-color: transparent !important;
    }

    /* Label Input */
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
        sheet_name = st.text_input("📄 Nama Sheet:", placeholder="Misal: Sheet1")
    with col2:
        cell_range = st.text_input("🎯 Lokasi Cell:", placeholder="Misal: A1")

    st.markdown("<style>div.stCheckbox > label > div[data-testid='stMarkdownContainer'] > p {color: white !important; font-weight: bold;}</style>", unsafe_allow_html=True)
    only_numbers = st.checkbox("🔢 Ambil Angka Saja (Auto-Extract)", value=True)

if st.button("🚀 GENERATE RUMUS"):
    if url_input and sheet_name and cell_range:
        spreadsheet_id = extract_spreadsheet_id(url_input)
        if spreadsheet_id:
            base_import = f'IMPORTRANGE("{spreadsheet_id}", "{sheet_name}!{cell_range}")'
            if only_numbers:
                final_formula = f'=VALUE(REGEXEXTRACT(TO_TEXT({base_import}), "\\d+"))'
            else:
                final_formula = f'={base_import}'
            
            st.success("✨ Rumus Berhasil Dibuat!")
            st.code(final_formula, language="excel")
        else:
            st.error("❌ Link tidak valid.")
    else:
        st.warning("⚠️ Data belum lengkap.")

st.markdown("""<div class="footer">Dibuat dengan ❤️ oleh Tim Anjab Bagor Kab Muaro Jambi</div>""", unsafe_allow_html=True)
