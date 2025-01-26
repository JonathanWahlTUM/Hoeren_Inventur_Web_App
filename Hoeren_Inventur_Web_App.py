import streamlit as st
import time

# Seitenkonfiguration für optimales Layout auf Mobilgeräten
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

# Session State für 1-Sekunden-Sperre und Logs
if "last_click_time" not in st.session_state:
    st.session_state["last_click_time"] = 0.0

if "logs" not in st.session_state:
    st.session_state["logs"] = []

# Minimaler CSS zur Anpassung des Layouts
custom_css = """
<style>
    /* Überschrift verkleinern */
    h1 {
        font-size: 20px !important;
        text-align: center !important;
        margin-top: 10px;
        margin-bottom: 20px;
    }

    /* Buttons Styling */
    .button-container {
        display: flex;
        flex-wrap: wrap;
        gap: 5px;
        justify-content: center;
        padding: 10px 0;
    }

    .stButton > button {
        font-size: 14px !important;
        padding: 5px 10px !important;
        height: 35px !important;
        min-width: 70px !important;
        margin: 0 !important;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s;
    }

    .stButton > button:hover {
        background-color: #0056b3 !important;
    }

    /* Responsive Anpassungen */
    @media (max-width: 768px) {
        .stButton > button {
            font-size: 12px !important;
            padding: 4px 8px !important;
            height: 30px !important;
            min-width: 60px !important;
        }
    }
</style>
"""

# Anwenden des CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Oberes Viertel: Bild + Titel
st.image("piktogramm.png", use_container_width=True)
st.markdown("<h1>51 Minuten, 10.01.2024, 12.17 Uhr - München - Hören</h1>", unsafe_allow_html=True)

# Button-Container starten
st.markdown('<div class="button-container">', unsafe_allow_html=True)

# Platzieren der Buttons innerhalb des Flex-Containers
for label in button_definitions:
    if st.button(label, key=label):
        current_time = time.time()
        if current_time - st.session_state["last_click_time"] < 1:
            st.warning("Bitte warte 1 Sekunde zwischen den Klicks!")
        else:
            st.session_state["last_click_time"] = current_time
            st.session_state["logs"].append(label)

# Button-Container schließen
st.markdown('</div>', unsafe_allow_html=True)

# Unteres Viertel: Textfeld für die Logs
st.text_area("Ausgabe", value=" ".join(st.session_state["logs"]), height=100)