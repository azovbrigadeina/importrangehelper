import streamlit as st
import re

def extract_spreadsheet_id(url):
    pattern = r"/spreadsheets/d/([a-zA-Z0-9-_]+)"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

st.set_page_config(page_title="Slava Ukraini - ImportRange", page_icon="🇺🇦")

# --- CSS COSMETIC SLAVA UKRAINI ---
st.markdown("""
    <style>
    /* Background Bendera Ukraina yang Halus */
    .stApp {
        background: linear-gradient(180deg, #0057B7 0%, #0057B7 50%, #FFD700 50%, #FFD700 100%);
        background-attachment: fixed;
    }

    /* Animasi Teks Slava Ukraini */
    .slava-text {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 900;
        color: #FFD700;
        text-shadow: 3px 3px #000, 0 0 20px #FFD700;
        margin-bottom: 0px;
        font-family: 'Arial Black', sans-serif;
    }

    /* Kotak Input Putih Bersih */
    div[data-baseweb="input"], .stTextInput input {
        background-color: #ffffff !important;
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
        border: 2px solid #0057B7 !important;
        border-radius: 10px !important;
    }
    
    /* Placeholder Hilang Saat Fokus */
    input::placeholder { color: #555555 !important; opacity: 1 !important; }
    input:focus::placeholder { color: transparent !important; }

    /* Container dengan Glassmorphism di bagian tengah */
    div[data-testid="stVerticalBlock"] > div {
        background-color: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 25px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.3);
    }

    /* Label Input */
    label {
        color: #ffffff !important;
        font-weight: bold !important;
        text-shadow: 1px 1px 3px #000;
        font-size: 1.1rem !important;
    }

    /* Tombol Heroik */
    .stButton>button {
        background: linear-gradient(90deg, #0057B7, #0080ff) !important;
        color: #FFD700 !important;
        font-weight: 900;
        font-size: 1.2rem;
        border: 2px solid #FFD700;
        border-radius: 50px;
        transition: 0.4s ease;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 20px #FFD700;
        color: #ffffff !important;
    }

    /* Footer tetap */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: rgba(0, 58, 122, 0.9);
        color: #FFD700;
        text-align: center;
        padding: 10px;
        font-weight: bold;
        border-top: 3px solid #FFD700;
        z-index: 1000;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SLAVA UKRAINI ---
st.markdown('<p class="slava-text">SLAVA UKRAINI! 🇺🇦</p>', unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: white; margin-top:-10px;'>Gerombolan ImportRange - Muaro Jambi</h3>", unsafe_allow_html=True)

with st.container():
    url_input = st.text_input("🔗 Link Spreadsheet Sumber:", placeholder="Tempel link di sini...")
    
    col1, col2 = st.columns(2)
    with col1:
        sheet_name = st.text_input("📄 Nama Sheet:", placeholder="Misal: Sheet1")
    with col2:
        cell_range = st.text_input("🎯 Lokasi Cell:", placeholder="Misal: A1")

    st.markdown("<style>div.stCheckbox > label > div[data-testid='stMarkdownContainer'] > p {color: #FFD700 !important; font-weight: bold; font-size: 18px; text-shadow: 1px 1px 2px #000;}</style>", unsafe_allow_html=True)
    only_numbers = st.checkbox("🔢 Ekstrak Angka (Hero Mode)", value=True)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🚀 GENERATE FREEDOM FORMULA"):
    if url_input and sheet_name and cell_range:
        spreadsheet_id = extract_spreadsheet_id(url_input)
        if spreadsheet_id:
            base_import = f'IMPORTRANGE("{spreadsheet_id}", "{sheet_name}!{cell_range}")'
            if only_numbers:
                final_formula = f'=VALUE(REGEXEXTRACT(TO_TEXT({base_import}), "\\d+"))'
            else:
                final_formula = f'={base_import}'
            
            st.balloons() # Efek perayaan
            st.success("✨ Rumus Siap Digunakan!")
            st.code(final_formula, language="excel")
        else:
            st.error("❌ Link tidak valid!")
    else:
        st.warning("⚠️ Data belum lengkap, Kawan!")

# --- FOOTER ---
st.markdown("""
    <div class="footer">
        Dibuat dengan ❤️ oleh Tim Anjab Bagor Kab Muaro Jambi | Heroiam Slava!
    </div>
    """, unsafe_allow_html=True)
