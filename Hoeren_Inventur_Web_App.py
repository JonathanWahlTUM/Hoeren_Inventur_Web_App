import streamlit as st
import time

# Seitenkonfiguration für optimales Layout auf Mobilgeräten
st.set_page_config(
    page_title="Hören Inventur Web App",
    layout="centered"  # Alternativ 'wide' ausprobieren
)

# CSS zur Anpassung des Layouts auf mobilen Geräten
CUSTOM_CSS = """
<style>
    /* Überschrift verkleinern */
    h1 {
        font-size: 20px !important;
        text-align: center !important;
        margin-top: 10px;
        margin-bottom: 20px;
    }

    /* Buttons Styling */
    .stButton>button {
        font-size: 14px !important;
        padding: 5px !important;
        height: 35px !important;
        min-width: 70px; /* Mindestbreite für Buttons */
        margin: 2px; /* Minimaler Abstand zwischen Buttons */
    }

    /* Textfeld an unteres Viertel anpassen */
    .stTextArea textarea {
        font-size: 14px !important;
        height: 100px !important;
    }

    /* Flexbox Layout für Buttons */
    .button-container {
        display: flex;
        flex-wrap: wrap;
        gap: 5px; /* Abstand zwischen den Buttons */
        justify-content: center; /* Zentriert die Buttons horizontal */
        padding: 10px;
    }

    @media (max-width: 768px) {
        .button-container {
            gap: 3px; /* Weniger Abstand auf kleineren Bildschirmen */
        }
    }
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Oberes Viertel: Bild + Titel
st.image("piktogramm.png", use_container_width=True)
st.markdown("<h1>51 Minuten, 10.01.2024, 12.17 Uhr - München - Hören</h1>", unsafe_allow_html=True)

# Liste der Button-Beschriftungen
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

# Container für die Buttons mit Flexbox
st.markdown('<div class="button-container">', unsafe_allow_html=True)

# Platzieren der Buttons innerhalb des Flex-Containers
for label in button_definitions:
    # Jeder Button erhält einen eindeutigen Schlüssel
    if st.button(label, key=label):
        current_time = time.time()
        if current_time - st.session_state["last_click_time"] < 1:
            st.warning("Bitte warte 1 Sekunde zwischen den Klicks!")
        else:
            st.session_state["last_click_time"] = current_time
            st.session_state["logs"].append(label)

st.markdown('</div>', unsafe_allow_html=True)

# Unteres Viertel: Textfeld für die Logs
st.text_area("Ausgabe", value=" ".join(st.session_state["logs"]), height=100)