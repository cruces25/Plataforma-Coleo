import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Quinielas de Coleo", layout="centered")

# Tu diccionario de credenciales ya funciona correctamente
creds_dict = {
    # ... (mantén tu diccionario exacto como lo tienes ahora) ...
}

def get_client():
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
    return gspread.authorize(creds)

st.title("🏆 Plataforma de Quinielas de Coleo")

try:
    client = get_client()
    # Asegúrate de que el nombre del archivo sea exactamente "BaseDatosColeo"
    sheet = client.open("BaseDatosColeo")
    hoja = sheet.worksheet("Cuadros")
    
    st.success("¡Conexión exitosa con Google Sheets!")

    # Formulario para capturar los datos
    with st.form("registro_cuadro"):
        nombre = st.text_input("Nombre del Participante")
        whatsapp = st.text_input("Número de WhatsApp")
        c1 = st.text_input("Coleador 1")
        c2 = st.text_input("Coleador 2")
        c3 = st.text_input("Coleador 3")
        c4 = st.text_input("Coleador 4")
        
        btn_enviar = st.form_submit_button("Registrar Cuadro")
        
        if btn_enviar:
            if nombre and whatsapp:
                hoja.append_row([nombre, whatsapp, c1, c2, c3, c4])
                st.success("¡Cuadro registrado con éxito!")
            else:
                st.error("Por favor, completa al menos el nombre y WhatsApp.")

except Exception as e:
    st.error(f"Error al conectar con la hoja: {e}")
