import streamlit as st
import base64
import os

# Configuración de la página
st.set_page_config(page_title="ITBA - Probabilidad y Azar", layout="wide", initial_sidebar_state="collapsed")

# Función para cargar imágenes locales en el HTML
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return f"data:image/png;base64,{base64.b64encode(img_file.read()).decode()}"
    return "https://via.placeholder.com/150?text=No+Image"

# Estilos CSS
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    
    /* El recuadro azul/gris de Intro */
    .intro-box {
        background-color: #e2e8f0;
        border-radius: 15px;
        border-left: 10px solid #0074D9;
        padding: 30px;
        display: flex;
        align-items: center;
        gap: 30px;
        margin-bottom: 30px;
    }

    /* Mosaico 2x2 */
    .mosaic-container {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 10px;
        min-width: 320px;
    }
    .mosaic-container img {
        width: 150px;
        height: 100px;
        object-fit: cover;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }

    /* Texto de la derecha */
    .intro-text-side {
        flex: 1;
    }
    .intro-text-side h2 {
        color: #001f3f;
        margin-bottom: 15px;
        font-size: 32px !important;
    }
    .intro-text-side p {
        font-size: 22px !important;
        line-height: 1.5;
        color: #1e293b;
    }

    /* Tarjetas de Apps */
    .app-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 15px;
        border-top: 5px solid #D86018;
    }
    
    /* Botón de navegación personalizado (misma pestaña, corrigiendo el target) */
    .btn-nav {
        display: block;
        width: 100%;
        padding: 12px 0;
        background-color: #001f3f;
        color: #ffffff !important;
        text-align: center;
        border-radius: 10px;
        text-decoration: none;
        font-weight: 600;
        font-size: 16px;
        transition: background-color 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .btn-nav:hover {
        background-color: #0074D9;
        color: white !important;
    }
    
    /* Estilo para alinear el QR a la derecha */
    [data-testid="stHorizontalBlock"] > div:last-child {
        display: flex;
        justify-content: flex-end;
        align-items: center;
    }

    /* --- PARCHE RESPONSIVO PARA CELULARES --- */
    @media (max-width: 768px) {
        h1 {
            font-size: 26px !important;
        }
        h3 {
            font-size: 16px !important;
        }
        .intro-box {
            flex-direction: column !important;
            padding: 20px !important;
            gap: 20px !important;
            text-align: center !important;
        }
        .mosaic-container {
            justify-content: center !important;
            min-width: 100% !important;
            margin: 0 auto !important;
        }
        .mosaic-container img {
            width: 120px !important;
            height: 80px !important;
        }
        .intro-text-side h2 {
            font-size: 22px !important;
        }
        .intro-text-side p {
            font-size: 16px !important;
        }
        .math-container {
            font-size: 15px !important;
            padding: 10px 15px !important;
            display: block !important;
            width: 100% !important;
            box-sizing: border-box !important;
            word-wrap: break-word !important;
        }
        .fraction {
            font-size: 14px !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
col_logo, col_titulo, col_qr = st.columns([1, 4, 1])

with col_logo:
    if os.path.exists('logo_itba.png'):
        st.image('logo_itba.png', width=150)
    else:
        st.write("### ITBA")

with col_titulo:
    st.markdown("<h1 style='color: #0074D9; font-size: 48px; margin-bottom: 0;'>Razonando con Probabilidades</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #475569; margin-top: 5px;'>Intuiciones, Paradojas y Cálculos</h3>", unsafe_allow_html=True)
    st.write("Future Day 2026 - Explorando la matemática del azar")

with col_qr:
    if os.path.exists('qr-code.png'):
        st.image('qr-code.png', width=180) 
    else:
        st.caption("QR Code")

st.write("---")

# --- SECCIÓN INTRO (MOSAICO + TEXTO DENTRO DEL RECUADRO) ---
img_casino = get_base64_image('casino.png')
img_tormenta = get_base64_image('tormenta.png')
img_atomo = get_base64_image('atomo.png')
img_futbol = get_base64_image('futbol.png')

st.markdown(f"""
    <div class="intro-box">
        <div class="mosaic-container">
            <img src="{img_casino}" alt="Casino">
            <img src="{img_tormenta}" alt="Tormenta">
            <img src="{img_atomo}" alt="Atomo">
            <img src="{img_futbol}" alt="Futbol">
        </div>
        <div class="intro-text-side">
            <h2>Fenómenos Aleatorios: <span style="color: #D86018;">el Azar y las Probabilidades</span></h2>
            <p>
                Los <b><i>fenómenos aleatorios</i></b> se presentan con ubicuidad en la naturaleza y la actividad humana. 
                A diferencia de los <b><i>fenómenos determinísticos</i></b>, en el caso aleatorio, no podemos predecir los 
                resultados con <b>certeza</b> sino sólo con cierta <b>probabilidad</b>.
            </p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Botón centrado para ir a la intro extendida (Cambiado a _top)
col_vacia1, col_boton_intro, col_vacia2 = st.columns([1, 1, 1])
with col_boton_intro:
    st.markdown('<a href="https://future-day-2026-intro-yym3jwktpbunjoytjix7xq.streamlit.app/" target="_top" class="btn-nav">Introducción Teórica-Histórica</a>', unsafe_allow_html=True)

st.write("---")
st.write("### 🚀 Experiencias Interactivas")

# --- SECCIÓN 2: GRILLA DE APPS ---
apps = [
    {"titulo": "⚽ Paradoja de la racha", "desc": "¿Conviene Enfrentar a Sacachispas o Real Madrid?", "url": "https://future-day-2026-streak-kaz6bgjpiw25m6ahsjpsfy.streamlit.app/", "icono": "🥅"},
    {"titulo": "🥧 Calculando Pi con Dardos", "desc": "von Neumann visita Monte Carlo.", "url": "https://future-day-2026-01-mcpi-nvhqgvk2ezle3rfb9rgcjb.streamlit.app/", "icono": "🎯"},
    {"titulo": "🎂 Cumpleaños y Probabilidades", "desc": "¿Por qué solo 23 invitados bastan para asegurar una coincidencia?", "url": "https://future-day-2026-birthday-yni9zpxujh2xwfyjzquf7f.streamlit.app/", "icono": "🍰"},
    {"titulo": "🎁 El Dilema de Monty Hall", "desc": "A ver, a ver ¿qué pasó aquí? 🤔", "url": "https://future-day-2026-monty-hr7ey836gttjc6c7srpujq.streamlit.app/", "icono": "🚪"},
    {"titulo": "📋 La Paradoja del Fiscal", "desc": "Falsos Positivos y Probabilidades Contraintuitivas.", "url": "https://future-day-2026-facial-bjp4gqcxdj8atb4h9rcy5e.streamlit.app/", "icono": "🩺"},
    {"titulo": "🧪 El Paseo al Azar", "desc": "Caminatas Dudosas y Movimiento Browniano.", "url": "https://future-day-2026-brownian-3muvodcsqtdcsrrec6vke4.streamlit.app/", "icono": "📉"}
]

rows = [apps[i:i + 3] for i in range(0, len(apps), 3)]
for row in rows:
    cols = st.columns(3)
    for i, app in enumerate(row):
        with cols[i]:
            st.markdown(f"""
                <div class="app-card">
                    <h3>{app['icono']} {app['titulo']}</h3>
                    <p style="height: 60px; color: #475569;">{app['desc']}</p>
                </div>
                <a href="{app['url']}" target="_top" class="btn-nav">Abrir Experimento</a>
            """, unsafe_allow_html=True)

st.write("---")
st.caption("ITBA Future Day 2026 - Departamento de Ciencias Exactas y Naturales")
