import streamlit as st
import time

# Seitenkonfiguration
st.set_page_config(
    page_title="Hören Inventur Web App",
    layout="centered"
)

# Button-Beschriftungen
button_definitions = [
    "Warnsignal", "Autogeräusche", "Zuggeräusche", "Busgeräusche",
    "Motorrollergeräusche", "Schritte", "Stimmen", "Fahrstuhl",
    "Husten", "Durchsage", "Rascheln", "Klappern",
    "Bremsgeräusch", "Läuten", "Vogelzwitschern", "Rolltreppe",
    "Tür", "Hupen", "Sirenen", "Wind"
]

# Session State
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

# Minimaler CSS zur Anpassung des Layouts (nur einmal)
custom_css = """
<style>
    /* Container für die Buttons */
    .button-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(80px, 1fr));
        gap: 5px;
        justify-items: center;
        padding: 10px 0;
    }

    /* Buttons Styling */
    .button-container button {
        width: 100%;
        max-width: 120px;
        font-size: 14px;
        padding: 8px;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s;
    }

    .button-container button:hover {
        background-color: #0056b3;
    }

    /* Responsive Anpassungen */
    @media (max-width: 768px) {
        .button-container button {
            font-size: 12px;
            padding: 6px;
            max-width: 100px;
        }
    }
</style>
"""

# JavaScript für Button-Handling
js_code = """
<script>
    function send_value(value) {
        var streamlit_data = window.parent.document.getElementById("streamlit-data");
        if(streamlit_data){
            streamlit_data.value = value;
            streamlit_data.dispatchEvent(new Event('input'));
        }
    }
</script>
<input type="hidden" id="streamlit-data" />
"""

# HTML-Buttons als Fließtext-Elemente
button_html = " ".join([
    f'<button onclick="send_value(\'{label}\')">{label}</button>' for label in button_definitions
])

# Anwenden des CSS, der Buttons und des JavaScript-Codes (nur einmal)
st.markdown(custom_css + f'<div class="button-container">{button_html}</div>' + js_code, unsafe_allow_html=True)

# Streamlit Event-Handler, um das geklickte Element zu speichern (nur einmal)
clicked_button = st.text_input("", key="streamlit-data", value="", placeholder="", label_visibility="hidden")

# Wenn ein Button geklickt wird, speichere ihn im Session State
if clicked_button:
    current_time = time.time()
    if current_time - st.session_state["last_click_time"] < 1:
        st.warning("Bitte warte 1 Sekunde zwischen den Klicks!")
    else:
        st.session_state["last_click_time"] = current_time
        st.session_state["logs"].append(clicked_button)
        # Leere das versteckte Textfeld nach dem Speichern
        st.session_state["streamlit-data"] = ""

# Ausgabe-Textfeld aktualisieren (nur einmal)
st.text_area("Ausgabe", value=" ".join(st.session_state["logs"]), height=100)