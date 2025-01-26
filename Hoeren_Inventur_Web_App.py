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

# Oberes Viertel: Bild + Titel
st.image("piktogramm.png", use_container_width=True)
st.markdown("""
    <h1 style='font-size:20px; text-align:center; margin-top:10px; margin-bottom:20px;'>
        51 Minuten, 10.01.2024, 12.17 Uhr - München - Hören
    </h1>
    """, unsafe_allow_html=True)

# Anzahl der Spalten pro Zeile
cols_per_row = 3  # Passe dies je nach Bildschirmgröße an (z.B. 2 für Mobile)

# Platzieren der Buttons in mehreren Spalten
for i in range(0, len(button_definitions), cols_per_row):
    # Erstelle eine Zeile mit `cols_per_row` Spalten
    cols = st.columns(cols_per_row)
    for j, label in enumerate(button_definitions[i:i + cols_per_row]):
        with cols[j]:
            if st.button(label, key=label):
                current_time = time.time()
                if current_time - st.session_state["last_click_time"] < 1:
                    st.warning("Bitte warte 1 Sekunde zwischen den Klicks!")
                else:
                    st.session_state["last_click_time"] = current_time
                    st.session_state["logs"].append(label)

# Unteres Viertel: Textfeld für die Logs
st.text_area("Ausgabe", value=" ".join(st.session_state["logs"]), height=100)