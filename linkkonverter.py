import streamlit as st
import re

def extract_spreadsheet_id(url):
    pattern = r"/spreadsheets/d/([a-zA-Z0-9-_]+)"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

st.set_page_config(page_title="Anjab Bagor - ImportRange", page_icon="📊")

# --- CSS PERBAIKAN (Kontras Tinggi) ---
st.markdown("""
    <style>
    /* Latar belakang halaman gradasi Biru-Kuning */
    .stApp {
        background: linear-gradient(180deg, #0057B7 0%, #FFD700 100%);
    }

    /* Kotak Input: Latar belakang putih terang, teks HITAM PEKAT */
    div[data-baseweb="input"], .stTextInput input {
        background-color: #ffffff !important;
        color: #000000 !important; /* Teks hitam */
        -webkit-text-fill-color: #000000 !important;
    }
    
    /* Warna placeholder (teks bantuan di dalam kotak) */
    ::placeholder {
        color: #666666 !important;
        opacity: 1; 
    }

    /* Membungkus form agar lebih rapi */
    .stForm, div[data-testid="stVerticalBlock"] > div {
        background-color: rgba(255, 255, 255, 0.2);
        padding: 20px;
        border-radius: 15px;
    }

    /* Judul Utama */
    h1 {
        color: #ffffff !important;
        text-shadow: 2px 2px #0057B7;
        text-align: center;
        font-weight: 800;
    }

    /* Label di atas kotak input (Kuning terang agar kontras dengan biru) */
    label {
        color: #FFD700 !important;
        font-weight: bold !important;
        font-size: 1.1rem !important;
        text-shadow: 1px 1px #000000;
    }

    /* Tombol */
    .stButton>button {
        background-color: #FFD700 !important;
        color: #0057B7 !important;
        font-weight: bold;
        border: 2px solid #ffffff;
        width: 100%;
        height: 3.5em;
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
    }
    </style>
    """, unsafe_allow_html=True)

# --- ISI APLIKASI ---
st.title("🇺🇦 ImportRange Generator")
st.markdown("<p style='text-align: center; color: white;'>Sistem Administrasi Data - Kab. Muaro Jambi</p>", unsafe_allow_html=True)

with st.container():
    url_input = st.text_input("🔗 Link URL Google Sheets Sumber:", placeholder="Tempel link di sini...")
    
    col1, col2 = st.columns(2)
    with col1:
        sheet_name = st.text_input("📄 Nama Sheet:", placeholder="Contoh: Sheet1")
    with col2:
        cell_range = st.text_input("🎯 Lokasi Cell:", placeholder="Contoh: A1")

    # Warna teks checkbox diatur lewat CSS atau label
    st.markdown("<style>div.stCheckbox > label > div[data-testid='stMarkdownContainer'] > p {color: white !important; font-weight: bold;}</style>", unsafe_allow_html=True)
    only_numbers = st.checkbox("🔢 Ambil Angka Saja (Auto-Clean)", value=True)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🚀 GENERATE RUMUS SEKARANG"):
    if url_input and sheet_name and cell_range:
        spreadsheet_id = extract_spreadsheet_id(url_input)
        if spreadsheet_id:
            base_import = f'IMPORTRANGE("{spreadsheet_id}", "{sheet_name}!{cell_range}")'
            if only_numbers:
                final_formula = f'=VALUE(REGEXEXTRACT(TO_TEXT({base_import}), "\\d+"))'
            else:
                final_formula = f'={base_import}'
            
            st.success("✅ Berhasil! Silakan salin rumus di bawah ini:")
            st.code(final_formula, language="excel")
        else:
            st.error("Link URL tidak valid!")
    else:
        st.warning("Mohon lengkapi data terlebih dahulu.")

# --- FOOTER ---
st.markdown("""
    <div class="footer">
        Dibuat dengan ❤️ oleh Tim Anjab Bagor Kab Muaro Jambi
    </div>
    """, unsafe_allow_html=True)
