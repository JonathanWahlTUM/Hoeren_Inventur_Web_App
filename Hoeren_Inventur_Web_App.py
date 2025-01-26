import streamlit as st
import time

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
    }

    /* Buttons in Reihen von je 3 oder 2 anzeigen */
    .stButton>button {
        width: 30% !important;
        font-size: 14px !important;
        margin: 5px auto !important;
        display: inline-block !important;
    }

    /* Textfeld an unteres Viertel anpassen */
    .stTextArea textarea {
        font-size: 14px !important;
        height: 100px !important;
    }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Oberes Viertel: Bild + Titel
st.image("piktogramm.png", use_container_width=True)
st.markdown("<h1>51 Minuten, 10.01.2024, 12.17 Uhr - München - Hören</h1>", unsafe_allow_html=True)

# Session State für 1-Sekunden-Sperre
if "last_click_time" not in st.session_state:
    st.session_state["last_click_time"] = 0.0

if "logs" not in st.session_state:
    st.session_state["logs"] = []

button_definitions = [
    "Warnsignal", "Autogeräusche", "Zuggeräusche", "Busgeräusche",
    "Motorrollergeräusche", "Schritte", "Stimmen", "Fahrstuhl",
    "Husten", "Durchsage", "Rascheln", "Klappern",
    "Bremsgeräusch", "Läuten", "Vogelzwitschern", "Rolltreppe",
    "Tür", "Hupen", "Sirenen", "Wind"
]

# Buttons in zwei oder drei Reihen anzeigen
cols = st.columns(3)  # 3 Spalten für mobile Ansicht

for i, label in enumerate(button_definitions):
    col_index = i % 3  # Verteilt Buttons auf 3 Spalten
    with cols[col_index]:
        if st.button(label):
            current_time = time.time()
            if current_time - st.session_state["last_click_time"] < 1:
                st.warning("Bitte warte 1 Sekunde zwischen den Klicks!")
            else:
                st.session_state["last_click_time"] = current_time
                st.session_state["logs"].append(label)

# Unteres Viertel: Textfeld für die Logs
st.text_area("Ausgabe", value=" ".join(st.session_state["logs"]), height=100)