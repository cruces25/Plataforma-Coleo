import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Función para conectar de forma segura
def conectar_sheets():
    # Cargamos el diccionario desde los secrets
    creds_dict = dict(st.secrets["gcp"])
    creds = Credentials.from_service_account_info(
        creds_dict,
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    return gspread.authorize(creds)
