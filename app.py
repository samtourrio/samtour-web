"""
SAM TOUR RIO - Landing Page Premium
Arquitectura integrada: Claude (Volumen/Lógica) + Diseño Lujo y CTA WhatsApp Directo
"""

import base64
import os
import streamlit as st

# ──────────────────────────────────────────────────────────────────────────
# 1. CONFIGURACIÓN GENERAL Y SEO
# ──────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Sam Tour | Culture · Food · Sports · Nature",
    page_icon="🌎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Constantes de negocio
SLOGAN = "CULTURE · FOOD · SPORTS · NATURE"
CADASTUR = "CADASTUR: 19.322142.61-7"
FOUNDER = "Samuel Ossa · Sam Tour"
WHATSAPP_NUMBER = "5521981808354"
EMAIL_CONTACT = "samtourrio@gmail.com"
INSTA_1 = "@sam.tour.rio"
INSTA_2 = "@sam.cook.rio"

# ──────────────────────────────────────────────────────────────────────────
# 2. BASE DE DATOS DE TRADUCCIONES (Alta fidelidad)
# ──────────────────────────────────────────────────────────────────────────
TRANSLATIONS = {
    "en": {
        "hero_title": "South America, Personally Hosted.",
        "hero_subtitle": "I'm Sam — your private host across Rio de Janeiro and the Southern Cone. Tours, relocation and real estate, planned and accompanied personally from start to finish.",
        "video_fallback": "SAM TOUR",
        "service_prompt": "OUR EXPERIENCES",
        "services": {
            "rio": {
                "label": "Rio de Janeiro Tailor-Made Experiences",
                "desc": "Private, fully customized days built around what actually moves you — not a fixed bus-tour route.",
                "bullets": [
                    "Iconic Rio — Christ the Redeemer, Sugarloaf and postcard views, without the crowds.",
                    "Gastronomy — private tastings and off-menu tables at Rio's best kitchens.",
                    "Football — matches, stadium visits and the culture behind the shirt.",
                    "Nature — Tijuca Forest, hidden beaches and the trails locals actually use."
                ]
            },
            "concierge": {
                "label": "Expat Concierge & Relocation (Rio)",
                "desc": "A private hand to hold, from the moment you land to the moment Rio feels like home.",
                "bullets": [
                    "Full accompaniment through your first weeks in the city.",
                    "Neighborhood induction — where to live, shop and belong.",
                    "CPF and essential paperwork, handled alongside you.",
                    "Security guidance and daily transport arranged for you."
                ]
            },
            "remax": {
                "label": "Premium Property Search (RE/MAX)",
                "desc": "High-standard homes, sourced through RE/MAX's global real estate network and local expertise.",
                "bullets": [
                    "Curated shortlist matched to your standard and preferred neighborhood.",
                    "Private viewings accompanied from start to finish.",
                    "Backed by RE/MAX's global tools, listings and negotiation support."
                ]
            },
            "winter": {
                "label": "Winter Season: Santiago & Around (Chile)",
                "desc": "A Brazilian favorite — the Andes turn white from May to August, and Sam takes you there.",
                "bullets": [
                    "Snow days in the Cordillera, for first-timers and regulars alike.",
                    "Valle Nevado and Farellones, at the pace you want.",
                    "Vineyard afternoons in between the mountain days.",
                    "May through August — Santiago's best season, hosted personally."
                ]
            }
        },
        "cta_title": "START PLANNING YOUR JOURNEY",
        "cta_subtitle": "Connect directly with Sam to design your tailored experience.",
        "cta_button": "Message Sam on WhatsApp",
        "wa_msg": "Hi Sam! I am interested in planning a tailored experience in South America.",
        "footer_legal": "All rights reserved."
    },
    "es": {
        "hero_title": "Sudamérica, con anfitrión personal.",
        "hero_subtitle": "Soy Sam — tu anfitrión privado en Río de Janeiro y el Cono Sur. Tours, reubicación e inmuebles, planeados y acompañados personalmente de principio a fin.",
        "video_fallback": "SAM TOUR",
        "service_prompt": "NUESTRAS EXPERIENCIAS",
        "services": {
            "rio": {
                "label": "Experiencias a Medida en Río de Janeiro",
                "desc": "Días privados y totalmente personalizados según lo que realmente te interesa — no una ruta fija de bus turístico.",
                "bullets": [
                    "Río Icónico — Cristo Redentor, Pan de Azúcar y las vistas de postal, sin multitudes.",
                    "Gastronomía — degustaciones privadas y mesas exclusivas en las mejores cocinas de Río.",
                    "Fútbol — partidos, visitas a estadios y la cultura detrás de la camiseta.",
                    "Naturaleza — Bosque de Tijuca, playas escondidas y senderos locales."
                ]
            },
            "concierge": {
                "label": "Concierge de Expatriados y Reubicación",
                "desc": "Un acompañamiento privado, desde que aterrizas hasta que Río se siente como tu casa.",
                "bullets": [
                    "Acompañamiento integral durante tus primeras semanas en la ciudad.",
                    "Inducción al barrio — dónde vivir, comprar y pertenecer.",
                    "CPF y trámites esenciales, gestionados junto a ti.",
                    "Orientación de seguridad y transporte diario coordinado para ti."
                ]
            },
            "remax": {
                "label": "Búsqueda Premium de Propiedades (RE/MAX)",
                "desc": "Inmuebles de alto estándar, respaldados por la red inmobiliaria global de RE/MAX y experiencia local.",
                "bullets": [
                    "Selección curada según tu estándar y el barrio de tu preferencia.",
                    "Visitas privadas acompañadas de principio a fin.",
                    "Respaldado por las herramientas globales y negociación de RE/MAX."
                ]
            },
            "winter": {
                "label": "Temporada de Invierno (Chile)",
                "desc": "Un favorito de los brasileños — la cordillera se viste de blanco de mayo a agosto, y Sam te lleva.",
                "bullets": [
                    "Días de nieve en la cordillera, para principiantes y expertos.",
                    "Valle Nevado y Farellones, al ritmo que prefieras.",
                    "Tardes de viñedos entre los días de montaña.",
                    "De mayo a agosto — la mejor temporada de Santiago, con anfitrión personal."
                ]
            }
        },
        "cta_title": "PLANIFICA TU VIAJE",
        "cta_subtitle": "Conecta directamente con Sam para diseñar tu experiencia a medida.",
        "cta_button": "Escríbele a Sam por WhatsApp",
        "wa_msg": "¡Hola Sam! Me gustaría planificar una experiencia a medida en Sudamérica.",
        "footer_legal": "Todos los derechos reservados."
    },
    "pt": {
        "hero_title": "América do Sul, com anfitrião pessoal.",
        "hero_subtitle": "Eu sou o Sam — seu anfitrião privado no Rio de Janeiro e no Cone Sul. Passeios, relocation e imóveis, planejados e acompanhados pessoalmente do início ao fim.",
        "video_fallback": "SAM TOUR",
        "service_prompt": "NOSSAS EXPERIÊNCIAS",
        "services": {
            "rio": {
                "label": "Experiências Sob Medida no Rio",
                "desc": "Dias privados e totalmente personalizados de acordo com o que realmente importa para você — não um roteiro fixo.",
                "bullets": [
                    "Rio Icônico — Cristo Redentor, Pão de Açúcar e vistas de cartão-postal, sem multidões.",
                    "Gastronomia — degustações privadas e mesas exclusivas nas melhores cozinhas do Rio.",
                    "Futebol — jogos, visitas a estádios e a cultura por trás da camisa.",
                    "Natureza — Floresta da Tijuca, praias escondidas e trilhas locais."
                ]
            },
            "concierge": {
                "label": "Concierge para Expatriados & Relocation",
                "desc": "Um acompanhamento privado, desde o pouso até o momento em que o Rio parecer sua casa.",
                "bullets": [
                    "Acompanhamento integral nas primeiras semanas na cidade.",
                    "Indução ao bairro — onde morar, comprar e pertencer.",
                    "CPF e trâmites essenciais, resolvidos ao seu lado.",
                    "Orientação de segurança e transporte diário organizado para você."
                ]
            },
            "remax": {
                "label": "Busca Premium de Imóveis (RE/MAX)",
                "desc": "Imóveis de alto padrão, com o respaldo da rede imobiliária global da RE/MAX e conhecimento local.",
                "bullets": [
                    "Seleção curada de acordo com seu padrão e bairro de preferência.",
                    "Visitas privadas acompanhadas do início ao fim.",
                    "Respaldado pelas ferramentas globais e negociação da RE/MAX."
                ]
            },
            "winter": {
                "label": "Temporada de Inverno (Chile)",
                "desc": "Um favorito dos brasileiros — a cordilheira fica branca de maio a agosto, e o Sam leva você até lá.",
                "bullets": [
                    "Dias de neve na cordilheira, para iniciantes e experientes.",
                    "Valle Nevado e Farellones, no seu ritmo.",
                    "Tardes em vinícolas entre os dias de montanha.",
                    "De maio a agosto — a melhor temporada de Santiago, com anfitrião pessoal."
                ]
            }
        },
        "cta_title": "PLANEJE SUA VIAGEM",
        "cta_subtitle": "Fale diretamente com o Sam para desenhar sua experiência sob medida.",
        "cta_button": "Fale com o Sam no WhatsApp",
        "wa_msg": "Olá Sam! Tenho interesse em planejar uma experiência sob medida na América do Sul.",
        "footer_legal": "Todos os direitos reservados."
    }
}

# ──────────────────────────────────────────────────────────────────────────
# 3. ESTADO DE SESIÓN (IDIOMA)
# ──────────────────────────────────────────────────────────────────────────
if "lang" not in st.session_state:
    st.session_state.lang = "en"

t = TRANSLATIONS[st.session_state.lang]

# ──────────────────────────────────────────────────────────────────────────
# 4. INYECCIÓN CSS EXTREMA (Sobrescribiendo Streamlit)
# ──────────────────────────────────────────────────────────────────────────
CSS = """
<style>
/* Importar tipografía estilo Varig (Montserrat) */
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800;900&display=swap');

/* Forzar tipografía en TODOS los elementos de Streamlit */
* {
    font-family: 'Montserrat', sans-serif !important;
}

:root {
    --navy: #1F264C;
    --gold: #BFA43B;
    --red: #E63946;
    --bg-light: #F8F9FA;
}

/* Fondo principal */
.stApp {
    background-color: var(--bg-light);
}

/* Ocultar elementos nativos */
#MainMenu, header, footer { visibility: hidden; display: none; }
.block-container { max-width: 1200px; padding-top: 1rem; padding-bottom: 2rem; }

/* Menú de Idiomas */
div[data-testid="column"] button {
    background-color: transparent !important;
    border: 2px solid var(--navy) !important;
    color: var(--navy) !important;
    font-weight: 800 !important;
    font-size: 1rem !important;
    border-radius: 0px !important; /* Cuadrado estilo aerolínea */
    width: 100%;
    letter-spacing: 2px;
    transition: all 0.3s ease;
}
div[data-testid="column"] button:hover {
    background-color: var(--navy) !important;
    color: white !important;
    border-color: var(--navy) !important;
}

/* Logo Text (Fallback) */
.brand-arc { display: block; margin: 0 auto -10px auto; width: 220px; }
.brand-name { font-size: 4rem; font-weight: 900; color: var(--navy); letter-spacing: 6px; margin: 0; text-align: center; text-transform: uppercase;}
.brand-slogan { font-size: 1.1rem; font-weight: 700; letter-spacing: 4px; color: var(--gold); margin-top: 10px; text-align: center;}

/* Hero Section */
.hero-title { text-align: center; font-size: 2.5rem; font-weight: 800; color: var(--navy); margin-top: 2rem; margin-bottom: 1rem; line-height: 1.2; }
.hero-subtitle { text-align: center; font-size: 1.2rem; color: #4A4A4A; max-width: 800px; margin: 0 auto 3rem auto; line-height: 1.6; font-weight: 400;}

/* Tarjetas de Servicio Lujo */
.service-card {
    background-color: #FFFFFF;
    border-top: 6px solid var(--navy);
    padding: 2.5rem;
    height: 100%;
    box-shadow: 0 10px 30px rgba(31, 38, 76, 0.08);
    transition: transform 0.3s ease, border-color 0.3s ease;
}
.service-card:hover {
    transform: translateY(-5px);
    border-top: 6px solid var(--gold);
}
.service-card h3 { 
    color: var(--navy); 
    font-weight: 800; 
    font-size: 1.4rem; 
    text-transform: uppercase; 
    letter-spacing: 1px;
    margin-top: 0;
}
.service-card p.desc { color: #555; font-size: 1.05rem; line-height: 1.6; margin-bottom: 1.5rem; font-weight: 500;}
.service-card ul { padding-left: 1.2rem; margin: 0; }
.service-card li { color: #333; margin-bottom: 0.8rem; line-height: 1.5; font-weight: 400;}

/* Título Sección Servicios */
.section-title { text-align: center; font-size: 2rem; font-weight: 900; color: var(--navy); letter-spacing: 3px; margin: 4rem 0 2rem 0; text-transform: uppercase;}

/* Video Contenedor */
.video-wrap { width: 100%; border-radius: 0px 0px 20px 20px; overflow: hidden; box-shadow: 0 15px 40px rgba(0,0,0,0.15); margin-bottom: 2rem; background: var(--navy);}
.video-wrap video { width: 100%; height: auto; display: block; max-height: 65vh; object-fit: cover;}

/* Footer & CTA */
.footer-lux {
    background-color: var(--navy);
    padding: 4rem 2rem;
    text-align: center;
    margin-top: 4rem;
    color: white;
}
.footer-lux h2 { color: white; font-weight: 800; font-size: 2rem; letter-spacing: 2px; margin-bottom: 1rem;}
.footer-lux p.sub { color: #A0A5C0; font-size: 1.1rem; margin-bottom: 2.5rem;}
.btn-whatsapp {
    background-color: var(--gold);
    color: var(--navy) !important;
    font-size: 1.2rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 2px;
    padding: 1.2rem 3rem;
    text-decoration: none;
    display: inline-block;
    transition: all 0.3s ease;
}
.btn-whatsapp:hover { background-color: white; transform: scale(1.05); }
.footer-info { margin-top: 3rem; font-size: 0.95rem; color: #8086A8; line-height: 1.8;}
.footer-info a { color: var(--gold); text-decoration: none; font-weight: 600;}
.footer-info a:hover { color: white; }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────────
# 5. MENÚ DE NAVEGACIÓN (Banderas)
# ──────────────────────────────────────────────────────────────────────────
col_espacio, col_en, col_es, col_pt = st.columns([7, 1, 1, 1])
with col_en:
    if st.button("EN"): st.session_state.lang = "en"; st.rerun()
with col_es:
    if st.button("ES"): st.session_state.lang = "es"; st.rerun()
with col_pt:
    if st.button("PT"): st.session_state.lang = "pt"; st.rerun()

# ──────────────────────────────────────────────────────────────────────────
# 6. HEADER VISUAL (Logo y Video)
# ──────────────────────────────────────────────────────────────────────────
st.markdown("<div style='text-align: center; margin-top: 1rem; margin-bottom: 2rem;'>", unsafe_allow_html=True)

# Lógica robusta para cargar el logo: busca en raíz y en carpetas
logo_paths = ["logo.png", "SAM_TOUR_RIO_dorso_alta_legibilidad_300dpi.png", "images/logo.png"]
logo_loaded = False
for path in logo_paths:
    if os.path.exists(path):
        st.image(path, width=400)
        logo_loaded = True
        break

# Si no encuentra la imagen física, renderiza el logo en código HTML emulando la foto 1 que me enviaste
if not logo_loaded:
    st.markdown(f"""
        <svg class="brand-arc" viewBox="0 0 190 28" xmlns="http://www.w3.org/2000/svg">
            <path d="M5,24 Q95,-6 185,24" fill="none" stroke="#E63946" stroke-width="3" stroke-linecap="round"/>
        </svg>
        <h1 class="brand-name">SAM TOUR</h1>
    """, unsafe_allow_html=True)

st.markdown(f"<div class='brand-slogan'>{SLOGAN}</div></div>", unsafe_allow_html=True)

# Lógica robusta para cargar el video:
video_paths = ["SAM-TOUR-abertura.mp4", "videos/SAM-TOUR-abertura.mp4", "video.mp4"]
video_b64 = None
for vp in video_paths:
    if os.path.exists(vp):
        with open(vp, "rb") as f:
            video_b64 = base64.b64encode(f.read()).decode("utf-8")
        break

if video_b64:
    st.markdown(f"""
        <div class="video-wrap">
            <video autoplay loop muted playsinline>
                <source src="data:video/mp4;base64,{video_b64}" type="video/mp4">
            </video>
        </div>
    """, unsafe_allow_html=True)
else:
    # Fallback si el video aún no está en GitHub
    st.markdown(f"<div class='video-wrap' style='padding:4rem;text-align:center;'><h2 style='color:var(--gold);'>SUBE EL VIDEO '{video_paths[0]}' A GITHUB</h2></div>", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────────
# 7. HERO SECTION (Propuesta de Valor)
# ──────────────────────────────────────────────────────────────────────────
st.markdown(f"<div class='hero-title'>{t['hero_title']}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='hero-subtitle'>{t['hero_subtitle']}</div>", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────────
# 8. ECOSISTEMA CIRCULAR (Tarjetas Premium)
# ──────────────────────────────────────────────────────────────────────────
st.markdown(f"<div class='section-title'>{t['service_prompt']}</div>", unsafe_allow_html=True)

def render_card(service_key):
    srv = t["services"][service_key]
    bullets_html = "".join([f"<li>{b}</li>" for b in srv["bullets"]])
    return f"""
    <div class="service-card">
        <h3>{srv['label']}</h3>
        <p class="desc">{srv['desc']}</p>
        <ul>{bullets_html}</ul>
    </div>
    """

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown(render_card("rio"), unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(render_card("remax"), unsafe_allow_html=True)

with col2:
    st.markdown(render_card("concierge"), unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(render_card("winter"), unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────────
# 9. FOOTER DE LUJO Y LLAMADO A LA ACCIÓN (WhatsApp)
# ──────────────────────────────────────────────────────────────────────────
msg_encoded = t['wa_msg'].replace(' ', '%20')
wa_link = f"https://wa.me/{WHATSAPP_NUMBER}?text={msg_encoded}"

st.markdown(f"""
    <div class="footer-lux">
        <h2>{t['cta_title']}</h2>
        <p class="sub">{t['cta_subtitle']}</p>
        
        <a href="{wa_link}" target="_blank" class="btn-whatsapp">
            {t['cta_button']}
        </a>
        
        <div class="footer-info">
            <strong>{FOUNDER}</strong><br>
            {CADASTUR}<br><br>
            ✉️ <a href="mailto:{EMAIL_CONTACT}">{EMAIL_CONTACT}</a><br>
            Instagram: <a href="https://instagram.com/sam.tour.rio" target="_blank">{INSTA_1}</a> | <a href="https://instagram.com/sam.cook.rio" target="_blank">{INSTA_2}</a>
            <br><br>
            <span style="font-size:0.8rem; opacity:0.6;">{t['footer_legal']}</span>
        </div>
    </div>
""", unsafe_allow_html=True)
