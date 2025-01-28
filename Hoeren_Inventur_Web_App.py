import streamlit as st
import time
import os

# Seitenkonfiguration für optimales Layout auf Mobilgeräten
st.set_page_config(
    page_title="Hören Inventur Web App",
    layout="centered"  # Optimal für mobile Geräte
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

if "current_audio" not in st.session_state:
    st.session_state["current_audio"] = None

# Minimaler CSS zur Anpassung des Layouts
CUSTOM_CSS = """
<style>
    /* Überschrift verkleinern und zentrieren */
    h1 {
        font-size: 24px !important;
        text-align: center !important;
        margin-top: 10px;
        margin-bottom: 20px;
    }

    /* Button-Container mit Flexbox */
    .button-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center; /* Zentriert die Buttons */
        gap: 10px; /* Abstand zwischen den Buttons */
        padding: 10px 0;
    }

    /* Buttons Styling */
    .stButton > button {
        font-size: 14px !important; /* Kleinere Schriftgröße */
        padding: 8px 16px !important; /* Verkleinertes Padding */
        height: 40px !important; /* Verkleinerte Höhe */
        min-width: 100px !important; /* Verkleinerte Mindestbreite */
        max-width: 150px !important; /* Verkleinerte Maximalbreite */
        background-color: #007bff !important; /* Button-Farbe */
        color: white !important; /* Textfarbe */
        border: none !important; /* Kein Rahmen */
        border-radius: 8px !important; /* Abgerundete Ecken */
        cursor: pointer !important; /* Cursor ändert sich zu Pointer */
        white-space: nowrap !important; /* Verhindert Textumbruch */
        overflow: hidden !important; /* Versteckt überflüssigen Text */
        text-overflow: ellipsis !important; /* Fügt "..." hinzu, wenn der Text zu lang ist */
        transition: background-color 0.3s !important; /* Hover-Effekt */
    }

    .stButton > button:hover {
        background-color: #0056b3 !important; /* Dunklere Farbe beim Hover */
    }

    /* Responsive Anpassungen */
    @media (max-width: 768px) {
        .stButton > button {
            font-size: 12px !important; /* Noch kleinere Schriftgröße */
            padding: 6px 12px !important; /* Noch kleineres Padding */
            height: 35px !important; /* Noch kleinere Höhe */
            min-width: 80px !important; /* Noch kleinere Mindestbreite */
            max-width: 130px !important; /* Noch kleinere Maximalbreite */
        }
    }
</style>
"""

# Anwenden des CSS
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Oberes Viertel: Bild + Titel
image_path = "audio_files/piktogramm.png"
if os.path.exists(image_path):
    st.image(image_path, use_container_width=True)
else:
    st.error(f"Bild nicht gefunden: {image_path}")

st.markdown("<h1>51 Minuten, 10.01.2024, 12.17 Uhr - München - Hören</h1>", unsafe_allow_html=True)

# **Neuer Abschnitt: Drei unabhängige Audio-Player**
st.markdown("### Audio-Player")
st.markdown("<hr>", unsafe_allow_html=True)

# Platzierung der drei Audio-Player
audio_players = [
    {
        "title": "Aufnahme Heimweg",
        "url": "https://tumde-my.sharepoint.com/:u:/g/personal/jonathan_wahl_tum_de/EV1l_2BCE8NOtKIgiOUzSw4BW7n3WxuKOuSdex8yyl6yIA/download?version=1.0"
    },
    {
        "title": "Aufnahme Türen",
        "url": "https://tumde-my.sharepoint.com/:u:/g/personal/jonathan_wahl_tum_de/DummyLink_Tueren/download?version=1.0"
    },
    {
        "title": "Noise Cancelling",
        "url": "https://tumde-my.sharepoint.com/:u:/g/personal/jonathan_wahl_tum_de/DummyLink_NoiseCancelling/download?version=1.0"
    }
]

for player in audio_players:
    st.subheader(player["title"])
    st.audio(player["url"], format='audio/mp3')
    st.markdown("<br>", unsafe_allow_html=True)

# Mittleres Viertel: Ausgabe-Textfeld (nur einmal)
st.markdown("<hr>", unsafe_allow_html=True)
st.text_area("Ausgabe", value=" ".join(st.session_state["logs"]), height=100)

# Funktion zum Aufteilen der Liste in Chunks
def chunk_list(lst, n):
    """Teilt die Liste lst in Chunks von Größe n."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

# Buttons: Arrange in a grid-like pattern (z.B. 4 Spalten pro Reihe)
cols_per_row = 4  # Anzahl der Spalten pro Zeile

# Wrapper für die Button-Anordnung im Grid
st.markdown('<div class="button-container">', unsafe_allow_html=True)

for row_buttons in chunk_list(button_definitions, cols_per_row):
    cols = st.columns(cols_per_row)
    for col, label in zip(cols, row_buttons):
        with col:
            if st.button(label, key=label):
                current_time = time.time()
                # Prüfe die 1-Sekunden-Sperre
                if current_time - st.session_state["last_click_time"] < 1:
                    st.warning("Bitte warte 1 Sekunde zwischen den Klicks!")
                else:
                    st.session_state["last_click_time"] = current_time
                    st.session_state["logs"].append(label)
                    # Audio abspielen
                    st.audio(button_definitions[label], format='audio/mp3')

st.markdown('</div>', unsafe_allow_html=True)