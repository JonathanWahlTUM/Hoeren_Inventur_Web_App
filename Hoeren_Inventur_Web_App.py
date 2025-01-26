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
        margin: 1px; /* Minimaler Abstand zwischen Buttons */
    }

    /* Textfeld an unteres Viertel anpassen */
    .stTextArea textarea {
        font-size: 14px !important;
        height: 100px !important;
    }

    /* Override columns stacking auf mobilen Geräten für drei Spalten */
    @media (max-width: 768px) {
        /* Zwinge Streamlit-Spalten, drei Spalten nebeneinander zu bleiben */
        div[data-testid^="column"] > div {
            flex: 0 0 30% !important; /* Drei Spalten à 30% */
            max-width: 30% !important;
            margin: 1.66% !important; /* Minimaler Abstand zwischen den Spalten */
        }
    }

    /* Zusätzliche Anpassungen für sehr kleine Bildschirme */
    @media (max-width: 480px) {
        div[data-testid^="column"] > div {
            flex: 0 0 48% !important; /* Zwei Spalten à 48% */
            max-width: 48% !important;
            margin: 1% !important; /* Minimaler Abstand zwischen den Spalten */
        }
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

# Anzahl der Spalten pro Reihe (3 für Desktop und Landscape, 2 für Portrait)
buttons_per_row = 3

# Funktion zur Aufteilung der Buttons in Gruppen
def chunked(iterable, n):
    """Teilt eine Liste in Gruppen der Größe n."""
    for i in range(0, len(iterable), n):
        yield iterable[i:i + n]

# Erstelle die Button-Reihen
for row in chunked(button_definitions, buttons_per_row):
    cols = st.columns(buttons_per_row)
    for col, label in zip(cols, row):
        with col:
            if st.button(label):
                current_time = time.time()
                if current_time - st.session_state["last_click_time"] < 1:
                    st.warning("Bitte warte 1 Sekunde zwischen den Klicks!")
                else:
                    st.session_state["last_click_time"] = current_time
                    st.session_state["logs"].append(label)

# Unteres Viertel: Textfeld für die Logs
st.text_area("Ausgabe", value=" ".join(st.session_state["logs"]), height=100)