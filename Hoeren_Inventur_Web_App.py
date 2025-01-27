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

# Funktion zum Aufteilen der Liste in Chunks
def chunk_list(lst, n):
    """Teilt die Liste lst in Chunks von Größe n."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

# Buttons: Arrange in a grid-like pattern (4 columns per row)
cols_per_row = 4  # Anzahl der Spalten pro Zeile (für ein 4x5 Grid)

for row_buttons in chunk_list(button_definitions, cols_per_row):
    cols = st.columns(cols_per_row)
    for col, label in zip(cols, row_buttons):
        with col:
            if st.button(label, key=label):
                current_time = time.time()
                # Prüfe die 1-Sekunden-Sperre
                if current_time - st.session_state["last_click_time"] < 1:
                    st.warning("noch keine Sekunde vergangen")
                else:
                    st.session_state["last_click_time"] = current_time
                    st.session_state["logs"].append(label)