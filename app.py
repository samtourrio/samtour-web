import streamlit as st
import base64
import os

# ──────────────────────────────────────────────────────────────────────────
# 1. CONFIGURACIÓN GENERAL Y SEO
# ──────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="SAM TOUR | Culture · Food · Sports · Nature",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ──────────────────────────────────────────────────────────────────────────
# 2. INYECCIÓN DE CSS (Identidad Visual Lujo - Estilo Varig)
# ──────────────────────────────────────────────────────────────────────────
st.markdown("""
    <style>
    /* Tipografía corporativa */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif !important;
        background-color: #FAFAFA;
        color: #1F264C;
    }

    /* Ocultar UI de Streamlit */
    #MainMenu, header, footer {visibility: hidden;}

    /* Contenedores principales */
    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Títulos de sección */
    h1, h2, h3 {
        color: #1F264C !important;
        font-weight: 800 !important;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    .gold-text { color: #BFA43B; font-weight: 700; letter-spacing: 3px; }
    .red-text { color: #E63946; }

    /* Botones de Idioma elegantes */
    div[data-testid="column"] button {
        background-color: transparent !important;
        border: 1px solid #1F264C !important;
        color: #1F264C !important;
        font-weight: 700 !important;
        border-radius: 4px !important;
        width: 100%;
        transition: 0.3s;
    }
    div[data-testid="column"] button:hover {
        border-color: #BFA43B !important;
        color: #BFA43B !important;
    }

    /* Tarjetas de Servicio */
    .service-card {
        background-color: #FFFFFF;
        border-top: 4px solid #1F264C;
        border-radius: 8px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 15px rgba(31,38,76,0.05);
        transition: 0.3s;
    }
    .service-card:hover {
        border-top: 4px solid #BFA43B;
        box-shadow: 0 8px 25px rgba(31,38,76,0.1);
    }
    .service-card h3 { font-size: 1.3rem; margin-bottom: 0.5rem; }
    .service-card p { font-size: 1rem; color: #555; line-height: 1.6; }
    .service-card ul { padding-left: 1.2rem; color: #444; line-height: 1.7; }

    /* Footer / CTA */
    .footer-box {
        background-color: #1F264C;
        color: white;
        text-align: center;
        padding: 3rem 2rem;
        border-radius: 8px;
        margin-top: 3rem;
    }
    .footer-box a {
        color: #BFA43B;
        text-decoration: none;
        font-weight: bold;
    }
    .footer-box a:hover { color: white; }
    
    /* Video container */
    .video-container {
        width: 100%;
        border-radius: 8px;
        overflow: hidden;
        margin-bottom: 3rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    video { width: 100%; height: auto; display: block; }
    </style>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────────
# 3. BASE DE DATOS DE TEXTOS (MULTI-IDIOMA)
# ──────────────────────────────────────────────────────────────────────────
if 'lang' not in st.session_state:
    st.session_state.lang = 'EN'

TRANSLATIONS = {
    'EN': {
        'slogan': 'CULTURE · FOOD · SPORTS · NATURE',
        'intro': 'South America, Personally Hosted. Private tours, relocation, and real estate.',
        'services_title': 'OUR EXPERIENCES',
        's1_title': 'Rio Tailor-Made Experiences',
        's1_desc': 'Private, fully customized days built around what actually moves you.',
        's1_bullets': ['Iconic Rio without crowds', 'Gastronomy & private tastings', 'Football & Maracaná culture', 'Hidden trails & nature'],
        's2_title': 'Expat Concierge & Relocation',
        's2_desc': 'A private hand to hold, from the moment you land to the moment Rio feels like home.',
        's2_bullets': ['Neighborhood induction', 'CPF & essential paperwork', 'Daily transport & security guidance'],
        's3_title': 'Premium Property Search (RE/MAX)',
        's3_desc': 'High-standard homes, sourced through RE/MAX’s global network.',
        's3_bullets': ['Curated shortlists', 'Accompanied private viewings', 'Full negotiation support'],
        's4_title': 'Winter Season (Chile)',
        's4_desc': 'The Andes turn white from May to August, and Sam takes you there.',
        's4_bullets': ['Valle Nevado & Farellones', 'Vineyard afternoons', 'Personally hosted in Santiago'],
        'cta_title': 'START PLANNING YOUR JOURNEY',
        'cta_btn': 'Message Sam on WhatsApp',
        'wa_msg': 'Hi Sam! I am interested in planning an experience.'
    },
    'ES': {
        'slogan': 'CULTURE · FOOD · SPORTS · NATURE',
        'intro': 'Sudamérica, con anfitrión personal. Tours, reubicación e inmuebles.',
        'services_title': 'NUESTRAS EXPERIENCIAS',
        's1_title': 'Experiencias a Medida en Río',
        's1_desc': 'Días privados y personalizados según lo que realmente te interesa.',
        's1_bullets': ['Río icónico sin multitudes', 'Gastronomía y catas privadas', 'Fútbol y cultura del Maracaná', 'Naturaleza y senderos ocultos'],
        's2_title': 'Concierge Expatriados y Relocation',
        's2_desc': 'Acompañamiento privado desde que aterrizas hasta que Río se siente como casa.',
        's2_bullets': ['Inducción al barrio', 'Trámites de CPF', 'Orientación de seguridad y transporte'],
        's3_title': 'Búsqueda Premium de Inmuebles (RE/MAX)',
        's3_desc': 'Propiedades de alto estándar con el respaldo global de RE/MAX.',
        's3_bullets': ['Selección curada', 'Visitas privadas acompañadas', 'Soporte completo en negociación'],
        's4_title': 'Temporada de Invierno (Chile)',
        's4_desc': 'La cordillera se viste de blanco de mayo a agosto, y Sam te lleva.',
        's4_bullets': ['Valle Nevado y Farellones', 'Tardes de viñedos', 'Anfitrión personal en Santiago'],
        'cta_title': 'PLANIFICA TU VIAJE',
        'cta_btn': 'Escríbele a Sam por WhatsApp',
        'wa_msg': '¡Hola Sam! Me gustaría planificar una experiencia.'
    },
    'PT': {
        'slogan': 'CULTURE · FOOD · SPORTS · NATURE',
        'intro': 'América do Sul, com anfitrião pessoal. Tours, relocation e imóveis.',
        'services_title': 'NOSSAS EXPERIÊNCIAS',
        's1_title': 'Experiências Sob Medida no Rio',
        's1_desc': 'Dias privados e personalizados de acordo com o que realmente importa para você.',
        's1_bullets': ['Rio icônico sem multidões', 'Gastronomia e degustações privadas', 'Futebol e cultura do Maracanã', 'Natureza e trilhas escondidas'],
        's2_title': 'Concierge Expatriados & Relocation',
        's2_desc': 'Acompanhamento privado, desde o pouso até o Rio parecer sua casa.',
        's2_bullets': ['Indução ao bairro', 'Trâmites de CPF', 'Orientação de segurança e transporte'],
        's3_title': 'Busca Premium de Imóveis (RE/MAX)',
        's3_desc': 'Imóveis de alto padrão com o respaldo global da rede RE/MAX.',
        's3_bullets': ['Seleção curada', 'Visitas privadas acompanhadas', 'Suporte completo em negociação'],
        's4_title': 'Temporada de Inverno (Chile)',
        's4_desc': 'A cordilheira fica branca de maio a agosto, e o Sam leva você.',
        's4_bullets': ['Valle Nevado e Farellones', 'Tardes em vinícolas', 'Anfitrião pessoal em Santiago'],
        'cta_title': 'PLANEJE SUA VIAGEM',
        'cta_btn': 'Fale com o Sam no WhatsApp',
        'wa_msg': 'Olá Sam! Tenho interesse em planejar uma experiência.'
    }
}

t = TRANSLATIONS[st.session_state.lang]

# ──────────────────────────────────────────────────────────────────────────
# 4. NAVEGACIÓN Y LOGO
# ──────────────────────────────────────────────────────────────────────────
# Selector de idiomas
col_space, col_en, col_es, col_pt = st.columns([7, 1, 1, 1])
with col_en:
    if st.button("EN"): st.session_state.lang = 'EN'; st.rerun()
with col_es:
    if st.button("ES"): st.session_state.lang = 'ES'; st.rerun()
with col_pt:
    if st.button("PT"): st.session_state.lang = 'PT'; st.rerun()

# Cabecera de Logo
st.markdown("<div style='text-align: center; margin-top: 1rem;'>", unsafe_allow_html=True)
try:
    # Intenta cargar el logo si existe en el repositorio
    st.image("logo.png", width=300)
except:
    # Fallback visual elegante si aún no subes la foto
    st.markdown("<h1>SAM TOUR</h1>", unsafe_allow_html=True)

st.markdown(f"<p class='gold-text'>{t['slogan']}</p>", unsafe_allow_html=True)
st.markdown(f"<p style='font-size: 1.2rem; color: #555; margin-bottom: 2rem;'>{t['intro']}</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────────
# 5. VIDEO HERO (Reproducción automática)
# ──────────────────────────────────────────────────────────────────────────
def load_video():
    video_path = "SAM-TOUR-abertura.mp4"
    if os.path.exists(video_path):
        with open(video_path, "rb") as v_file:
            video_base64 = base64.b64encode(v_file.read()).decode('utf-8')
            return f'''
            <div class="video-container">
                <video autoplay loop muted playsinline>
                    <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
                </video>
            </div>
            '''
    return ""

st.markdown(load_video(), unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────────
# 6. ECOSISTEMA CIRCULAR (Los 4 Pilares)
# ──────────────────────────────────────────────────────────────────────────
st.markdown(f"<h2 style='text-align: center; margin-bottom: 2rem;'>{t['services_title']}</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

def build_card(title, desc, bullets):
    li_items = "".join([f"<li>{b}</li>" for b in bullets])
    return f"""
    <div class="service-card">
        <h3>{title}</h3>
        <p>{desc}</p>
        <ul>{li_items}</ul>
    </div>
    """

with col1:
    st.markdown(build_card(t['s1_title'], t['s1_desc'], t['s1_bullets']), unsafe_allow_html=True)
    st.markdown(build_card(t['s3_title'], t['s3_desc'], t['s3_bullets']), unsafe_allow_html=True)

with col2:
    st.markdown(build_card(t['s2_title'], t['s2_desc'], t['s2_bullets']), unsafe_allow_html=True)
    st.markdown(build_card(t['s4_title'], t['s4_desc'], t['s4_bullets']), unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────────────────
# 7. FOOTER Y LLAMADO A LA ACCIÓN (WhatsApp Directo)
# ──────────────────────────────────────────────────────────────────────────
whatsapp_number = "5521981808354"
# Codificamos el mensaje para la URL de WhatsApp
msg_encoded = t['wa_msg'].replace(' ', '%20')
whatsapp_link = f"https://wa.me/{whatsapp_number}?text={msg_encoded}"

st.markdown(f"""
    <div class="footer-box">
        <h2 style="color: white !important;">{t['cta_title']}</h2>
        <p style="margin-bottom: 2rem;">Samuel Ossa · CADASTUR: 19.322142.61-7</p>
        
        <a href="{whatsapp_link}" target="_blank" style="background-color: #BFA43B; color: #1F264C; padding: 15px 30px; border-radius: 50px; font-size: 1.1rem; text-transform: uppercase; font-weight: 800; display: inline-block; margin-bottom: 2rem;">
            {t['cta_btn']} ➔
        </a>
        
        <div style="font-size: 0.9rem; color: #A0A4B8;">
            <p>✉️ <a href="mailto:samtourrio@gmail.com">samtourrio@gmail.com</a></p>
            <p>Instagram: <a href="https://instagram.com/sam.tour.rio" target="_blank">@sam.tour.rio</a> | <a href="https://instagram.com/sam.cook.rio" target="_blank">@sam.cook.rio</a></p>
        </div>
    </div>
""", unsafe_allow_html=True)
