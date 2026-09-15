import streamlit as st
import base64

# 1. CONFIGURACIÓN INICIAL DE LA PÁGINA (Debe ser la primera línea de Streamlit)
st.set_page_config(
    page_title="SAM TOUR | Culture · Food · Sports · Nature",
    page_icon="🌎", # Pronto lo cambiaremos por tu logo
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. INYECCIÓN DE CSS DE LUJO Y TIPOGRAFÍA
def local_css():
    st.markdown("""
        <style>
        /* Importar tipografía geométrica y elegante */
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&display=swap');

        /* Aplicar tipografía a toda la página y colores base */
        html, body, [class*="css"]  {
            font-family: 'Montserrat', sans-serif;
            background-color: #FAFAFA; /* Blanco muy sutil para dar respiro */
            color: #1F264C; /* Azul Marino Profundo para los textos */
        }

        /* Títulos H1, H2, H3 (Estilo aerolínea clásica: bold y espaciado) */
        h1, h2, h3 {
            font-weight: 700 !important;
            letter-spacing: 2px !important;
            color: #1F264C !important;
            text-transform: uppercase;
        }

        /* Detalles en Dorado Ocre y Arco Rojo Sutil */
        .highlight-gold { color: #BFA43B; font-weight: bold; }
        .highlight-red { color: #E63946; font-weight: bold; }

        /* Ocultar elementos por defecto de Streamlit para aspecto de web real */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Estilo para el contenedor del video hero */
        .sam-tour-intro {
            width: 100%;
            max-height: 60vh;
            object-fit: cover;
            border-radius: 0px 0px 20px 20px;
            box-shadow: 0px 10px 30px rgba(31, 38, 76, 0.2);
        }
        
        /* Contenedor centralizado */
        .center-text { text-align: center; }
        </style>
        """, unsafe_allow_html=True)

local_css()

# 3. GESTOR DE IDIOMAS (STATE MANAGEMENT)
if 'idioma' not in st.session_state:
    st.session_state['idioma'] = 'EN' # Inglés por defecto

# Diccionario de traducciones (Aquí iremos agregando todo el texto de la web)
textos = {
    'EN': {
        'slogan': 'CULTURE · FOOD · SPORTS · NATURE',
        'welcome': 'Welcome to your tailored experience in Rio de Janeiro.',
        'btn_tours': 'Private Tours',
        'btn_expat': 'Expat Concierge',
    },
    'ES': {
        'slogan': 'CULTURE · FOOD · SPORTS · NATURE',
        'welcome': 'Bienvenido a tu experiencia a medida en Río de Janeiro.',
        'btn_tours': 'Tours Privados',
        'btn_expat': 'Concierge para Expatriados',
    },
    'PT': {
        'slogan': 'CULTURE · FOOD · SPORTS · NATURE',
        'welcome': 'Bem-vindo à sua experiência sob medida no Rio de Janeiro.',
        'btn_tours': 'Tours Privados',
        'btn_expat': 'Concierge para Expatriados',
    }
}

lang = st.session_state['idioma']

# 4. BARRA DE NAVEGACIÓN SUPERIOR (Selector de idiomas)
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 8, 2])
with col1:
    if st.button("🇬🇧 EN"): st.session_state['idioma'] = 'EN'; st.rerun()
with col2:
    if st.button("🇪🇸 ES"): st.session_state['idioma'] = 'ES'; st.rerun()
with col3:
    if st.button("🇧🇷 PT"): st.session_state['idioma'] = 'PT'; st.rerun()

# 5. HERO SECTION (Video de apertura)
# Como tienes el video en /videos/SAM-TOUR-abertura.mp4 en tu repositorio:
st.markdown("<div class='center-text'>", unsafe_allow_html=True)
st.markdown(f"<h1>SAM TOUR</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 style='color: #BFA43B;'>{textos[lang]['slogan']}</h3>", unsafe_allow_html=True)

# Inserción del video (Si está en la misma carpeta del repositorio)
try:
    video_file = open('videos/SAM-TOUR-abertura.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes, autoplay=True, loop=True, muted=True)
except FileNotFoundError:
    st.warning("⚠️ Video no encontrado. Asegúrate de que la carpeta 'videos' y el archivo 'SAM-TOUR-abertura.mp4' estén en tu repositorio de GitHub.")

st.markdown(f"<p style='font-size: 1.2rem; margin-top: 20px;'>{textos[lang]['welcome']}</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- FIN DEL CÓDIGO BASE ---
