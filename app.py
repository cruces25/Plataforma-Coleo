import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

st.title("🏆 Registro de Quinielas")

# Definimos el alcance
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

def get_creds():
    # Streamlit permite leer los secretos como un diccionario directamente
    return Credentials.from_service_account_info(
        st.secrets["gcp"],
        scopes=SCOPES
    )

# Ejecución
try:
    creds = get_creds()
    client = gspread.authorize(creds)
    hoja = client.open("BaseDatosColeo").worksheet("Cuadros")
    
    with st.form("registro"):
        nombre = st.text_input("Nombre")
        tel = st.text_input("WhatsApp")
        c1 = st.text_input("Coleador 1")
        c2 = st.text_input("Coleador 2")
        c3 = st.text_input("Coleador 3")
        c4 = st.text_input("Coleador 4")
        enviar = st.form_submit_button("Guardar")
        
        if enviar:
            hoja.append_row([nombre, tel, c1, c2, c3, c4])
            st.success("¡Registrado!")
except Exception as e:
    st.error(f"Error: {e}")
