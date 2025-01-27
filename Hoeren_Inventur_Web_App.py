import streamlit as st
import time

# Seitenkonfiguration für optimales Layout auf Mobilgeräten
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

# Minimaler CSS zur Anpassung des Layouts
CUSTOM_CSS = """
<style>
    /* Überschrift verkleinern und zentrieren */
    h1 {
        font-size: 20px !important;
        text-align: center !important;
        margin-top: 10px;
        margin-bottom: 20px;
    }

    /* Container für die Buttons */
    .button-container {
        display: flex;
        justify-content: center; /* Zentriert die Buttons */
        flex-wrap: wrap; /* Ermöglicht das Umbrechen bei kleineren Bildschirmen */
        gap: 10px; /* Abstand zwischen den Buttons */
        padding: 10px 0;
    }

    /* Buttons Styling */
    .stButton > button {
        font-size: 16px !important; /* Größere Schriftgröße */
        padding: 10px 20px !important; /* Größeres Padding */
        height: 50px !important; /* Größere Höhe */
        min-width: 120px !important; /* Mindestbreite erhöhen */
        max-width: 200px !important; /* Maximale Breite festlegen */
        background-color: #007bff !important; /* Button-Farbe */
        color: white !important; /* Textfarbe */
        border: none !important; /* Kein Rahmen */
        border-radius: 8px !important; /* Abgerundete Ecken */
        cursor: pointer !important; /* Cursor ändert sich zu Pointer */
        transition: background-color 0.3s !important; /* Hover-Effekt */
    }

    .stButton > button:hover {
        background-color: #0056b3 !important; /* Dunklere Farbe beim Hover */
    }

    /* Responsive Anpassungen */
    @media (max-width: 768px) {
        .stButton > button {
            font-size: 14px !important;
            padding: 8px 16px !important;
            height: 45px !important;
            min-width: 100px !important;
            max-width: 150px !important;
        }
    }
</style>
"""

# Anwenden des CSS
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Oberes Viertel: Bild + Titel
st.image("piktogramm.png", use_container_width=True)
st.markdown("<h1>51 Minuten, 10.01.2024, 12.17 Uhr - München - Hören</h1>", unsafe_allow_html=True)

# Mittleres Viertel: Ausgabe-Textfeld (nur einmal)
st.text_area("Ausgabe", value=" ".join(st.session_state["logs"]), height=100)

# Buttons: Arrange in two rows
# Teilen der Button-Liste in zwei Hälften
mid_index = len(button_definitions) // 2
first_half = button_definitions[:mid_index]
second_half = button_definitions[mid_index:]

def create_button_row(buttons):
    # Anzahl der Spalten pro Reihe anpassen, z.B. 5 pro Reihe für 10 Buttons insgesamt
    cols_per_row = len(buttons)  # Alle Buttons in einer Reihe
    cols = st.columns(cols_per_row)
    for i, label in enumerate(buttons):
        with cols[i]:
            if st.button(label, key=label):
                current_time = time.time()
                # Prüfe die 1-Sekunden-Sperre
                if current_time - st.session_state["last_click_time"] < 1:
                    st.warning("Bitte warte 1 Sekunde zwischen den Klicks!")
                else:
                    st.session_state["last_click_time"] = current_time
                    st.session_state["logs"].append(label)

# Erste Reihe der Buttons
create_button_row(first_half)

# Zweite Reihe der Buttons
create_button_row(second_half)