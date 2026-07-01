import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

st.set_page_config(page_title="Quinielas", page_icon="🏆")
st.title("🏆 Plataforma de Quinielas de Coleo")

# Conectar a Google Sheets
try:
    creds = Credentials.from_service_account_info(
        st.secrets["gcp"],
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    client = gspread.authorize(creds)
    # COPIA LA URL DE TU HOJA Y PEGALA ABAJO
    hoja = client.open_by_url("https://docs.google.com/spreadsheets/d/1GIHAS9zvV32vyj-PKxM7W8YC4gL4qGSSIsUb8MMVhzs/edit").worksheet("Cuadros")
    st.success("¡Conexión lista!")
except Exception as e:
    st.error(f"Error: {e}")
    st.stop()

# Formulario
with st.form("registro"):
    nombre = st.text_input("Nombre del Participante")
    whatsapp = st.text_input("WhatsApp")
    c1 = st.text_input("Coleador 1")
    c2 = st.text_input("Coleador 2")
    c3 = st.text_input("Coleador 3")
    c4 = st.text_input("Coleador 4")
    
    if st.form_submit_button("Guardar Cuadro"):
        hoja.append_row([nombre, whatsapp, c1, c2, c3, c4])
        st.success("¡Guardado correctamente!")
