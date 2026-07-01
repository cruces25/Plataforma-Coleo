import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

st.set_page_config(page_title="Quinielas de Coleo")

def get_client():
    # Carga las credenciales desde los Secrets definidos arriba
    creds = Credentials.from_service_account_info(
        st.secrets["gcp"],
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    return gspread.authorize(creds)

st.title("🏆 Registro de Quinielas")

# Formulario
with st.form("registro_cuadros"):
    participante = st.text_input("Nombre del Participante")
    whatsapp = st.text_input("WhatsApp")
    c1 = st.text_input("Coleador 1")
    c2 = st.text_input("Coleador 2")
    c3 = st.text_input("Coleador 3")
    c4 = st.text_input("Coleador 4")
    
    enviar = st.form_submit_button("Guardar Cuadro")
    
    if enviar:
        if participante and whatsapp:
            try:
                client = get_client()
                hoja = client.open("BaseDatosColeo").worksheet("Cuadros")
                hoja.append_row([participante, whatsapp, c1, c2, c3, c4])
                st.success("¡Cuadro registrado correctamente!")
            except Exception as e:
                st.error(f"Error al guardar: {e}")
        else:
            st.warning("Por favor, rellena al menos el Nombre y WhatsApp.")
