import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Configuración de credenciales usando los Secretos de Streamlit
creds_dict = {
    "type": st.secrets["gcp"]["type"],
    "project_id": st.secrets["gcp"]["project_id"],
    "private_key_id": st.secrets["gcp"]["private_key_id"],
    "private_key": st.secrets["gcp"]["private_key"].replace("\\n", "\n"),
    "client_email": st.secrets["gcp"]["client_email"],
    "client_id": st.secrets["gcp"]["client_id"],
    "auth_uri": st.secrets["gcp"]["auth_uri"],
    "token_uri": st.secrets["gcp"]["token_uri"],
    "auth_provider_x509_cert_url": st.secrets["gcp"]["auth_provider_x509_cert_url"],
    "client_x509_cert_url": st.secrets["gcp"]["client_x509_cert_url"]
}

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
client = gspread.authorize(creds)

# Abrir el Google Sheet por nombre
sheet = client.open("BaseDatosColeo")
hoja_cuadros = sheet.worksheet("Cuadros")

st.title("🏆 Plataforma de Quinielas de Coleo")

with st.form("registro_cuadro", clear_on_submit=True):
    nombre = st.text_input("Nombre del Participante")
    whatsapp = st.text_input("Número de WhatsApp")
    c1 = st.text_input("Coleador 1")
    c2 = st.text_input("Coleador 2")
    c3 = st.text_input("Coleador 3")
    c4 = st.text_input("Coleador 4")
    
    btn_enviar = st.form_submit_button("Enviar Cuadro")

if btn_enviar:
    if nombre and whatsapp and c1 and c2 and c3 and c4:
        # Aquí es donde ocurre la magia: enviamos los datos a la hoja
        hoja_cuadros.append_row([nombre, whatsapp, c1, c2, c3, c4])
        st.success(f"¡Excelente {nombre}! Tu cuadro ha sido guardado en la base de datos.")
    else:
        st.error("Por favor, llena todos los campos.")
