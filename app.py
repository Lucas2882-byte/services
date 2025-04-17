import streamlit as st

st.set_page_config(page_title="Lucasweb - Visibilité Locale", layout="wide")

# HEADER
st.markdown("""
    <style>
        body {
            background-color: #ffffff;
        }
        .title {
            font-size: 48px;
            font-weight: 700;
            color: #f97316;
        }
        .subtitle {
            font-size: 22px;
            font-weight: 400;
            color: #374151;
            margin-bottom: 40px;
        }
        .service-card {
            background: #f9fafb;
            border-radius: 16px;
            padding: 25px;
            margin-bottom: 25px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
            border: 1px solid #e5e7eb;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            position: relative;
        }
        .section-title {
            font-size: 22px;
            font-weight: 700;
            color: #111827;
            margin-bottom: 12px;
        }
        .price-box {
            position: absolute;
            top: 20px;
            right: 20px;
            background-color: #f97316;
            color: white;
            padding: 6px 12px;
            border-radius: 8px;
            font-weight: bold;
            font-size: 14px;
        }
        .benefit {
            color: #4b5563;
            margin-top: 8px;
            font-size: 15px;
        }
        .feature-list {
            color: #1f2937;
            font-size: 16px;
            margin-left: 0;
            padding-left: 1.2rem;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🚀 Boostez votre visibilité locale avec Lucasweb</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Des solutions simples et efficaces pour être visible sur Google, générer plus d’appels, plus de clients.</div>', unsafe_allow_html=True)

# DASHBOARD-LIKE SERVICE DISPLAY

def service_card(title, price, features, benefits, container):
    with container:
        content = f"""
        <div class='service-card'>
            <div class='price-box'>{price}</div>
            <div class='section-title'>{title}</div>
            <ul class='feature-list'>
                {''.join([f'<li>{f}</li>' for f in features])}
            </ul>
            <div style='margin-top: 10px;'>
                {''.join([f"<div class='benefit'>👉 {b}</div>" for b in benefits])}
            </div>
        </div>
        """
        st.markdown(content, unsafe_allow_html=True)

# GRID OF CARDS
row1 = st.columns(2)
service_card(
    "🌐 Création de site internet vitrine",
    "450€",
    ["Site responsive (mobile, tablette)", "Design moderne, formulaire de contact, SEO local", "Hébergement + nom de domaine 1 an inclus (puis 100€/an)"],
    ["Présentez votre activité 24/7 et renforcez votre image pro.", "Convertissez les visiteurs en clients."],
    row1[0]
)
service_card(
    "📍 Optimisation fiche Google My Business",
    "50€/mois",
    ["Création ou optimisation complète (infos, photos, posts, etc.)", "Suivi mensuel, réponses aux avis, analyse de performance"],
    ["Améliorez votre classement sur Google Maps.", "Recevez plus d'appels entrants depuis votre zone locale."],
    row1[1]
)

row2 = st.columns(2)
service_card(
    "📦 Pack 1 fiche + site (sans justificatif)",
    "600€",
    ["1 fiche Google dans la ville de votre choix (sans adresse physique)", "1 site vitrine avec nom de domaine + hébergement inclus"],
    ["Créez une présence locale sans local physique.", "Idéal pour les pros nomades ou multisecteurs."],
    row2[0]
)
service_card(
    "🚀 Pack 5 fiches locales",
    "1 050€",
    ["5 fiches Google (210€/fiche)", "1 site principal (400€) + 4 mini-sites (100€ chacun)", "Numéros de redirection : 25€/mois", "Hébergement + 5 noms de domaine : 160€/an"],
    ["Multipliez les points de présence sur Google Maps.", "Couvrez plusieurs villes sans ouvrir de locaux physiques."],
    row2[1]
)

row3 = st.columns(2)
service_card(
    "🏢 Création de fiche justifiée",
    "75€",
    ["Fiche Google avec justificatif d'adresse réel inclus"],
    ["Obtenez une fiche 100% conforme pour votre entreprise locale."],
    row3[0]
)
service_card(
    "⭐ Achat d’avis Google vérifiés",
    "À partir de 130€",
    ["10 avis : 13€/avis → 130€", "25 avis : 12€/avis → 300€", "50 avis : 11€/avis → 550€", "100 avis : 9€/avis → 900€"],
    ["Améliorez votre e-réputation localement.", "Renforcez votre visibilité grâce à la preuve sociale."],
    row3[1]
)

# CONTACT FULL WIDTH
st.markdown('<div class="service-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">📞 Contact & accompagnement</div>', unsafe_allow_html=True)
st.markdown("""
- Email : contact@lucas-freelance.fr  
- Téléphone : 06 69 29 51 87  
- 🔧 Packs personnalisables selon vos objectifs
""")
st.markdown('</div>', unsafe_allow_html=True)
