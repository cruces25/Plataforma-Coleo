import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

st.title("🏆 Plataforma de Quinielas de Coleo")

# Conectamos con los datos guardados en la caja fuerte (Secrets)
try:
    creds = Credentials.from_service_account_info(
        st.secrets["gcp"],
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    client = gspread.authorize(creds)
    # Abre tu hoja con el ID (sin toda la URL, solo el código largo)
    # Tu ID es: 1GIHAS9zvV32vyj-PKxM7W8YC4gL4qGSSIsUb8MMVhzs
    hoja = client.open_by_key("1GIHAS9zvV32vyj-PKxM7W8YC4gL4qGSSIsUb8MMVhzs").worksheet("Cuadros")
    st.success("¡Conexión establecida con éxito!")
except Exception as e:
    st.error(f"Error al conectar: {e}")
    st.stop()

# Formulario para el usuario
with st.form("registro"):
    nombre = st.text_input("Nombre del Participante")
    whatsapp = st.text_input("WhatsApp")
    c1 = st.text_input("Coleador 1")
    c2 = st.text_input("Coleador 2")
    c3 = st.text_input("Coleador 3")
    c4 = st.text_input("Coleador 4")
    
    if st.form_submit_button("Guardar Cuadro"):
        hoja.append_row([nombre, whatsapp, c1, c2, c3, c4])
        st.success("¡Tu cuadro ha sido guardado!")
