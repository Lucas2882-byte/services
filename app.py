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
            color: #ccc;
            margin-bottom: 40px;
        }
        .section-box {
            background-color: #1F2937;
            border-radius: 10px;
            padding: 25px;
            margin-bottom: 25px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }
        .section-title {
            font-size: 24px;
            font-weight: 700;
            color: #FBBF24;
            margin-bottom: 10px;
        }
        .price {
            font-weight: bold;
            font-size: 18px;
            color: #10B981;
        }
        .benefit {
            color: #9CA3AF;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🚀 Boostez votre visibilité locale avec Lucasweb</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Des solutions simples et efficaces pour être visible sur Google, générer plus d’appels, plus de clients.</div>', unsafe_allow_html=True)

# SERVICES AS BOXES
def service_box(title, price, features, benefits):
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{title} <span class="price">{price}</span></div>', unsafe_allow_html=True)
    for feature in features:
        st.markdown(f"- {feature}")
    if benefits:
        st.markdown('<br>', unsafe_allow_html=True)
        for b in benefits:
            st.markdown(f'<span class="benefit">👉 {b}</span>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

service_box(
    "🌐 Création de site internet vitrine",
    "450€",
    [
        "Site responsive (mobile, tablette)",
        "Design moderne, formulaire de contact, SEO local",
        "Hébergement + nom de domaine 1 an inclus (puis 100€/an)"
    ],
    ["Présentez votre activité 24/7 et renforcez votre image pro.", "Convertissez les visiteurs en clients."]
)

service_box(
    "📍 Optimisation fiche Google My Business",
    "50€/mois",
    [
        "Création ou optimisation complète (infos, photos, posts, etc.)",
        "Suivi mensuel, réponses aux avis, analyse de performance"
    ],
    ["Améliorez votre classement sur Google Maps.", "Recevez plus d'appels entrants depuis votre zone locale."]
)

service_box(
    "📦 Pack 1 fiche + site (sans justificatif)",
    "600€",
    [
        "1 fiche Google dans la ville de votre choix (sans adresse physique)",
        "1 site vitrine avec nom de domaine + hébergement inclus"
    ],
    ["Créez une présence locale sans local physique.", "Idéal pour les pros nomades ou multisecteurs."]
)

service_box(
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

service_box(
    "🏢 Création de fiche justifiée",
    "75€",
    [
        "Fiche Google avec justificatif d'adresse réel inclus"
    ],
    ["Obtenez une fiche 100% conforme pour votre entreprise locale."]
)

service_box(
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
st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.markdown('<div class="section-title">📞 Contact & accompagnement</div>', unsafe_allow_html=True)
st.markdown("""
- Email : contact@lucas-freelance.fr  
- Téléphone : 06 69 29 51 87  
- 🔧 Packs personnalisables selon vos objectifs
""")
st.markdown('</div>', unsafe_allow_html=True)
