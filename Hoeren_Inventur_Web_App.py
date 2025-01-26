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

# Minimaler CSS zur Anpassung des Layouts
custom_css = """
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
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(60px, 1fr));
        gap: 5px;
        justify-items: center;
        padding: 10px 0;
    }

    /* Buttons Styling */
    .button-container button {
        width: 100%;
        max-width: 80px;
        font-size: 14px;
        padding: 5px 10px;
        height: 35px;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s;
        box-sizing: border-box;
    }

    .button-container button:hover {
        background-color: #0056b3;
    }

    /* Responsive Anpassungen */
    @media (max-width: 768px) {
        .button-container button {
            font-size: 12px;
            padding: 4px 8px;
            height: 30px;
            max-width: 70px;
            min-width: 50px;
        }
    }

    /* Verberge das "Letzter Klick" Textfeld */
    #streamlit-data {
        display: none;
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

# Anwenden des CSS, der Buttons und des JavaScript-Codes
st.markdown(custom_css + f'<div class="button-container">{button_html}</div>' + js_code, unsafe_allow_html=True)

# Streamlit Event-Handler, um das geklickte Element zu speichern
# Verwende ein verstecktes Textfeld, um den Wert zu erfassen
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

# Unteres Viertel: Textfeld für die Logs
st.text_area("Ausgabe", value=" ".join(st.session_state["logs"]), height=100)