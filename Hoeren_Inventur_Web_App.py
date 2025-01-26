import streamlit as st
import time

st.set_page_config(
    page_title="Hören Inventur Web App",
    layout="centered"
)

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

# Wir wollen z. B. 3 Spalten
N_COLS = 3
cols = st.columns(N_COLS)

for i, label in enumerate(button_definitions):
    # Button in die passende Spalte schreiben
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