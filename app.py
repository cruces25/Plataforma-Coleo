import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# --- CONFIGURACIÓN ---
def get_gspread_client():
    creds_dict = dict(st.secrets["gcp"])
    creds_dict["private_key"] = creds_dict["private_key"].replace("\\n", "\n")
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
    return gspread.authorize(creds)

# --- INTERFAZ ---
st.set_page_config(page_title="Quinielas de Coleo", layout="centered")
st.title("🏆 Plataforma de Quinielas de Coleo")

try:
    client = get_gspread_client()
    sheet = client.open("BaseDatosColeo")
    hoja_cuadros = sheet.worksheet("Cuadros")
    hoja_coleadores = sheet.worksheet("Coleadores")

    # Leer coleadores (asumiendo que están en la columna A)
    lista_coleadores = hoja_coleadores.col_values(1)[1:]

    with st.form("registro_cuadro", clear_on_submit=True):
        nombre = st.text_input("Nombre del Participante")
        whatsapp = st.text_input("Número de WhatsApp")
        
        c1 = st.selectbox("Coleador 1", lista_coleadores)
        c2 = st.selectbox("Coleador 2", lista_coleadores)
        c3 = st.selectbox("Coleador 3", lista_coleadores)
        c4 = st.selectbox("Coleador 4", lista_coleadores)
        
        btn_enviar = st.form_submit_button("Enviar Cuadro")

        if btn_enviar:
            if nombre and whatsapp:
                hoja_cuadros.append_row([nombre, whatsapp, c1, c2, c3, c4])
                st.success(f"¡Excelente {nombre}! Tu cuadro ha sido guardado.")
            else:
                st.warning("Por favor, ingresa tu nombre y número.")
except Exception as e:
    st.error(f"Error de conexión: {e}")
    st.write("Asegúrate de que tus 'Secrets' estén bien configurados y que el correo de la cuenta de servicio sea editor en el Google Sheet.")
