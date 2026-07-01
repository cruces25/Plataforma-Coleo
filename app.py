import streamlit as st
import gspread
import json
from google.oauth2.service_account import Credentials

st.title("🏆 Plataforma de Quinielas de Coleo")

# Función de conexión simplificada
def conectar_sheets():
    # Abrimos el archivo que acabas de subir al repositorio
    with open('gcp_key.json', 'r') as f:
        creds_dict = json.load(f)
    
    creds = Credentials.from_service_account_info(
        creds_dict,
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    return gspread.authorize(creds)

# Intentar conectar
try:
    client = conectar_sheets()
    hoja = client.open("BaseDatosColeo").worksheet("Cuadros")
except Exception as e:
    st.error(f"Error al conectar con la hoja: {e}")
    st.stop()

# Formulario
with st.form("registro_cuadros"):
    st.subheader("Registrar nuevo cuadro")
    participante = st.text_input("Nombre del Participante")
    whatsapp = st.text_input("WhatsApp")
    c1 = st.text_input("Coleador 1")
    c2 = st.text_input("Coleador 2")
    c3 = st.text_input("Coleador 3")
    c4 = st.text_input("Coleador 4")
    
    enviar = st.form_submit_button("Guardar Cuadro")

    if enviar:
        if not participante or not whatsapp:
            st.warning("Por favor, completa al menos el nombre y WhatsApp.")
        else:
            try:
                hoja.append_row([participante, whatsapp, c1, c2, c3, c4])
                st.success(f"¡Cuadro de {participante} registrado con éxito!")
            except Exception as e:
                st.error(f"Error al guardar: {e}")
