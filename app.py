import streamlit as st

st.set_page_config(page_title="Lucasweb - Visibilité Locale", layout="wide")

# HEADER
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

        html, body, [class*="css"] {
            background-color: #ffffff !important;
            font-family: 'Poppins', sans-serif;
            color: #111827 !important;
        }
        .title {
            font-size: 48px;
            font-weight: 700;
            color: #f97316;
            margin-bottom: 10px;
        }
        .subtitle {
            font-size: 22px;
            font-weight: 400;
            color: #374151;
            margin-bottom: 40px;
        }
        .service-boxes {
            display: flex;
            flex-direction: column;
            gap: 30px;
            margin-bottom: 60px;
        }
        .box {
            background-color: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 12px;
            padding: 25px 30px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            line-height: 1.8;
        }
        .box strong {
            font-size: 18px;
            color: #1f2937;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🚀 Boostez votre visibilité locale avec Lucasweb</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Des solutions simples et efficaces pour être visible sur Google, générer plus d’appels, plus de clients.</div>', unsafe_allow_html=True)

# SERVICE BOXES
st.markdown('<div class="service-boxes">', unsafe_allow_html=True)

services = [
    (
        "🌐 Vente de site internet vitrine – 450€",
        [
            "1 page complète, responsive, optimisée SEO local",
            "Design professionnel personnalisé (images, couleurs, call-to-action)",
            "Formulaire de contact / prise de rendez-vous",
            "Hébergement + nom de domaine inclus pendant 1 an",
            "💻 C’est votre vitrine en ligne, accessible 24/7.",
            "📈 Idéal pour rassurer, convaincre, et générer des contacts.",
            "🔐 Hébergement rapide, sécurisé, sans pub ni distraction."
        ]
    ),
    (
        "📍 Gestion complète d’une fiche Google My Business – 50€/mois",
        [
            "Optimisation fiche existante ou création complète",
            "Photos, description, catégories, services, prise de rendez-vous",
            "Réponses aux avis, publications hebdo, suivi des performances",
            "Rapport mensuel clair : vues, clics, appels, directions",
            "🚀 Une fiche active = plus de visibilité.",
            "📞 Vous remontez dans les résultats et recevez plus d'appels."
        ]
    ),
    (
        "🏢 Création de fiche avec justificatif d'adresse – 75€",
        [
            "Fiche créée dans une ville de votre choix avec adresse réelle vérifiée",
            "Optimisation de base incluse (photos, description, horaires)",
            "Convient aux activités locales ou aux franchises",
            "🔐 Fiche 100% conforme et pérenne dans le temps.",
            "🏙️ Apparaît dans les résultats Google Maps de la zone choisie."
        ]
    ),
    (
        "📦 Création de fiche sans justificatif – 250€",
        [
            "Fiche créée sans local physique",
            "Possibilité de choisir une ville stratégique",
            "Avec mini-site vitrine inclus (optimisation SEO local)",
            "📍 Idéal pour se positionner dans une nouvelle ville sans y être.",
            "💼 Solution rapide et efficace pour les indépendants ou services à distance."
        ]
    ),
    (
        "⭐ Achat d’avis Google vérifiés",
        [
            "10 avis : 13€/avis → 130€",
            "25 avis : 12€/avis → 300€",
            "50 avis : 11€/avis → 550€",
            "100 avis : 9€/avis → 900€",
            "💬 Avis personnalisés, rédigés à la main, livrés progressivement",
            "🔍 Renforce votre crédibilité aux yeux des clients & de Google",
            "📈 Améliore le taux de clic et le positionnement de votre fiche"
        ]
    )
]

for title, points in services:
    st.markdown(f'<div class="box"><strong>{title}</strong><br>' + '<br>'.join(points) + '</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
