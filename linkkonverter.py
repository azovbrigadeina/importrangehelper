import streamlit as st
import re

def extract_spreadsheet_id(url):
    pattern = r"/spreadsheets/d/([a-zA-Z0-9-_]+)"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

st.set_page_config(page_title="GS ImportRange Generator", page_icon="📊")

st.title("📊 ImportRange Generator")
st.markdown("Aplikasi ini sekarang secara otomatis menyiapkan pembersihan angka (Regex).")

with st.container():
    st.subheader("1. Detail Spreadsheet")
    url_input = st.text_input("URL Google Sheets Sumber:", 
                              placeholder="https://docs.google.com/spreadsheets/d/...")
    
    col1, col2 = st.columns(2)
    with col1:
        sheet_name = st.text_input("Nama Sheet:", placeholder="Sheet1")
    with col2:
        cell_range = st.text_input("Lokasi Cell/Range:", placeholder="A1")

    st.subheader("2. Pengaturan")
    # Mengubah value menjadi True agar otomatis tercentang saat aplikasi dibuka
    only_numbers = st.checkbox("Hanya ambil angka (Value Extraction)", value=True)
    
if st.button("Generate Rumus"):
    if url_input and sheet_name and cell_range:
        spreadsheet_id = extract_spreadsheet_id(url_input)
        
        if spreadsheet_id:
            base_import = f'IMPORTRANGE("{spreadsheet_id}", "{sheet_name}!{cell_range}")'
            
            if only_numbers:
                # Rumus ini akan mengambil angka pertama yang ditemukan
                final_formula = f'=VALUE(REGEXEXTRACT(TO_TEXT({base_import}), "\\d+"))'
            else:
                final_formula = f'={base_import}'
            
            st.success("Rumus siap digunakan:")
            st.code(final_formula, language="excel")
            
            if only_numbers:
                st.warning("Catatan: Rumus ini menggunakan `TO_TEXT` di dalamnya agar `REGEXEXTRACT` tidak error jika sumbernya sudah berupa angka.")
        else:
            st.error("URL tidak valid.")
    else:
        st.warning("Mohon lengkapi semua data.")
