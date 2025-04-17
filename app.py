import streamlit as st

st.set_page_config(page_title="Lucasweb - Visibilité Locale", layout="wide")

# HEADER
st.markdown("""
    <style>
        body {
            background-color: #0f172a;
        }
        .title {
            font-size: 48px;
            font-weight: 700;
            color: #f97316;
        }
        .subtitle {
            font-size: 22px;
            font-weight: 400;
            color: #e5e7eb;
            margin-bottom: 40px;
        }
        .service-card {
            background: linear-gradient(135deg, #1e293b, #0f172a);
            border-radius: 16px;
            padding: 30px;
            margin-bottom: 25px;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
            border: 1px solid #334155;
        }
        .section-title {
            font-size: 26px;
            font-weight: 700;
            color: #facc15;
            margin-bottom: 12px;
        }
        .price {
            font-weight: bold;
            font-size: 18px;
            color: #22c55e;
        }
        .benefit {
            color: #94a3b8;
            margin-top: 8px;
            font-size: 15px;
        }
        .feature-list {
            color: #f1f5f9;
            font-size: 16px;
            margin-left: 15px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🚀 Boostez votre visibilité locale avec Lucasweb</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Des solutions simples et efficaces pour être visible sur Google, générer plus d’appels, plus de clients.</div>', unsafe_allow_html=True)

# SERVICES

def service_card(title, price, features, benefits):
    st.markdown('<div class="service-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{title} <span class="price">{price}</span></div>', unsafe_allow_html=True)
    st.markdown('<ul class="feature-list">', unsafe_allow_html=True)
    for f in features:
        st.markdown(f'<li>{f}</li>', unsafe_allow_html=True)
    st.markdown('</ul>', unsafe_allow_html=True)
    for b in benefits:
        st.markdown(f'<div class="benefit">👉 {b}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

service_card(
    "🌐 Création de site internet vitrine",
    "450€",
    [
        "Site responsive (mobile, tablette)",
        "Design moderne, formulaire de contact, SEO local",
        "Hébergement + nom de domaine 1 an inclus (puis 100€/an)"
    ],
    ["Présentez votre activité 24/7 et renforcez votre image pro.", "Convertissez les visiteurs en clients."]
)

service_card(
    "📍 Optimisation fiche Google My Business",
    "50€/mois",
    [
        "Création ou optimisation complète (infos, photos, posts, etc.)",
        "Suivi mensuel, réponses aux avis, analyse de performance"
    ],
    ["Améliorez votre classement sur Google Maps.", "Recevez plus d'appels entrants depuis votre zone locale."]
)

service_card(
    "📦 Pack 1 fiche + site (sans justificatif)",
    "600€",
    [
        "1 fiche Google dans la ville de votre choix (sans adresse physique)",
        "1 site vitrine avec nom de domaine + hébergement inclus"
    ],
    ["Créez une présence locale sans local physique.", "Idéal pour les pros nomades ou multisecteurs."]
)

service_card(
    "🚀 Pack 5 fiches locales",
    "1 050€",
    [
        "5 fiches Google (210€/fiche)",
        "1 site principal (400€) + 4 mini-sites (100€ chacun)",
        "Numéros de redirection : 25€/mois",
        "Hébergement + 5 noms de domaine : 160€/an"
    ],
    ["Multipliez les points de présence sur Google Maps.", "Couvrez plusieurs villes sans ouvrir de locaux physiques."]
)

service_card(
    "🏢 Création de fiche justifiée",
    "75€",
    [
        "Fiche Google avec justificatif d'adresse réel inclus"
    ],
    ["Obtenez une fiche 100% conforme pour votre entreprise locale."]
)

service_card(
    "⭐ Achat d’avis Google vérifiés",
    "À partir de 130€",
    [
        "10 avis : 13€/avis → 130€",
        "25 avis : 12€/avis → 300€",
        "50 avis : 11€/avis → 550€",
        "100 avis : 9€/avis → 900€"
    ],
    ["Améliorez votre e-réputation localement.", "Renforcez votre visibilité grâce à la preuve sociale."]
)

# CONTACT
st.markdown('<div class="service-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">📞 Contact & accompagnement</div>', unsafe_allow_html=True)
st.markdown("""
- Email : contact@lucas-freelance.fr  
- Téléphone : 06 69 29 51 87  
- 🔧 Packs personnalisables selon vos objectifs
""")
st.markdown('</div>', unsafe_allow_html=True)
