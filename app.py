import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

st.set_page_config(page_title="Plataforma de Coleo", page_icon="🏆")
st.title("🏆 Plataforma de Quinielas de Coleo")

# 1. Configuración de credenciales (Inyectadas directamente)
GCP_CONFIG = {
    "type": "service_account",
    "project_id": "generated-wharf-481303-u5",
    "private_key_id": "162ba21471771bf8b0e16642c7cf01fe0ae44525",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC8h7qeulYq65U+Iv5Isd4WJJaCmSNlwKNm45b14J2WosWmltYZjcSXrOGh3qMXboQKavaq9ASmxHT+m7E6TLKC1xiiGdAeCiDxi7xkmRFmlCeUbpGrmG3Vn5LxJpq3fKBcJU4khOExpUkG5BT2BQ/rniq7PiS5DtCIgNiG5Y7m91EW9HD7Ip7uzTYKS5W65NOwLyBKY7lw//8KjsfbUZ9LS7qeQj5NoTf5SY8KuBlalxo8TRMKTeb5zlpc6ugq48QvRPVH4IpgQzjxRd76S0WX1t8qco1SsOEXfjJGx0hJMrVvYB+5XpBQqtNfB99ggAVH4qZPvva4iQjakrMO6nb7AgMBAAECggEAAdBH/4ZzzjHkosENpSpEa4xVOP27P+KqvfX5L1k4QDPTw13TNItH6ty4cZra5ld4tiVjfhLXwJy4FhEnIU0cBg+GwyMbGTJvTVxvbfWkxlHX3r1ycbxciTxv9v0FoxsesnYBaOD4I2M74NRs3Ic6KRczT8+Vc0wQhQpPYEIp9RdDusnFPmiCmuvFDHlc5N7P3VQ5ni4tVCa3+oMII5Qp6tgjsaXOqhopQNAJEZZ4LrJWjczh4TjkdjN4LfYTj00cLf2wnm1UW5kEhADhICpCUZHbWa+YA+7K/hyoA/QI8ItFbe3clasn0IYXvFA/V1WSGSKe+ziOfO6C3QCey9G7UQKBgQDtu8gSkUbvgRtnpv5LvUqGDJF0ciknZnnm7YhOlG0HjLmCauh/xG4z+vh5SnPU2QzgT8tMBDijZgfyv5Z/4r82tBTLffMA7fmR7Ytxd+03c3NYEOIsKmkJA2gVFPSxAgFayp94kwdPj3Ejwh7yR63iQsiNGoQWiMJ0cMZoeYx/5wKBgQDLBB4wUguj7cSWbsZ2SsioLdJBYb3iCZoqBZrUE8ldlX2bi/wK6ZjiHtHmcJhe7EIpQ6IfJFwMFtNst++Jj5vI82+IN/JclV9acMx3u6WBn6udH2gqTjZp5MPEVc5wPdAXHFUnS5+m2hPzwbuteEgJBBaILB+P51yLllBMY+I9zQKBgQDm8k9wyjTxIqkuzqmnhmJJSxha2TRllEXEMukB/WrVtL3almT7CiZM1PhhTBSup5S8rIfAdzFWex4pkjlwTySWzeaNsPNK6eRTAUM/ndOS1NMusGgno6OaH/cS0+LJujr6qnC1P5AQmDa/GCvcDgo8DciqWyIKihzt5Ui54aq97QKBgFZP5uHWT/qfAQCQEjKCsvLFoGmJu6gZOwD4pw3ZZ7gw8VkrV7nv/L7OKaFWZ4Gb4rkWdxvUYooFPlgvj1ilxK7XyKhaWOFB5GtYH6YcEk6c6uJ/UtMBs6KrzwtvC7iunwTkV9PAFB1lBCyTRk6HH+EtasL0N2sAC1mRS4xevvZVAoGAREGc/zQQnAl3NvJoob0le0zve0xT1uBFdrfIw2OqDovWiD7bWwMMgI1eYQQsx3wDXk5/7JZrZ37VBdor3BOLpJHcyYoDTIM24K0MwwNgXyhwoSZ0YCxalpSQRuEnXNHg2mWzU6trJEzviRQzYg75axm0WWpwc+GlizlVP6yLz1I=\n-----END PRIVATE KEY-----",
    "client_email": "parley-coleo-aguirre@generated-wharf-481303-u5.iam.gserviceaccount.com"
}

# 2. Lógica de conexión
try:
    creds = Credentials.from_service_account_info(GCP_CONFIG, scopes=["https://www.googleapis.com/auth/spreadsheets"])
    client = gspread.authorize(creds)
    # IMPORTANTE: Reemplaza la URL de abajo por la tuya
    hoja = client.open_by_url("https://docs.google.com/spreadsheets/d/1GIHAS9zV3Zvyj-_PKxM7W0YC4gL4qGSSIsUb8WMVhzs/edit?gid=0#gid=0").worksheet("Cuadros")
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
