import streamlit as st
import time

# Seitenkonfiguration
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

# Bild und Titel
st.image("piktogramm.png", use_container_width=True)
st.markdown("""
    <h1 style='text-align: center; font-size: 20px;'>
        51 Minuten, 10.01.2024, 12.17 Uhr - München - Hören
    </h1>
    """, unsafe_allow_html=True)

# Ausgabe-Textfeld (nur einmal)
st.text_area("Ausgabe", value=" ".join(st.session_state["logs"]), height=100)

# Buttons: Arrange in multiple rows with 2 columns per row
cols_per_row = 2  # Für bessere mobile Darstellung

for i in range(0, len(button_definitions), cols_per_row):
    cols = st.columns(cols_per_row)
    for j, label in enumerate(button_definitions[i:i + cols_per_row]):
        with cols[j]:
            if st.button(label, key=label):
                current_time = time.time()
                # Prüfe die 1-Sekunden-Sperre
                if current_time - st.session_state["last_click_time"] < 1:
                    st.warning("Bitte warte 1 Sekunde zwischen den Klicks!")
                else:
                    st.session_state["last_click_time"] = current_time
                    st.session_state["logs"].append(label)