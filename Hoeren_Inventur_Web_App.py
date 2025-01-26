import streamlit as st
import time

# Seitenkonfiguration für optimales Layout auf Mobilgeräten
st.set_page_config(
    page_title="Hören Inventur Web App",
    layout="centered"
)

# CSS zur Anpassung des Layouts für einen Fließtext-Stil
CUSTOM_CSS = """
<style>
    .button-container {
        display: block;
        white-space: nowrap;
        overflow-x: auto;
    }

    .stButton>button {
        display: inline-block;
        font-size: 14px !important;
        padding: 5px 10px !important;
        height: 40px !important;
        margin-right: 5px;
    }
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Oberes Viertel: Bild + Titel
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

# Platzieren der Buttons innerhalb des Flex-Containers für Fließtext-Anordnung
st.markdown('<div class="button-container">', unsafe_allow_html=True)

for label in button_definitions:
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