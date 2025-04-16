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
## Music
### Love Live! School Idol Project
- Ayumu Uehara
- Setsuna Yuuki
- Karin Asaka
### K-On!
- Yui Hirasawa
- Mio Akiyama
- Ritsu Tainaka
### BanG Dream!
- Kasumi Toyama
- Tae Hanazono
- Arisa Ichigaya

## Other
### Fate/Stay Night
- Shirou Emiya
- Saber (Artoria Pendragon)
- Rin Tohsaka
### Chi: Chikyuu no Undou ni Tsuite
- Rafal
- Badeni
- Nowak
### One Outs
- Toua Tokuchi
- Kojima Hiromichi
- Saikawa

"""

markdown_input = st.text_area("📝 Masukkan Markdown kamu di sini (`Ctrl + Enter` untuk submit):", value=default_markdown, height=300)

# Tampilkan Mind Map
st.subheader("🗺️ Hasil Mind Map")
markmap(markdown_input)