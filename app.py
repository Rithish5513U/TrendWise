import streamlit as st
import pandas as pd

# Page setting up
st.set_page_config(
    page_title="TrendWise - AI Inventory Forecaster",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS for the webpage
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Declarations for elements */
    :root {
        --primary-color: #667eea;
        --secondary-color: #764ba2;
        --accent-color: #f093fb;
        --success-color: #10b981;
        --warning-color: #f59e0b;
        --error-color: #ef4444;
        --border-radius: 12px;
        --border-radius-lg: 20px;
        --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.1);
        --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.15);
        --shadow-lg: 0 8px 32px rgba(0, 0, 0, 0.2);
        --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    /* Dark mode elements */
    [data-theme="dark"] {
        --card-bg: rgba(31, 41, 55, 0.8);
        --card-border: rgba(75, 85, 99, 0.3);
        --text-primary: #f9fafb;
        --text-secondary: #d1d5db;
        --bg-primary: #111827;
        --bg-secondary: #1f2937;
    }
    
    /* Light mode elements */
    [data-theme="light"] {
        --card-bg: rgba(255, 255, 255, 0.8);
        --card-border: rgba(229, 231, 235, 0.5);
        --text-primary: #111827;
        --text-secondary: #6b7280;
        --bg-primary: #ffffff;
        --bg-secondary: #f9fafb;
    }
    
    .main {
        font-family: 'Inter', sans-serif;
        padding: 1rem;
    }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 50%, var(--accent-color) 100%);
        padding: 2.5rem 2rem;
        border-radius: var(--border-radius-lg);
        margin-bottom: 2rem;
        box-shadow: var(--shadow-lg);
        text-align: center;
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(10px);
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.1) 50%, transparent 70%);
        animation: shine 3s ease-in-out infinite;
    }
    
    @keyframes shine {
        0%, 100% { transform: translateX(-100%); }
        50% { transform: translateX(100%); }
    }
    
    .main-header h1 {
        color: white;
        margin: 0;
        font-size: clamp(2rem, 4vw, 3rem);
        font-weight: 700;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.3);
        position: relative;
        z-index: 1;
    }
    
    .main-header p {
        color: rgba(255,255,255,0.9);
        margin: 0.8rem 0 0 0;
        font-size: clamp(1rem, 2vw, 1.2rem);
        font-weight: 400;
        position: relative;
        z-index: 1;
    }
    
    /* Universal card component */
    .card {
        background: var(--card-bg);
        border: 1px solid var(--card-border);
        border-radius: var(--border-radius);
        padding: 1.5rem;
        box-shadow: var(--shadow-sm);
        transition: var(--transition);
        backdrop-filter: blur(10px);
    }
    
    .card:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-md);
    }
    
    .card-lg {
        border-radius: var(--border-radius-lg);
        padding: 2rem;
        box-shadow: var(--shadow-md);
    }
    
    /* Metric cards */
    .metric-card {
        background: var(--card-bg);
        border: 1px solid var(--card-border);
        border-radius: var(--border-radius);
        padding: 1.5rem;
        text-align: center;
        transition: var(--transition);
        backdrop-filter: blur(10px);
        position: relative;
        overflow: hidden;
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
    }
    
    .metric-card:hover {
        transform: translateY(-4px);
        box-shadow: var(--shadow-lg);
        border-color: var(--primary-color);
    }
    
    .metric-icon {
        font-size: 2rem;
        margin-bottom: 0.8rem;
        opacity: 0.8;
    }
    
    .metric-value {
        font-size: clamp(1.5rem, 3vw, 2.5rem);
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 0.5rem;
        line-height: 1.2;
    }
    
    .metric-label {
        font-size: 0.875rem;
        color: var(--text-secondary);
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Alert components */
    .alert {
        padding: 1.2rem;
        border-radius: var(--border-radius);
        margin: 1rem 0;
        border-left: 4px solid;
        animation: slideInLeft 0.5s ease-out;
        backdrop-filter: blur(10px);
        position: relative;
    }
    
    @keyframes slideInLeft {
        from { opacity: 0; transform: translateX(-20px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    .alert-success {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(16, 185, 129, 0.05) 100%);
        border-color: var(--success-color);
        color: var(--success-color);
    }
    
    .alert-warning {
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.1) 0%, rgba(245, 158, 11, 0.05) 100%);
        border-color: var(--warning-color);
        color: var(--warning-color);
    }
    
    .alert-error {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.1) 0%, rgba(239, 68, 68, 0.05) 100%);
        border-color: var(--error-color);
        color: var(--error-color);
    }
    
    /* Chat interface */
    .chat-container {
        background: var(--card-bg);
        border: 1px solid var(--card-border);
        border-radius: var(--border-radius-lg);
        padding: 1.5rem;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
    }
    
    .message {
        padding: 1rem 1.2rem;
        border-radius: var(--border-radius);
        margin: 0.8rem 0;
        animation: messageSlide 0.3s ease-out;
        word-wrap: break-word;
    }
    
    @keyframes messageSlide {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .user-message {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.15) 0%, rgba(102, 126, 234, 0.08) 100%);
        border: 1px solid rgba(102, 126, 234, 0.2);
        border-radius: var(--border-radius) var(--border-radius) 4px var(--border-radius);
        margin-left: 2rem;
        color: var(--text-primary);
    }
    
    .ai-message {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.15) 0%, rgba(16, 185, 129, 0.08) 100%);
        border: 1px solid rgba(16, 185, 129, 0.2);
        border-radius: var(--border-radius) var(--border-radius) var(--border-radius) 4px;
        margin-right: 2rem;
        color: var(--text-primary);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
        color: white;
        border: none;
        border-radius: var(--border-radius);
        padding: 0.75rem 2rem;
        font-weight: 500;
        font-family: 'Inter', sans-serif;
        transition: var(--transition);
        box-shadow: var(--shadow-sm);
        cursor: pointer;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-md);
        background: linear-gradient(135deg, var(--secondary-color) 0%, var(--primary-color) 100%);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* Suggestion buttons */
    .suggestion-button {
        background: var(--card-bg) !important;
        color: var(--text-primary) !important;
        border: 1px solid var(--card-border) !important;
        border-radius: var(--border-radius) !important;
        padding: 0.8rem 1rem !important;
        margin: 0.3rem !important;
        font-size: 0.875rem !important;
        transition: var(--transition) !important;
        backdrop-filter: blur(10px) !important;
    }
    
    .suggestion-button:hover {
        background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%) !important;
        color: white !important;
        transform: translateY(-2px) !important;
        box-shadow: var(--shadow-md) !important;
    }
    
    /* Form inputs */
    .stSelectbox > div > div,
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input {
        background: var(--card-bg) !important;
        border: 1px solid var(--card-border) !important;
        border-radius: var(--border-radius) !important;
        color: var(--text-primary) !important;
        backdrop-filter: blur(10px) !important;
        transition: var(--transition) !important;
    }
    
    .stSelectbox > div > div:focus-within,
    .stTextInput > div > div:focus-within,
    .stNumberInput > div > div:focus-within {
        border-color: var(--primary-color) !important;
        box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.2) !important;
    }
    
    /* File uploader */
    .stFileUploader > div {
        background: var(--card-bg) !important;
        border: 2px dashed var(--card-border) !important;
        border-radius: var(--border-radius-lg) !important;
        padding: 2rem !important;
        transition: var(--transition) !important;
        backdrop-filter: blur(10px) !important;
    }
    
    .stFileUploader > div:hover {
        border-color: var(--primary-color) !important;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.05) 0%, rgba(118, 75, 162, 0.05) 100%) !important;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        background: var(--card-bg);
        border-radius: var(--border-radius);
        padding: 0.5rem;
        border: 1px solid var(--card-border);
        backdrop-filter: blur(10px);
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: var(--border-radius);
        color: var(--text-secondary);
        font-weight: 500;
        padding: 0.75rem 1.5rem;
        transition: var(--transition);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
        color: white !important;
        box-shadow: var(--shadow-sm);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: var(--card-bg) !important;
        backdrop-filter: blur(10px) !important;
    }
    
    /* Loading spinner */
    .loading-spinner {
        border: 4px solid rgba(102, 126, 234, 0.1);
        border-top: 4px solid var(--primary-color);
        border-radius: 50%;
        width: 40px;
        height: 40px;
        animation: spin 1s linear infinite;
        margin: 0 auto 1rem auto;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* Feature cards */
    .feature-card {
        background: var(--card-bg);
        border: 1px solid var(--card-border);
        border-radius: var(--border-radius);
        padding: 1.5rem;
        text-align: center;
        transition: var(--transition);
        backdrop-filter: blur(10px);
        height: 100%;
    }
    
    .feature-card:hover {
        transform: translateY(-4px);
        box-shadow: var(--shadow-lg);
        border-color: var(--primary-color);
    }
    
    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        display: block;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main-header {
            padding: 1.5rem 1rem;
        }
        
        .card {
            padding: 1rem;
        }
        
        .metric-card {
            padding: 1rem;
        }
        
        .user-message {
            margin-left: 0.5rem;
        }
        
        .ai-message {
            margin-right: 0.5rem;
        }
    }
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--bg-secondary);
    }
    
    ::-webkit-scrollbar-thumb {
        background: var(--primary-color);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: var(--secondary-color);
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown("""
    <div class="main-header">
        <h1>📈 TrendWise</h1>
        <p>Your Intelligent Inventory Companion - Powered by AI</p>
    </div>
    """, unsafe_allow_html=True)

def display_welcome_screen():
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div class="card card-lg" style="text-align: center;">
            <h2 style="margin-bottom: 1rem;">🎉 Welcome to TrendWise!</h2>
            <p style="font-size: 1.1rem; margin-bottom: 2rem; opacity: 0.8;">
                Transform your inventory management with AI-powered insights and predictions
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### ✨ **What TrendWise Can Do for You**")
    
    features = [
        {"icon": "📈", "title": "Smart Forecasting", "desc": "Predict future demand with 95%+ accuracy using advanced AI"},
        {"icon": "📦", "title": "Inventory Optimization", "desc": "Get precise reorder points and safety stock recommendations"},
        {"icon": "🤖", "title": "AI Assistant", "desc": "Chat with our AI for personalized business insights"},
        {"icon": "⚠️", "title": "Smart Alerts", "desc": "Proactive notifications for stockouts and opportunities"},
        {"icon": "📊", "title": "Visual Analytics", "desc": "Beautiful charts and dashboards for data-driven decisions"},
        {"icon": "🎯", "title": "Performance Tracking", "desc": "Monitor forecast accuracy and inventory KPIs"}
    ]
    
    cols = st.columns(3)
    for i, feature in enumerate(features):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="feature-card">
                <div class="feature-icon">{feature['icon']}</div>
                <h4 style="margin-bottom: 0.5rem;">{feature['title']}</h4>
                <p style="font-size: 0.9rem; opacity: 0.8;">{feature['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Getting started section
    st.markdown("### 🚀 **Getting Started is Easy**")
    
    steps_cols = st.columns(4)
    steps = [
        {"num": "1", "title": "Upload Data", "desc": "CSV with Date, SKU, Sales"},
        {"num": "2", "title": "Configure", "desc": "Set forecast and inventory parameters"},
        {"num": "3", "title": "Analyze", "desc": "Select SKU and review predictions"},
        {"num": "4", "title": "Optimize", "desc": "Chat with AI for insights"}
    ]
    
    for i, step in enumerate(steps):
        with steps_cols[i]:
            st.markdown(f"""
            <div style="text-align: center; padding: 1rem;">
                <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                           color: white; width: 40px; height: 40px; border-radius: 50%; 
                           display: flex; align-items: center; justify-content: center; 
                           margin: 0 auto 1rem auto; font-weight: bold; font-size: 1.2rem;">
                    {step['num']}
                </div>
                <h5 style="margin-bottom: 0.5rem;">{step['title']}</h5>
                <p style="font-size: 0.8rem; opacity: 0.8;">{step['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Sample data section
    st.markdown("### 📋 **Data Format Example**")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        sample_data = pd.DataFrame({
            'Date': ['2024-01-01', '2024-01-02', '2024-01-03'],
            'SKU': ['ProductA', 'ProductA', 'ProductB'],
            'Sales': [25, 30, 15]
        })
        
        st.dataframe(sample_data, use_container_width=True)
        
        if st.button("📥 **Download Sample Data**", use_container_width=True):
            st.success("✅ Sample data ready for download!")

if __name__ == "__main__":
    main()
