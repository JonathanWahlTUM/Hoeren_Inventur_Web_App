import streamlit as st
import time
from math import ceil

# Seitenkonfiguration für optimales Layout auf Mobilgeräten
st.set_page_config(
    page_title="Hören Inventur Web App",
    layout="centered"
)

# CSS für mobile Geräte – Anordnung und Schriftgröße anpassen
CUSTOM_CSS = """
<style>
    /* Anpassung der gesamten App-Padding für Mobilgeräte */
    .stApp {
        padding: 5px !important;
    }

    /* Überschrift verkleinern */
    h1 {
        font-size: 20px !important;
        text-align: center !important;
        margin-top: 10px;
    }

    /* Buttons styling */
    .stButton>button {
        font-size: 14px !important;
        padding: 8px !important;
        /* Entferne die feste Breite, damit die Buttons in Spalten passen */
        /* width: 100% !important; */
        height: 40px !important;
    }

    /* Textfeld an unteres Viertel anpassen */
    .stTextArea textarea {
        font-size: 14px !important;
        height: 100px !important;
    }

    /* Abstand zwischen den Button-Reihen */
    .button-row {
        margin-bottom: 10px;
    }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Funktion zur Aufteilung der Buttons in Gruppen
def chunked(iterable, n):
    """Teilt eine Liste in Gruppen der Größe n."""
    for i in range(0, len(iterable), n):
        yield iterable[i:i + n]

# Oberes Viertel: Bild + Titel
with st.container():
    st.image("piktogramm.png", use_container_width=True)
    st.markdown("<h1>51 Minuten, 10.01.2024, 12.17 Uhr - München - Hören</h1>", unsafe_allow_html=True)

# Mittlere zwei Viertel: Buttons
button_definitions = [
    "Warnsignal", "Autogeräusche", "Zuggeräusche", "Busgeräusche",
    "Motorrollergeräusche", "Schritte", "Stimmen", "Fahrstuhl",
    "Husten", "Durchsage", "Rascheln", "Klappern",
    "Bremsgeräusch", "Läuten", "Vogelzwitschern", "Rolltreppe",
    "Tür", "Hupen", "Sirenen", "Wind"
]

# Session State für 1-Sekunden-Sperre und Logs
if "last_click_time" not in st.session_state:
    st.session_state["last_click_time"] = 0.0

if "logs" not in st.session_state:
    st.session_state["logs"] = []

# Anzahl der Spalten pro Reihe (2 für mobile Optimierung)
buttons_per_row = 2  # Du kannst hier auf 3 ändern, wenn gewünscht

# Erstelle die Button-Reihen
for row in chunked(button_definitions, buttons_per_row):
    cols = st.columns(buttons_per_row)
    for idx, label in enumerate(row):
        with cols[idx]:
            if st.button(label):
                current_time = time.time()
                if current_time - st.session_state["last_click_time"] < 1:
                    st.warning("Bitte warte 1 Sekunde zwischen den Klicks!")
                else:
                    st.session_state["last_click_time"] = current_time
                    st.session_state["logs"].append(label)

# Unteres Viertel: Textfeld für die Logs
with st.container():
    st.text_area("Ausgabe", value=" ".join(st.session_state["logs"]), height=100)