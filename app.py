import streamlit as st
import gspread
import json
from google.oauth2.service_account import Credentials

st.title("🏆 Registro de Quinielas")

def conectar_sheets():
    # Lee el archivo que acabas de subir al repositorio
    with open('gcp_key.json') as f:
        creds_dict = json.load(f)
    
    creds = Credentials.from_service_account_info(
        creds_dict,
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    return gspread.authorize(creds)

# Inicializar conexión
try:
    client = conectar_sheets()
    hoja = client.open("BaseDatosColeo").worksheet("Cuadros")
except Exception as e:
    st.error(f"Error al conectar: {e}")
    st.stop()

# Formulario
with st.form("registro"):
    nombre = st.text_input("Nombre del Participante")
    tel = st.text_input("WhatsApp")
    c1 = st.text_input("Coleador 1")
    c2 = st.text_input("Coleador 2")
    c3 = st.text_input("Coleador 3")
    c4 = st.text_input("Coleador 4")
    enviar = st.form_submit_button("Guardar Cuadro")

    if enviar:
        if nombre and tel:
            try:
                hoja.append_row([nombre, tel, c1, c2, c3, c4])
                st.success("¡Guardado correctamente!")
            except Exception as e:
                st.error(f"Error al guardar: {e}")
        else:
            st.warning("Nombre y WhatsApp son obligatorios.")
