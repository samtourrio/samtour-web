"""
Sam Tour Rio — Landing Page
Agencia de turismo premium y reubicación en Río de Janeiro y el Cono Sur.
Listo para Streamlit Community Cloud.
"""

import base64
import os
import re

import streamlit as st

# ──────────────────────────────────────────────────────────────────────────
# CONFIGURACIÓN GENERAL
# ──────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Sam Tour Rio | South America, Personally Hosted",
    page_icon="🌅",
    layout="wide",
)

VIDEO_PATH = "videos/SAM-TOUR-abertura.mp4"
SLOGAN = "CULTURE · FOOD · SPORTS · NATURE"
CADASTUR = "CADASTUR: 19.322142.61-7"
FOUNDER = "Samuel Ossa · Sam Tour Rio"
EMAIL_RE = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

SERVICE_KEYS = ["rio", "concierge", "remax", "winter"]

# ──────────────────────────────────────────────────────────────────────────
# TEXTOS / TRADUCCIONES (EN por defecto, ES, PT)
# ──────────────────────────────────────────────────────────────────────────
TRANSLATIONS = {
    "en": {
        "hero_title": "South America, Personally Hosted.",
        "hero_subtitle": (
            "I'm Sam — your private host across Rio de Janeiro and the Southern "
            "Cone. Tours, relocation and real estate, planned and accompanied "
            "personally from start to finish."
        ),
        "video_fallback": "SAM TOUR",
        "service_prompt": "Which experience would you like to explore?",
        "services": {
            "rio": {
                "label": "Rio de Janeiro Tailor-Made Experiences",
                "desc": (
                    "Private, fully customized days built around what actually "
                    "moves you — not a fixed bus-tour route."
                ),
                "bullets": [
                    "Iconic Rio — Christ the Redeemer, Sugarloaf and the postcard views, without the crowds.",
                    "Gastronomy — private tastings and off-menu tables at Rio's best kitchens.",
                    "Football — matches, stadium visits and the culture behind the shirt.",
                    "Nature — Tijuca Forest, hidden beaches and the trails locals actually use.",
                ],
            },
            "concierge": {
                "label": "Expat Concierge & Relocation (Rio)",
                "desc": "A private hand to hold, from the moment you land to the moment Rio feels like home.",
                "bullets": [
                    "Full accompaniment through your first weeks in the city.",
                    "Neighborhood induction — where to live, shop and belong.",
                    "Condominium onboarding and building know-how.",
                    "CPF and essential paperwork, handled alongside you.",
                    "Security guidance and daily transport arranged for you.",
                ],
            },
            "remax": {
                "label": "Premium Property Search (RE/MAX)",
                "desc": "High-standard homes, sourced through RE/MAX's global real estate network and local expertise.",
                "bullets": [
                    "Curated shortlist matched to your standard and preferred neighborhood.",
                    "Private viewings accompanied from start to finish.",
                    "Backed by RE/MAX's global tools, listings and negotiation support.",
                ],
            },
            "winter": {
                "label": "Winter Season: Santiago & Around (Chile)",
                "desc": "A Brazilian favorite — the Andes turn white from May to August, and Sam takes you there.",
                "bullets": [
                    "Snow days in the Cordillera, for first-timers and regulars alike.",
                    "Valle Nevado and Farellones, at the pace you want.",
                    "Vineyard afternoons in between the mountain days.",
                    "May through August — Santiago's best season, hosted personally.",
                ],
            },
        },
        "form_heading": "Plan your experience",
        "form_subheading": "Tell Sam a bit about you — he replies personally.",
        "form_name": "Full name",
        "form_email": "Email",
        "form_whatsapp": "WhatsApp (with country code)",
        "form_whatsapp_ph": "+1 555 123 4567",
        "form_lang_pref": "Preferred language",
        "form_lang_options": ["English", "Español", "Português"],
        "form_details": "Tell us about your plans",
        "form_details_ph": "Dates, group size, interests...",
        "form_submit": "Send to Sam",
        "form_error": "Please complete all required fields with a valid email before sending.",
        "remax_consent": (
            "I authorize my property requirements to be processed through "
            "RE/MAX's official channels and real estate infrastructure."
        ),
        "remax_error": "Please accept the RE/MAX authorization to continue.",
        "form_success": "Thank you! Your request has been received — Sam will personally contact you shortly.",
        "footer_legal": "All rights reserved.",
    },
    "es": {
        "hero_title": "Sudamérica, con anfitrión personal.",
        "hero_subtitle": (
            "Soy Sam — tu anfitrión privado en Río de Janeiro y el Cono Sur. "
            "Tours, reubicación e inmuebles, planeados y acompañados "
            "personalmente de principio a fin."
        ),
        "video_fallback": "SAM TOUR",
        "service_prompt": "¿Qué experiencia te gustaría explorar?",
        "services": {
            "rio": {
                "label": "Experiencias a Medida en Río de Janeiro",
                "desc": (
                    "Días privados y totalmente personalizados según lo que "
                    "realmente te interesa — no una ruta fija de bus turístico."
                ),
                "bullets": [
                    "Río Icónico — Cristo Redentor, Pan de Azúcar y las vistas de postal, sin multitudes.",
                    "Gastronomía — degustaciones privadas y mesas exclusivas en las mejores cocinas de Río.",
                    "Fútbol — partidos, visitas a estadios y la cultura detrás de la camiseta.",
                    "Naturaleza — Bosque de Tijuca, playas escondidas y los senderos que usan los locales.",
                ],
            },
            "concierge": {
                "label": "Concierge de Expatriados y Reubicación (Río)",
                "desc": "Un acompañamiento privado, desde que aterrizas hasta que Río se siente como tu casa.",
                "bullets": [
                    "Acompañamiento integral durante tus primeras semanas en la ciudad.",
                    "Inducción al barrio — dónde vivir, comprar y pertenecer.",
                    "Inducción al condominio y su funcionamiento.",
                    "CPF y trámites esenciales, gestionados junto a ti.",
                    "Orientación de seguridad y transporte diario coordinado para ti.",
                ],
            },
            "remax": {
                "label": "Búsqueda Premium de Propiedades (RE/MAX)",
                "desc": "Inmuebles de alto estándar, respaldados por la red inmobiliaria global de RE/MAX y experiencia local.",
                "bullets": [
                    "Selección curada según tu estándar y el barrio de tu preferencia.",
                    "Visitas privadas acompañadas de principio a fin.",
                    "Respaldado por las herramientas globales, listados y negociación de RE/MAX.",
                ],
            },
            "winter": {
                "label": "Temporada de Invierno: Santiago y Alrededores (Chile)",
                "desc": "Un favorito de los brasileños — la cordillera se viste de blanco de mayo a agosto, y Sam te lleva.",
                "bullets": [
                    "Días de nieve en la cordillera, para principiantes y expertos.",
                    "Valle Nevado y Farellones, al ritmo que prefieras.",
                    "Tardes de viñedos entre los días de montaña.",
                    "De mayo a agosto — la mejor temporada de Santiago, con anfitrión personal.",
                ],
            },
        },
        "form_heading": "Planifica tu experiencia",
        "form_subheading": "Cuéntale a Sam un poco sobre ti — él responde personalmente.",
        "form_name": "Nombre completo",
        "form_email": "Correo electrónico",
        "form_whatsapp": "WhatsApp (con código de país)",
        "form_whatsapp_ph": "+55 21 91234 5678",
        "form_lang_pref": "Idioma preferido",
        "form_lang_options": ["English", "Español", "Português"],
        "form_details": "Cuéntanos tus planes",
        "form_details_ph": "Fechas, número de personas, intereses...",
        "form_submit": "Enviar a Sam",
        "form_error": "Por favor completa todos los campos obligatorios con un correo válido antes de enviar.",
        "remax_consent": (
            "Autorizo que los requerimientos de mi propiedad sean procesados "
            "a través de los canales oficiales e infraestructura inmobiliaria de RE/MAX."
        ),
        "remax_error": "Por favor acepta la autorización de RE/MAX para continuar.",
        "form_success": "¡Gracias! Tu solicitud fue recibida — Sam te contactará personalmente en breve.",
        "footer_legal": "Todos los derechos reservados.",
    },
    "pt": {
        "hero_title": "América do Sul, com anfitrião pessoal.",
        "hero_subtitle": (
            "Eu sou o Sam — seu anfitrião privado no Rio de Janeiro e no Cone "
            "Sul. Passeios, relocation e imóveis, planejados e acompanhados "
            "pessoalmente do início ao fim."
        ),
        "video_fallback": "SAM TOUR",
        "service_prompt": "Qual experiência você gostaria de explorar?",
        "services": {
            "rio": {
                "label": "Experiências Sob Medida no Rio de Janeiro",
                "desc": (
                    "Dias privados e totalmente personalizados de acordo com o "
                    "que realmente importa para você — não um roteiro fixo de ônibus."
                ),
                "bullets": [
                    "Rio Icônico — Cristo Redentor, Pão de Açúcar e as vistas de cartão-postal, sem multidões.",
                    "Gastronomia — degustações privadas e mesas exclusivas nas melhores cozinhas do Rio.",
                    "Futebol — jogos, visitas a estádios e a cultura por trás da camisa.",
                    "Natureza — Floresta da Tijuca, praias escondidas e as trilhas que os cariocas realmente usam.",
                ],
            },
            "concierge": {
                "label": "Concierge para Expatriados & Relocation (Rio)",
                "desc": "Um acompanhamento privado, desde o pouso até o momento em que o Rio parecer sua casa.",
                "bullets": [
                    "Acompanhamento integral nas primeiras semanas na cidade.",
                    "Indução ao bairro — onde morar, comprar e pertencer.",
                    "Indução ao condomínio e seu funcionamento.",
                    "CPF e trâmites essenciais, resolvidos ao seu lado.",
                    "Orientação de segurança e transporte diário organizado para você.",
                ],
            },
            "remax": {
                "label": "Busca Premium de Imóveis (RE/MAX)",
                "desc": "Imóveis de alto padrão, com o respaldo da rede imobiliária global da RE/MAX e conhecimento local.",
                "bullets": [
                    "Seleção curada de acordo com seu padrão e bairro de preferência.",
                    "Visitas privadas acompanhadas do início ao fim.",
                    "Respaldado pelas ferramentas globais, anúncios e negociação da RE/MAX.",
                ],
            },
            "winter": {
                "label": "Temporada de Inverno: Santiago e Arredores (Chile)",
                "desc": "Um favorito dos brasileiros — a cordilheira fica branca de maio a agosto, e o Sam leva você até lá.",
                "bullets": [
                    "Dias de neve na cordilheira, para iniciantes e experientes.",
                    "Valle Nevado e Farellones, no seu ritmo.",
                    "Tardes em vinícolas entre os dias de montanha.",
                    "De maio a agosto — a melhor temporada de Santiago, com anfitrião pessoal.",
                ],
            },
        },
        "form_heading": "Planeje sua experiência",
        "form_subheading": "Conte um pouco sobre você para o Sam — ele responde pessoalmente.",
        "form_name": "Nome completo",
        "form_email": "E-mail",
        "form_whatsapp": "WhatsApp (com código do país)",
        "form_whatsapp_ph": "+55 21 91234 5678",
        "form_lang_pref": "Idioma preferido",
        "form_lang_options": ["English", "Español", "Português"],
        "form_details": "Conte-nos seus planos",
        "form_details_ph": "Datas, número de pessoas, interesses...",
        "form_submit": "Enviar para o Sam",
        "form_error": "Preencha todos os campos obrigatórios com um e-mail válido antes de enviar.",
        "remax_consent": (
            "Autorizo que os meus requisitos de imóvel sejam processados "
            "pelos canais oficiais e pela infraestrutura imobiliária da RE/MAX."
        ),
        "remax_error": "Aceite a autorização da RE/MAX para continuar.",
        "form_success": "Obrigado! Sua solicitação foi recebida — o Sam entrará em contato pessoalmente em breve.",
        "footer_legal": "Todos os direitos reservados.",
    },
}

# ──────────────────────────────────────────────────────────────────────────
# ESTILO — CSS personalizado (paleta, tipografía, tarjetas, formulario)
# ──────────────────────────────────────────────────────────────────────────
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800&display=swap');

:root {
    --navy: #1F264C;
    --gold: #BFA43B;
    --red: #E63946;
    --gold-soft: rgba(191, 164, 59, 0.14);
    --ink: #2E3350;
}

.stApp, .stApp * { font-family: 'Montserrat', sans-serif; }
.stApp { background-color: #FFFFFF; }
#MainMenu, footer, header { visibility: hidden; }

.block-container {
    max-width: 1080px;
    padding-top: 1.2rem;
    padding-bottom: 0.5rem;
}

/* Brand header */
.brand-wrap { text-align: center; padding: 0.3rem 0 0.1rem 0; }
.brand-arc { display: block; margin: 0 auto -12px auto; width: 190px; }
.brand-name {
    font-size: 2.05rem;
    font-weight: 800;
    color: var(--navy);
    letter-spacing: 3px;
    margin: 0;
}
.brand-name .accent { color: var(--red); }
.brand-slogan {
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 3px;
    color: var(--gold);
    margin-top: 6px;
}

/* Language buttons */
.stButton > button, .stFormSubmitButton > button {
    border-radius: 999px;
    border: 1.5px solid var(--gold);
    background-color: transparent;
    color: var(--navy);
    font-weight: 600;
    transition: all 0.2s ease;
}
.stButton > button:hover, .stFormSubmitButton > button:hover {
    background-color: var(--gold-soft);
}
button[kind="primary"] {
    background-color: var(--gold) !important;
    border-color: var(--gold) !important;
    color: #FFFFFF !important;
}
button[kind="primary"]:hover { background-color: #A88F30 !important; }
.stForm button[kind="primary"] {
    width: 100% !important;
    border-radius: 10px !important;
    padding: 0.7rem 0 !important;
    font-size: 1.02rem !important;
    margin-top: 0.4rem;
}

/* Video hero */
.video-hero, .video-fallback {
    width: 100%;
    border-radius: 16px;
    overflow: hidden;
    margin: 0.9rem 0 1.6rem 0;
}
.video-hero video {
    width: 100%;
    height: 62vh;
    max-height: 500px;
    object-fit: cover;
    display: block;
}
.video-fallback {
    height: 260px;
    background-color: var(--navy);
    display: flex;
    align-items: center;
    justify-content: center;
}
.video-fallback span {
    color: var(--gold);
    font-size: 2rem;
    font-weight: 800;
    letter-spacing: 7px;
}

/* Hero text */
.hero-title {
    text-align: center;
    font-size: 2.25rem;
    font-weight: 700;
    color: var(--navy);
    line-height: 1.25;
    margin-bottom: 0.7rem;
}
.hero-subtitle {
    text-align: center;
    font-size: 1.04rem;
    color: #565B70;
    max-width: 680px;
    margin: 0 auto 1.8rem auto;
    line-height: 1.6;
}

/* Service card */
.service-card {
    background-color: #FFFFFF;
    border: 1.5px solid var(--gold);
    border-radius: 16px;
    padding: 1.6rem 1.8rem;
    margin: 0.4rem 0 2rem 0;
    box-shadow: 0 2px 20px rgba(31, 38, 76, 0.07);
}
.service-card h3 { color: var(--navy); font-weight: 700; margin: 0 0 0.5rem 0; }
.service-card .service-desc { color: #565B70; margin-bottom: 1rem; line-height: 1.5; }
.service-card ul { margin: 0; padding-left: 1.15rem; }
.service-card li { color: var(--ink); margin-bottom: 0.5rem; line-height: 1.55; }

/* Form */
.form-heading {
    text-align: center;
    color: var(--navy);
    font-weight: 700;
    font-size: 1.5rem;
    margin-top: 0.6rem;
    margin-bottom: 0.15rem;
}
.form-subheading { text-align: center; color: #6B6F82; margin-bottom: 1.4rem; }

div[data-testid="stTextInput"] input,
div[data-testid="stTextArea"] textarea,
div[data-baseweb="select"] > div {
    border-radius: 10px !important;
    border-color: #D9D3BE !important;
}
div[data-testid="stCheckbox"] {
    background-color: var(--gold-soft);
    border: 1.5px solid var(--gold);
    border-radius: 10px;
    padding: 0.8rem 1rem;
    margin: 0.5rem 0 1rem 0;
}

/* Footer */
.footer-bar {
    background-color: var(--navy);
    color: #FFFFFF;
    text-align: center;
    padding: 1.7rem 1rem;
    margin-top: 2.2rem;
    border-radius: 16px 16px 0 0;
}
.footer-bar .footer-name { color: var(--gold); font-weight: 700; letter-spacing: 1px; font-size: 1.05rem; }
.footer-bar .footer-slogan { font-size: 0.72rem; letter-spacing: 3px; color: #E7E2CF; margin: 0.4rem 0; }
.footer-bar .footer-legal { font-size: 0.75rem; color: #B9BED2; margin-top: 0.5rem; }

/* Mobile */
@media (max-width: 640px) {
    .brand-name { font-size: 1.5rem; letter-spacing: 1.5px; }
    .brand-arc { width: 140px; }
    .video-hero video { height: 220px; }
    .video-fallback { height: 180px; }
    .video-fallback span { font-size: 1.35rem; letter-spacing: 4px; }
    .hero-title { font-size: 1.55rem; }
    .hero-subtitle { font-size: 0.95rem; }
    .service-card { padding: 1.2rem 1.2rem; }
}
</style>
"""

st.markdown(CSS, unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────────
# ESTADO DE SESIÓN
# ──────────────────────────────────────────────────────────────────────────
if "lang" not in st.session_state:
    st.session_state.lang = "en"  # Inglés por defecto (obligatorio)
if "selected_service" not in st.session_state:
    st.session_state.selected_service = SERVICE_KEYS[0]

lang = st.session_state.lang
t = TRANSLATIONS[lang]

# ──────────────────────────────────────────────────────────────────────────
# ENCABEZADO — Marca + selector de idioma
# ──────────────────────────────────────────────────────────────────────────
st.markdown(
    f"""
    <div class="brand-wrap">
        <svg class="brand-arc" viewBox="0 0 190 28" xmlns="http://www.w3.org/2000/svg">
            <path d="M5,24 Q95,-6 185,24" fill="none" stroke="#E63946"
                  stroke-width="2.4" stroke-linecap="round" opacity="0.85"/>
        </svg>
        <h1 class="brand-name"><span class="accent">S</span>AM TOU<span class="accent">R</span> RIO</h1>
        <p class="brand-slogan">{SLOGAN}</p>
    </div>
    """,
    unsafe_allow_html=True,
)

_, col_en, col_es, col_pt = st.columns([2.4, 1, 1, 1])
with col_en:
    if st.button("🇺🇸 EN", key="lang_en", use_container_width=True,
                 type="primary" if lang == "en" else "secondary"):
        st.session_state.lang = "en"
        st.rerun()
with col_es:
    if st.button("🇪🇸 ES", key="lang_es", use_container_width=True,
                 type="primary" if lang == "es" else "secondary"):
        st.session_state.lang = "es"
        st.rerun()
with col_pt:
    if st.button("🇧🇷 PT", key="lang_pt", use_container_width=True,
                 type="primary" if lang == "pt" else "secondary"):
        st.session_state.lang = "pt"
        st.rerun()

# ──────────────────────────────────────────────────────────────────────────
# VIDEO DE ENTRADA (autoplay, loop, silencioso) con fallback elegante
# ──────────────────────────────────────────────────────────────────────────
@st.cache_resource(show_spinner=False)
def _load_video_b64(path: str) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


if os.path.exists(VIDEO_PATH):
    video_b64 = _load_video_b64(VIDEO_PATH)
    st.markdown(
        f"""
        <div class="video-hero">
            <video autoplay loop muted playsinline>
                <source src="data:video/mp4;base64,{video_b64}" type="video/mp4">
            </video>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        f"""
        <div class="video-fallback">
            <span>{t['video_fallback']}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ──────────────────────────────────────────────────────────────────────────
# HERO
# ──────────────────────────────────────────────────────────────────────────
st.markdown(f"<div class='hero-title'>{t['hero_title']}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='hero-subtitle'>{t['hero_subtitle']}</div>", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────────
# SELECTOR DE SERVICIOS + TARJETA DINÁMICA
# ──────────────────────────────────────────────────────────────────────────
selected_service = st.selectbox(
    t["service_prompt"],
    options=SERVICE_KEYS,
    index=SERVICE_KEYS.index(st.session_state.selected_service),
    format_func=lambda key: t["services"][key]["label"],
    key="service_selectbox",
)
st.session_state.selected_service = selected_service

service = t["services"][selected_service]
bullets_html = "".join(f"<li>{b}</li>" for b in service["bullets"])
st.markdown(
    f"""
    <div class="service-card">
        <h3>{service['label']}</h3>
        <p class="service-desc">{service['desc']}</p>
        <ul>{bullets_html}</ul>
    </div>
    """,
    unsafe_allow_html=True,
)

# ──────────────────────────────────────────────────────────────────────────
# FORMULARIO DE CAPTACIÓN DE LEADS
# ──────────────────────────────────────────────────────────────────────────
st.markdown(f"<div class='form-heading'>{t['form_heading']}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='form-subheading'>{t['form_subheading']}</div>", unsafe_allow_html=True)

with st.form(key="lead_form", clear_on_submit=False):
    full_name = st.text_input(t["form_name"])
    email = st.text_input(t["form_email"])
    whatsapp = st.text_input(t["form_whatsapp"], placeholder=t["form_whatsapp_ph"])
    preferred_language = st.selectbox(t["form_lang_pref"], options=t["form_lang_options"])
    details = st.text_area(t["form_details"], placeholder=t["form_details_ph"])

    remax_consent = True
    if selected_service == "remax":
        remax_consent = st.checkbox(t["remax_consent"], value=False, key="remax_consent")

    submitted = st.form_submit_button(t["form_submit"], type="primary", use_container_width=True)

    if submitted:
        whatsapp_digits = re.sub(r"\D", "", whatsapp)
        fields_ok = bool(full_name.strip()) and bool(re.match(EMAIL_RE, email.strip())) and len(whatsapp_digits) >= 8

        if not fields_ok:
            st.error(t["form_error"])
        elif selected_service == "remax" and not remax_consent:
            st.error(t["remax_error"])
        else:
            st.success(t["form_success"])

# ──────────────────────────────────────────────────────────────────────────
# FOOTER LEGAL
# ──────────────────────────────────────────────────────────────────────────
st.markdown(
    f"""
    <div class="footer-bar">
        <div class="footer-name">{FOUNDER}</div>
        <div class="footer-slogan">{SLOGAN}</div>
        <div class="footer-legal">{CADASTUR} · {t['footer_legal']}</div>
    </div>
    """,
    unsafe_allow_html=True,
)
