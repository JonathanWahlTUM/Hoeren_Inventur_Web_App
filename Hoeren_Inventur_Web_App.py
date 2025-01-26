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

# CSS für horizontale Button-Anordnung als Fließtext
custom_css = """
<style>
    .button-container {
        white-space: nowrap; /* Verhindert Umbruch innerhalb einer Zeile */
        overflow-x: auto; /* Horizontales Scrollen bei Bedarf */
        display: flex;
        flex-wrap: wrap;
        gap: 5px;
        padding: 10px 0;
    }
    .button-container button {
        display: inline-block;
        background-color: #007bff;
        color: white;
        border: none;
        padding: 10px 15px;
        border-radius: 5px;
        cursor: pointer;
        font-size: 14px;
        transition: background-color 0.3s;
    }
    .button-container button:hover {
        background-color: #0056b3;
    }
</style>
"""

# HTML-Buttons als Fließtext-Elemente
button_html = " ".join([
    f'<button onclick="send_value(\'{label}\')">{label}</button>' for label in button_definitions
])

# JavaScript für Button-Handling
js_code = """
<script>
    function send_value(value) {
        var streamlit_data = window.parent.document.getElementById("streamlit-data");
        streamlit_data.value = value;
        streamlit_data.dispatchEvent(new Event('input'));
    }
</script>
<input type="hidden" id="streamlit-data" />
"""

# Ausgabe des CSS, der Buttons und des JavaScript-Codes
st.markdown(custom_css + f'<div class="button-container">{button_html}</div>' + js_code, unsafe_allow_html=True)

# Streamlit Event-Handler, um das geklickte Element zu speichern
clicked_button = st.text_input("Letzter Klick", key="streamlit-data", value="")

# Wenn ein Button geklickt wird, speichere ihn im Session State
if clicked_button:
    current_time = time.time()
    if current_time - st.session_state["last_click_time"] < 1:
        st.warning("Bitte warte 1 Sekunde zwischen den Klicks!")
    else:
        st.session_state["last_click_time"] = current_time
        st.session_state["logs"].append(clicked_button)

# Unteres Viertel: Textfeld für die Logs
st.text_area("Ausgabe", value=" ".join(st.session_state["logs"]), height=100)