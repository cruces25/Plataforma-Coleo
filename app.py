import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import json

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Quinielas de Coleo", layout="centered")

def get_gspread_client():
    # Leer el secreto como un diccionario directo
    creds_dict = dict(st.secrets["gcp"])
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
    return gspread.authorize(creds)

# --- INTERFAZ ---
st.title("🏆 Plataforma de Quinielas de Coleo")

try:
    client = get_gspread_client()
    sheet = client.open("BaseDatosColeo")
    hoja_cuadros = sheet.worksheet("Cuadros")
    hoja_coleadores = sheet.worksheet("Coleadores")

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
            hoja_cuadros.append_row([nombre, whatsapp, c1, c2, c3, c4])
            st.success("¡Excelente! Tu cuadro ha sido guardado.")

except Exception as e:
    st.error(f"Error técnico: {e}")
