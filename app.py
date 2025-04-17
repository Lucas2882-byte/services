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
        .top-box-grid {
            display: flex;
            justify-content: space-between;
            gap: 20px;
            margin-bottom: 40px;
        }
        .top-box {
            flex: 1;
            background: #fefefe;
            border: 1px solid #e5e7eb;
            border-radius: 16px;
            padding: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
            text-align: center;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .top-box:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 16px rgba(0,0,0,0.08);
        }
        .top-box h3 {
            font-size: 20px;
            color: #111827;
            margin-bottom: 10px;
        }
        .top-box p {
            font-size: 16px;
            color: #4b5563;
        }
        .service-card {
            background: linear-gradient(145deg, #ffffff, #f9fafb);
            border-radius: 16px;
            padding: 25px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.04);
            border: 1px solid #d1d5db;
            width: calc(50% - 10px);
            position: relative;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            overflow: hidden;
        }
        .service-card::before {
            content: "";
            position: absolute;
            top: -40px;
            right: -40px;
            width: 120px;
            height: 120px;
            background: #f97316;
            opacity: 0.05;
            transform: rotate(45deg);
            z-index: 0;
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
            position: relative;
            z-index: 1;
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
            z-index: 1;
        }
        .benefit {
            color: #4b5563;
            margin-top: 8px;
            font-size: 15px;
            position: relative;
            z-index: 1;
        }
        .feature-list {
            color: #1f2937;
            font-size: 16px;
            margin-left: 0;
            padding-left: 1.2rem;
            position: relative;
            z-index: 1;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🚀 Boostez votre visibilité locale avec Lucasweb</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Des solutions simples et efficaces pour être visible sur Google, générer plus d’appels, plus de clients.</div>', unsafe_allow_html=True)

# TOP INFO BOXES
st.markdown('<div class="top-box-grid">', unsafe_allow_html=True)

st.markdown('''
    <div class="top-box">
        <h3>🌐 Création de site vitrine</h3>
        <p>Présentez votre activité de manière professionnelle et captez des clients en ligne.</p>
    </div>
''', unsafe_allow_html=True)

st.markdown('''
    <div class="top-box">
        <h3>📍 Fiches Google My Business</h3>
        <p>Multipliez votre visibilité locale sur Google Maps et recevez plus d'appels.</p>
    </div>
''', unsafe_allow_html=True)

st.markdown('''
    <div class="top-box">
        <h3>⭐ Avis clients vérifiés</h3>
        <p>Boostez votre crédibilité avec des avis rédigés à la main et livrés progressivement.</p>
    </div>
''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

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

# Services cards continue as before...
