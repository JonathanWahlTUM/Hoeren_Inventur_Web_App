import streamlit as st
import time

# Seitenkonfiguration
st.set_page_config(
    page_title="Hören Inventur Web App",
    layout="centered"
)

# Liste der Button-Beschriftungen
button_definitions = [
    "Warnsignal", "Autogeräusche", "Zuggeräusche", "Busgeräusche",
    "Motorrollergeräusche", "Schritte", "Stimmen", "Fahrstuhl",
    "Husten", "Durchsage", "Rascheln", "Klappern",
    "Bremsgeräusch", "Läuten", "Vogelzwitschern", "Rolltreppe",
    "Tür", "Hupen", "Sirenen", "Wind"
]

# Session State initialisieren
if "last_click_time" not in st.session_state:
    st.session_state["last_click_time"] = 0.0

if "logs" not in st.session_state:
    st.session_state["logs"] = []

# URLs zu deinen Audiodateien auf Google Drive (öffentliche Links)
audio_files = {
    "Audio 1": "https://drive.google.com/uc?export=download&id=1W-0o0uqI8byVizJNXOwth9WdsAHLi-9e",
    "Audio 2": "https://drive.google.com/uc?export=download&id=1AHUh_Bg_h9Bf_99FvgT5uJA9_FsNFUfC",
    "Audio 3": "https://drive.google.com/uc?export=download&id=14brdTPVAqx6SYMAnL1_FyC611T1tPh5l",
}
# Minimaler CSS zur Anpassung des Layouts
CUSTOM_CSS = """
/* ... (Dein vorhandener CSS-Code) ... */

/* Audio Player Styling */
.audio-player {
    display: flex;
    justify-content: center;
    margin-top: 10px;
    margin-bottom: 20px;
}

.audio-player audio {
    width: 90%; /* Breite des Audio-Players */
    height: 40px; /* Höhe anpassen */
}
"""

# Anwenden des CSS
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Oberes Viertel: Bild + Titel
st.image("piktogramm.png", use_container_width=True)
st.markdown("<h1>51 Minuten, 10.01.2024, 12.17 Uhr - München - Hören</h1>", unsafe_allow_html=True)

# Audioplayer-Sektion
st.markdown('<div class="audio-player">', unsafe_allow_html=True)
for audio_name, audio_url in audio_files.items():
    st.audio(audio_url, format="audio/mpeg")
st.markdown('</div>', unsafe_allow_html=True)

# Mittleres Viertel: Ausgabe-Textfeld (nur einmal)
st.text_area("Ausgabe", value=" ".join(st.session_state["logs"]), height=100)

# Buttons
cols_per_row = 4

def chunk_list(lst, n):
    """Teilt die Liste lst in Chunks von Größe n."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

st.markdown('<div class="button-container">', unsafe_allow_html=True)

for row_buttons in chunk_list(button_definitions, cols_per_row):
    cols = st.columns(cols_per_row)
    for col, label in zip(cols, row_buttons):
        with col:
            if st.button(label, key=label):
                current_time = time.time()
                if current_time - st.session_state["last_click_time"] < 1:
                    st.warning("Bitte warte 1 Sekunde zwischen den Klicks!")
                else:
                    st.session_state["last_click_time"] = current_time
                    st.session_state["logs"].append(label)

st.markdown('</div>', unsafe_allow_html=True)