import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Título de la aplicación
st.title("🏆 Plataforma de Quinielas de Coleo")

# Función para configurar la conexión
def conectar_sheets():
    # Cargamos el diccionario desde los secrets de Streamlit
    creds_dict = dict(st.secrets["gcp"])
    creds = Credentials.from_service_account_info(
        creds_dict,
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    return gspread.authorize(creds)

# Intentamos conectar al iniciar la app
try:
    client = conectar_sheets()
    hoja = client.open("BaseDatosColeo").worksheet("Cuadros")
    st.success("¡Conexión exitosa con Google Sheets!")
except Exception as e:
    st.error(f"Error al conectar con la hoja: {e}")
    st.stop() # Detiene la ejecución si no hay conexión

# Formulario de registro
with st.form("registro_cuadros"):
    st.subheader("Registrar nuevo cuadro")
    participante = st.text_input("Nombre del Participante")
    whatsapp = st.text_input("WhatsApp")
    c1 = st.text_input("Coleador 1")
    c2 = st.text_input("Coleador 2")
    c3 = st.text_input("Coleador 3")
    c4 = st.text_input("Coleador 4")
    
    # Botón de enviar
    enviar = st.form_submit_button("Guardar Cuadro")

    if enviar:
        if not participante or not whatsapp:
            st.warning("Por favor, completa al menos el nombre y WhatsApp.")
        else:
            try:
                # Agregamos la fila a la hoja "Cuadros"
                hoja.append_row([participante, whatsapp, c1, c2, c3, c4])
                st.success(f"¡Cuadro de {participante} registrado con éxito!")
            except Exception as e:
                st.error(f"Error al guardar: {e}")
