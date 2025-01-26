import streamlit as st
import time

# Seitenkonfiguration für optimales Layout auf Mobilgeräten
st.set_page_config(
    page_title="Hören Inventur Web App",
    layout="centered"
)

# Dynamische Größenanpassung für mobile Geräte
CUSTOM_CSS = """
<style>
    @media only screen and (max-width: 768px) {
        .stButton>button {
            width: 100% !important;
            font-size: 14px !important;
            padding: 10px !important;
        }
        .stTextArea textarea {
            font-size: 14px !important;
        }
        .stApp {
            padding: 10px !important;
        }
    }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

st.image("piktogramm.png", use_container_width=True)
st.title("51 Minuten, 10.01.2024, 12.17 Uhr - München - Hören")

# Session State für 1-Sekunden-Sperre
if "last_click_time" not in st.session_state:
    st.session_state["last_click_time"] = 0.0

if "logs" not in st.session_state:
    st.session_state["logs"] = []

button_definitions = [
    "Warnsignal",
    "Autogeräusche",
    "Zuggeräusche",
    "Busgeräusche",
    "Motorrollergeräusche",
    "Schritte",
    "Stimmen",
    "Fahrstuhl",
    "Husten",
    "Durchsage",
    "Rascheln",
    "Klappern",
    "Bremsgeräusch",
    "Läuten",
    "Vogelzwitschern",
    "Rolltreppe",
    "Tür",
    "Hupen",
    "Sirenen",
    "Wind",
]

# Dynamische Anpassung der Spaltenanzahl für mobile Geräte
if st.session_state.get("is_mobile", False):
    N_COLS = 1  # Auf Mobilgeräten nur eine Spalte
else:
    N_COLS = 3  # Auf größeren Bildschirmen 3 Spalten

cols = st.columns(N_COLS)

for i, label in enumerate(button_definitions):
    col_index = i % N_COLS
    with cols[col_index]:
        if st.button(label):
            current_time = time.time()
            if current_time - st.session_state["last_click_time"] < 1:
                st.warning("Bitte warte 1 Sekunde zwischen den Klicks!")
            else:
                st.session_state["last_click_time"] = current_time
                st.session_state["logs"].append(label)

# Textbereich (unten)
st.text_area("Ausgabe", value=" ".join(st.session_state["logs"]), height=100)

# Erkennung von mobiler Ansicht durch Bildschirmgröße
if st.sidebar.button("Gerät testen"):
    width = st.sidebar.slider("Bildschirmbreite", min_value=300, max_value=1500, value=768)
    st.session_state["is_mobile"] = width < 768