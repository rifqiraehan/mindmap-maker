import streamlit as st
from streamlit_markmap import markmap

st.set_page_config(
    page_title="Mind Mapping Generator",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="auto"
)

st.title("🧠 Mind Map Generator with Markdown")

# Panduan singkat
with st.expander("📘 Panduan Format Markdown"):
    st.markdown("""
Berikut format markdown yang didukung untuk membuat mind map:

- `#` untuk topik utama
- `##` untuk sub-topik
- `###` untuk sub-sub-topik
- `-` untuk daftar / ide tambahan

Contoh:
```
# Teknologi
## Pemrograman
- Python
- C++
## Jaringan
- TCP/IP
```
""")

# Input markdown dari user
default_markdown = """# Anime
## Shounen
### Naruto
- Uzumaki Naruto
- Uchiha Sasuke
- Haruno Sakura
### One Piece
- Monkey D. Luffy
- Roronoa Zoro
- Nami
### My Hero Academia
- Midoriya Izuku
- Bakugou Katsuki
- Todoroki Shouto
## Shoujo
### Sailor Moon
- Tsukino Usagi
- Mizuno Ami
- Hino Rei
### Cardcaptor Sakura
- Kinomoto Sakura
- Li Syaoran
- Daidouji Tomoyo
### Ouran High School Host Club
- Fujioka Haruhi
- Suou Tamaki
- Ootori Kyouya

"""

markdown_input = st.text_area("📝 Masukkan Markdown kamu di sini (`Ctrl + Enter` untuk submit):", value=default_markdown, height=300)

# Tampilkan Mind Map
st.subheader("🗺️ Hasil Mind Map")
markmap(markdown_input)