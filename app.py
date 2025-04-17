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
        .card-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
        }
        .service-card {
            background: #ffffff;
            border-radius: 16px;
            padding: 25px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.04);
            border: 1px solid #d1d5db;
            width: calc(50% - 10px);
            position: relative;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .service-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
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

# CARD RENDERING
st.markdown('<div class="card-grid">', unsafe_allow_html=True)

def service_card(title, price, features, benefits):
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

# Masonry-style by letting browser wrap
service_card(
    "🌐 Création de site internet vitrine",
    "450€",
    ["Site responsive (mobile, tablette)", "Design moderne, formulaire de contact, SEO local", "Hébergement + nom de domaine 1 an inclus (puis 100€/an)", "Interface facile à mettre à jour"],
    ["Présentez votre activité 24/7.", "Renforcez votre image professionnelle.", "Optimisé pour générer des contacts facilement"]
)

service_card(
    "📍 Optimisation fiche Google My Business",
    "50€/mois",
    ["Création ou optimisation complète", "Ajout photos, posts, services", "Réponses aux avis clients", "Suivi des statistiques mensuelles"],
    ["Apparaître mieux classé sur Google Maps.", "Donner une image vivante et à jour.", "Recevoir plus d'appels locaux."]
)

service_card(
    "📦 Pack 1 fiche + site (sans justificatif)",
    "600€",
    ["Fiche Google dans la ville de votre choix", "Site vitrine personnalisé inclus", "Sans besoin d'adresse physique", "Nom de domaine + hébergement inclus"],
    ["Créez une présence dans une nouvelle zone.", "Idéal pour pros nomades ou multisecteurs."]
)

service_card(
    "🚀 Pack 5 fiches locales",
    "1 050€",
    ["5 fiches dans 5 villes différentes", "1 site principal + 4 mini-sites personnalisés", "5 numéros de redirection (25€/mois)", "Hébergement + domaines : 160€/an"],
    ["Présence multizone pour capter + d'appels.", "Très rentable pour prestataires de service local."]
)

service_card(
    "🏢 Création de fiche justifiée",
    "75€",
    ["Fiche Google créée avec justificatif réel", "Optimisation SEO locale incluse"],
    ["Pour professionnels avec adresse vérifiable.", "Fiche conforme et stable sur la durée."]
)

service_card(
    "⭐ Achat d’avis Google vérifiés",
    "À partir de 130€",
    ["10 avis : 13€/avis → 130€", "25 avis : 12€/avis → 300€", "50 avis : 11€/avis → 550€", "100 avis : 9€/avis → 900€"],
    ["Améliorez la crédibilité de votre fiche.", "Boostez le référencement naturel local."]
)

st.markdown('</div>', unsafe_allow_html=True)

# CONTACT
st.markdown('<div class="service-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">📞 Contact & accompagnement</div>', unsafe_allow_html=True)
st.markdown("""
- Email : contact@lucas-freelance.fr  
- Téléphone : 06 69 29 51 87  
- 🔧 Packs personnalisables selon vos objectifs
""")
st.markdown('</div>', unsafe_allow_html=True)
