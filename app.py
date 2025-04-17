import streamlit as st

st.set_page_config(page_title="Lucasweb - Visibilité Locale", layout="wide")

# HEADER
st.markdown("""
    <style>
        .title {
            font-size: 48px;
            font-weight: 700;
            color: #F97316;
        }
        .subtitle {
            font-size: 22px;
            font-weight: 400;
            color: #333;
            margin-bottom: 40px;
        }
        .section-title {
            font-size: 28px;
            font-weight: 600;
            margin-top: 40px;
            color: #111827;
        }
        .price {
            font-weight: bold;
            color: #059669;
        }
        .service-box {
            background-color: #F9FAFB;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🚀 Boostez votre visibilité locale avec Lucasweb</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Des solutions simples et efficaces pour être visible sur Google, générer plus d’appels, plus de clients.</div>', unsafe_allow_html=True)

# SERVICES
with st.container():
    st.markdown('<div class="section-title">🌐 Création de site internet vitrine - <span class="price">450€</span></div>', unsafe_allow_html=True)
    st.markdown("""
    - Site responsive (mobile, tablette)
    - Design moderne, formulaire de contact, SEO local
    - Hébergement + nom de domaine 1 an inclus (puis 100€/an)
    - ✅ Idéal pour présenter son activité et convertir ses visiteurs
    """)

with st.container():
    st.markdown('<div class="section-title">📍 Optimisation fiche Google My Business - <span class="price">50€/mois</span></div>', unsafe_allow_html=True)
    st.markdown("""
    - Création ou optimisation complète (infos, photos, posts, etc.)
    - Suivi mensuel, réponses aux avis, analyse de performance
    - ✅ Gagnez en visibilité locale sur Google Maps
    """)

with st.container():
    st.markdown('<div class="section-title">📦 Pack 1 fiche + site (sans justificatif) - <span class="price">600€</span></div>', unsafe_allow_html=True)
    st.markdown("""
    - 1 fiche Google dans la ville de votre choix (pas de local requis)
    - 1 site vitrine avec nom de domaine + hébergement inclus
    - ✅ Ciblez une zone stratégique sans vous déplacer
    """)

with st.container():
    st.markdown('<div class="section-title">🚀 Pack 5 fiches locales - <span class="price">1 050€</span></div>', unsafe_allow_html=True)
    st.markdown("""
    - 5 fiches locales (210€/fiche)
    - 1 site principal (400€) + 4 mini-sites personnalisés (100€ chacun) → 800€
    - 5 numéros de redirection → 25€/mois
    - Hébergement + 5 noms de domaine → 160€/an
    - ✅ Dominez Google Maps sur plusieurs zones
    """)

with st.container():
    st.markdown('<div class="section-title">🏢 Création de fiche justifiée - <span class="price">75€</span></div>', unsafe_allow_html=True)
    st.markdown("""
    - Fiche locale vérifiée avec justificatif d'adresse
    - ✅ Présence Google 100% conforme et crédible
    """)

with st.container():
    st.markdown('<div class="section-title">⭐ Avis Google vérifiés</div>', unsafe_allow_html=True)
    st.markdown("""
    - 10 avis : 13€/avis → 130€
    - 25 avis : 12€/avis → 300€
    - 50 avis : 11€/avis → 550€
    - 100 avis : 9€/avis → 900€
    - ✅ Boostez votre réputation et votre classement
    """)

# CONTACT
with st.container():
    st.markdown('<div class="section-title">📞 Contact & accompagnement</div>', unsafe_allow_html=True)
    st.markdown("""
    - Email : contact@lucas-freelance.fr
    - Téléphone : 06 69 29 51 87
    - 🔧 Packs personnalisables sur demande
    """)
