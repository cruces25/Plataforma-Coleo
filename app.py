import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

st.set_page_config(page_title="Plataforma de Coleo", page_icon="🏆")
st.title("🏆 Plataforma de Quinielas de Coleo")

# 1. Configuración de credenciales (Inyectadas directamente)
GCP_CONFIG = {{
  "type": "service_account",
  "project_id": "generated-wharf-481303-u5",
  "private_key_id": "93fe1c612b74486578238120b44c4621824309db",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDSwzXXck7p0GSX\ntf7hbdELsVnEypj6zIHAc9jzVUySsAj7EqLyRwQU8emasVDVQSmzFOfRcsgbegSU\nDDzKeRmtvZtwEskNgjASixk537+htAtwlkjwPJXXDbhmcUGVkU/gsSGxRRQpAP1E\n5Ro+DlHNpc+bvSi6WHPVSUHGt6CrF8ML9G9jAQcqghb1LysOjbYiuF+k4USdw0Vr\n7Eyx83nLjL5zdxBJqLqUP3NRh9Yeww3CXaZOx1KWFnum6V/wBagyybQ8DSEPHMIR\nYISAvPgvPZSORjCdKDjHI50BKh1yLqcIPvIO5e8PniqsHlZS6dl4Liut2VwBvtTr\nKv4gBaUhAgMBAAECggEAD3/KkFb4JaqtExkPrt1ID7+Rle6+NEdgzVnXnQFrWag3\naNtUf1Oooa+umbErfBtIKULCz3zM6XReLNL/j3Y7ZLL6YNII1gT6awquprplGcun\nQbbTk1MpQ8DfDC2NAKZIhQIRs7scQe2wMmZUuTaNXn2wmEffXGDP1+IEw8vSNXKu\nHpqM/JnhwsLH2852ZFFLUGD46mD3QhqhKy4/zvVUV7RnzzTBR+FLwERDUT8S6Ylb\nqCyRuGXtpYIn3DdJghQ4YzS1Pr0T2iCWLm1fNvrv1tXqmyv5nXfJg469NhT0+ogG\nydNzvCuYOjCtLPNoPRBF/v903xMkSxD6RnHUvC1eBwKBgQD8D1g55mjrT+gqikHC\nCXMo1rSwl4lREL2ZuOEaSfSMBpBCRQBHQgF8W1FGdOZUtsQ6c4vUKp/TxUB9VYv6\nAaelyeYrh+Vm1c4njMoQizoMH+bGMDnUoZgiETuOtj9wlrDRkToovv+kyiSyei3W\nQVH4X5O3eyyaiz95vKiVaqnJ6wKBgQDWDpulehrJCTx7wDDHgEzLTW7wZQU2qUKV\nAHC7TkDHT4Du1G0lJ7Sl9SbSFV2+4kjBODuOk9N2BzZUPgWwb4KpjElc6UFud6TM\nBdHiSsHL2zDNuav2WGQU8HtPWDa1s7uXsnHHw+QJvrhrwkFjYwWXJF8TT1S/OIxM\neOUXhJCeIwKBgDanFRgoz2MGRm7C35M0/VVDiJYppUqAeLvWDGjo1C9wVOMplu/c\nbfoKysqeGjsQDegmmZD9VP5T7LHAVMN2jGU0K8YQhzsO7M5ChqWjqohqel1Ko59p\nElWAqws8lPDSm7A07wlasI+IjQBt4XZtX1qdTqgf+wHfY3n/4AXVxM7VAoGBAJ9G\nvWATDG08lynJ50H7YKkCFCOCN6/loCp46mklICRuLxUHMbOs6Ml4MguuZFQN0m8b\npY1Ax98SHMXwZJFVWBdK0Kf21H4bPp+lUPgeAjfrAFSD7MXgHZBLJKX0kLkBZPvK\nhslLJJpvtJBSOg929gjxwmD+7aNfs12Ps3+dX3KbAoGAHhGrvSJQl2FUN5a8AgBj\nltgPKEwrl/WwfFgjKuH0fAZ9y8po9cq52ExIHZud4EQd9qqLjBJb5V8+NXY3LJ+y\nepBORU7p28PsjNevbq6ELgGgPiFBKjcs7GWRRmF2aiuRgWCZRj4PUWCS2TQ27HAx\n9RuUNA9WB4xJIQBFf6nkz/8=\n-----END PRIVATE KEY-----\n",
  "client_email": "parley-coleo-aguirre@generated-wharf-481303-u5.iam.gserviceaccount.com",
  "client_id": "111155693971512066009",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/parley-coleo-aguirre%40generated-wharf-481303-u5.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
}

# 2. Lógica de conexión
try:
    creds = Credentials.from_service_account_info(GCP_CONFIG, scopes=["https://www.googleapis.com/auth/spreadsheets"])
    client = gspread.authorize(creds)
    # IMPORTANTE: Reemplaza la URL de abajo por la tuya
    hoja = client.open_by_url("1GIHAS9zV3Zvyj-_PKxM7W0YC4gL4qGSSIsUb8WMVhzs").worksheet("Cuadros")
    st.success("¡Conexión establecida correctamente!")
except Exception as e:
    st.error(f"Error de conexión: {e}")
    st.stop()

# 3. Formulario
with st.form("registro"):
    st.subheader("Registrar nuevo cuadro")
    nombre = st.text_input("Nombre del Participante")
    whatsapp = st.text_input("WhatsApp")
    c1 = st.text_input("Coleador 1")
    c2 = st.text_input("Coleador 2")
    c3 = st.text_input("Coleador 3")
    c4 = st.text_input("Coleador 4")
    
    enviar = st.form_submit_button("Guardar Cuadro")

    if enviar:
        if nombre and whatsapp:
            try:
                hoja.append_row([nombre, whatsapp, c1, c2, c3, c4])
                st.success("¡Cuadro guardado en la hoja de cálculo!")
            except Exception as e:
                st.error(f"Error al guardar: {e}")
        else:
            st.warning("Por favor, completa Nombre y WhatsApp.")
