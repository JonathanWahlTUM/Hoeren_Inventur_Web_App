import streamlit as st
import time

# Seitenkonfiguration für optimales Layout auf Mobilgeräten
st.set_page_config(
    page_title="Hören Inventur Web App",
    layout="centered"
)

# Oberes Viertel: Bild + Titel
st.image("piktogramm.png", use_container_width=True)
st.markdown("<h1 style='text-align: center;'>51 Minuten, 10.01.2024, 12.17 Uhr - München - Hören</h1>", unsafe_allow_html=True)

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

# Anzahl der Spalten festlegen (z.B. 4 für ein flüssiges Layout)
num_columns = 4
cols = st.columns(num_columns)

# Buttons in die Spalten verteilen
for index, label in enumerate(button_definitions):
    col = cols[index % num_columns]
    with col:
        if st.button(label, key=label):
            current_time = time.time()
            if current_time - st.session_state["last_click_time"] < 1:
                st.warning("Bitte warte 1 Sekunde zwischen den Klicks!")
            else:
                st.session_state["last_click_time"] = current_time
                st.session_state["logs"].append(label)

# Unteres Viertel: Textfeld für die Logs
st.text_area("Ausgabe", value=" ".join(st.session_state["logs"]), height=100)