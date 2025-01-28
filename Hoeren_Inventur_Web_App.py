import streamlit as st
import time
import requests

# Seitenkonfiguration für optimales Layout auf Mobilgeräten
st.set_page_config(
    page_title="Hören Inventur Web App",
    layout="centered"  # Optimal für mobile Geräte
)

# Dictionary der Button-Beschriftungen und zugehörige direkte Audio-URLs
button_definitions = {
    "Warnsignal": "https://tumde-my.sharepoint.com/:u:/g/personal/jonathan_wahl_tum_de/EZiuE-3m1DJEq2RSN3ArlF8BwTZXikdI28Vbxuwf7UI0Nw/download?version=1.0",
    "Autogeräusche": "https://tumde-my.sharepoint.com/:u:/g/personal/jonathan_wahl_tum_de/AnotherLink/download?version=1.0",
    "Zuggeräusche": "https://tumde-my.sharepoint.com/:u:/g/personal/jonathan_wahl_tum_de/ThirdLink/download?version=1.0",
    # Füge hier die restlichen Buttons und ihre direkten Audio-URLs hinzu
}

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
        font-size: 20px !important;
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
st.image("audio_files/piktogramm.png", use_container_width=True)
st.markdown("<h1>51 Minuten, 10.01.2024, 12.17 Uhr - München - Hören</h1>", unsafe_allow_html=True)

# Mittleres Viertel: Ausgabe-Textfeld (nur einmal)
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

for row_buttons in chunk_list(list(button_definitions.keys()), cols_per_row):
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
                    # Setze das aktuelle Audio
                    st.session_state["current_audio"] = button_definitions[label]

st.markdown('</div>', unsafe_allow_html=True)

# Anzeigen des Audio-Players und Download-Buttons, wenn ein Audio ausgewählt ist
if st.session_state["current_audio"]:
    # Audio-Player
    st.audio(st.session_state["current_audio"], format='audio/mp3')

    # Download-Button: Audio-Datei herunterladen
    try:
        response = requests.get(st.session_state["current_audio"])
        response.raise_for_status()
        audio_bytes = response.content
        st.download_button(
            label="Download Audio",
            data=audio_bytes,
            file_name=f"{st.session_state['logs'][-1]}.mp3",
            mime="audio/mpeg"
        )
    except requests.exceptions.RequestException as e:
        st.error(f"Fehler beim Laden der Audio-Datei: {e}")