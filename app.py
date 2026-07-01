import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Quinielas de Coleo", layout="centered")

# Esta es tu información de cuenta de servicio. 
# Nota: He asegurado el formato de la clave privada.
service_account_info = {
    "type": "service_account",
    "project_id": "generated-wharf-481303-u5",
    "private_key_id": "a38fee23f5ba50d765c7375b1d2e3606fa41b4f5",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCqXJ9zVr/RDeJsfHb0DqJwpqr5M36enu3FkvxomHhjF3Kp/J9KiwbgvFIqk9zjwpBFaKN9TegJVSEhu5Ch3g2v6hgPlYhdef1OVrrpQjtFk3jrA05RhzuRLkyFeSufmjkFZbgBvYu6szMDcl9PYgT0m/lJvszxk//i+RElo1OzbXTkGdKdho4Amo6tTToIH4v0XUqmItNQ3RVpy9+SFerK0TvLoH9Bv0txv1hewuSWDWVHTOfiXjZ8ahF025FiCno4vwvrof+7bti1fjM2ehVuqdffPr/ieKX+zXT14cxYj6gQkFDQKv9nayA1M2hnpVV+LrggzGLcjrYJ7zKxH0lNAgMBAAECggEAK9dpO1PkSibiEZwYOqd3ezkQ/8+WMrjgpLs2VK6EMLAMlJ1L2vGbRAOCu61Qp5Ze7VXH2QvO/nPXcmhkCJvt9sruBTisnq2xl9LvB+9A9J9Ge2he49FC7ZI2JBUyOkEEkpSCPYRrbJEIPEdXKsUlVFO9XBKLiFHXhLAnDwIQnLhPWS2jcmgyHW1Ql323VpiT3jLCY8+44m4Sx19tkFx4IXF3ocSk9mkn9Dbm5RPhqeRPiWD4LBw/Vc8n2Bh256vO5x+4wOT12PIVLIRIDC27aqiVGlKWs7/TqJzNWbWGkED2Z8gTTu9Eyz8Mvs6y+B7FLN0jNivf6bajj3f/XVwv6wKBgQDWnc0NjiT1D0rJZIvxr3U20Uf3VqNRqAFNfRNJTwwPpOlE9qVSrDKxYTPGsrbFpT8EObw9gbUOY7Sb7wBghw9Bm6N/D8we4m4J9obY3PW5a6POHlj4NS7uFIU10qXSgSMVeXMKCnMGzpI6DiEBR0sxzbuhTqB/1LFOckpbv3a5vwKBgQDLNkN4hQvIeTmEn/28N6rs0sb+SOawlTmozRe21Ni+qom5iTI7b5exKz1P/kJ+49gA7fw66udp7Ta6XO/Pt0MZiyJGvtz+WWzo902umdF5dee8rSl+JSXYLcqBS3XVdgNVtDZvI/iPvaqFHbExX3w0OYKrTdUu//aknhgUmldH8wKBgG5ZStKacLQ0Pa7ZbP9CyRD7gHZTbLwSl0Dhe6Yo57mvgGV+MDkW4yXDJd0XjNSJB6LDkN9LLu4MJBQ9SkNXjmecf+9YDwseP5gN0v30dr/08Y+MmRBeQBgYIvouqiZXUdO704OpJcWtNxB0rVG795TPBJeHFw1DLjt4lnUgOAp/AoGAQl4qkwYA3yyYWHRYTkxwCoCcdRgiH7Hc7wBsqk3BrCPOb0YbncXIaRiSIboMxZxsQ4F2S1fE1JegtCT+PXzA8Wq7exeC3Z8fLsb2G/woqd6UHM8BKi2/umbaKHgYt+qfFDKTRKEe4PM06dzUriddTUErJ/93jK4UQ5dOjgwKTXkCgYEAzbVv9NNPwMhefBZiLRNQPxhtMoDxOZaxWoIgZklRrcMrn1eD7Q3oG6ufP5Rr3mOdmjhpT4WuWImgB2ju4PXot22BzWhWohHikblDbh7jlIlG02M8xeHUx3B9lPmKTyy6yguTNVz1OQBK3JxmBnlZnqYC3kK99rCzlFbY4L1KsxrE=\n-----END PRIVATE KEY-----",
    "client_email": "parley-coleo-aguirre@generated-wharf-481303-u5.iam.gserviceaccount.com",
    "client_id": "111155693971512066009",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/parley-coleo-aguirre%40generated-wharf-481303-u5.iam.gserviceaccount.com"
}

def get_gspread_client():
    # Aseguramos que la clave privada tenga los saltos de línea correctos
    service_account_info["private_key"] = service_account_info["private_key"].replace("\\n", "\n")
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_info(service_account_info, scopes=scopes)
    return gspread.authorize(creds)

# --- INTERFAZ ---
st.title("🏆 Plataforma de Quinielas de Coleo")

try:
    client = get_gspread_client()
    sheet = client.open("BaseDatosColeo")
    hoja_cuadros = sheet.worksheet("Cuadros")
    
    with st.form("registro", clear_on_submit=True):
        nombre = st.text_input("Nombre")
        whatsapp = st.text_input("WhatsApp")
        c1 = st.text_input("Coleador 1")
        c2 = st.text_input("Coleador 2")
        c3 = st.text_input("Coleador 3")
        c4 = st.text_input("Coleador 4")
        if st.form_submit_button("Enviar"):
            hoja_cuadros.append_row([nombre, whatsapp, c1, c2, c3, c4])
            st.success("¡Enviado!")
except Exception as e:
    st.error(f"Error: {e}")
