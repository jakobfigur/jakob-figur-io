"""
Jakob Figur | Technical Consultant & AI Engineer & Researcher
Personal Portfolio
"""

import streamlit as st
from streamlit_option_menu import option_menu
from pathlib import Path
import os
from PIL import Image
import base64

# ============================================================================
# PAGE CONFIG & STYLING
# ============================================================================

st.set_page_config(
    page_title="Jakob Figur | Technical Consultant & AI Engineer & Researcher",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Dark, Modern, Architect Design
st.markdown("""
<style>
    /* Main Theme */
    :root {
        --primary-color: #6366f1;
        --secondary-color: #475569;
        --background-dark: #0f172a;
        --background-card: #1e293b;
        --text-primary: #f1f5f9;
        --text-secondary: #94a3b8;
    }
    
    /* Remove default padding */
    .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }
    
    /* Typography */
    h1 {
        font-weight: 700;
        letter-spacing: -0.02em;
        color: var(--text-primary);
        line-height: 1.2;
        margin-bottom: 1.5rem;
    }
    
    h2 {
        font-weight: 600;
        letter-spacing: -0.01em;
        color: var(--text-primary);
        margin-top: 3rem;
        margin-bottom: 1.5rem;
    }
    
    h3 {
        font-weight: 500;
        color: var(--primary-color);
        margin-top: 1.5rem;
        margin-bottom: 0.75rem;
    }
    
    h4 {
        font-weight: 500;
        color: var(--text-primary);
        margin-top: 1rem;
    }
    
    p {
        line-height: 1.8;
        color: var(--text-secondary);
        font-size: 1.05rem;
    }
    
    /* Cards */
    .card {
        background: var(--background-card);
        border-radius: 12px;
        padding: 2rem;
        margin: 1.5rem 0;
        border-left: 3px solid var(--primary-color);
        transition: transform 0.2s ease;
    }
    
    .card:hover {
        transform: translateX(4px);
    }
    
    /* Pillar Cards */
    .pillar-card {
        background: var(--background-card);
        border-radius: 12px;
        padding: 2rem;
        margin: 1rem 0;
        border-top: 2px solid var(--primary-color);
        height: 100%;
    }
    
    .pillar-number {
        font-size: 0.85rem;
        color: var(--primary-color);
        font-weight: 600;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }
    
    .pillar-title {
        font-size: 1.25rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 0.75rem;
        line-height: 1.3;
    }
    
    .pillar-content {
        color: var(--text-secondary);
        line-height: 1.7;
        font-size: 1rem;
    }
    
    /* Timeline */
    .timeline-item {
        position: relative;
        padding-left: 2.5rem;
        padding-bottom: 2.5rem;
        border-left: 2px solid var(--secondary-color);
        margin-left: 1rem;
    }
    
    .timeline-item:last-child {
        border-left: 2px solid transparent;
        padding-bottom: 0;
    }
    
    .timeline-dot {
        position: absolute;
        left: -8px;
        top: 0;
        width: 14px;
        height: 14px;
        border-radius: 50%;
        background: var(--primary-color);
        border: 3px solid var(--background-dark);
    }
    
    .timeline-period {
        font-size: 0.85rem;
        color: var(--text-secondary);
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.5rem;
    }
    
    .timeline-title {
        font-size: 1.25rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 0.25rem;
    }
    
    .timeline-company {
        font-size: 1rem;
        color: var(--primary-color);
        margin-bottom: 0.75rem;
    }
    
    .timeline-description {
        color: var(--text-secondary);
        line-height: 1.7;
        margin-bottom: 0.5rem;
    }
    
    .timeline-impact {
        background: rgba(99, 102, 241, 0.1);
        border-left: 3px solid var(--primary-color);
        padding: 0.75rem 1rem;
        margin-top: 0.75rem;
        border-radius: 4px;
    }
    
    .timeline-impact strong {
        color: var(--primary-color);
    }
    
    /* Project Cards */
    .project-card {
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        border-radius: 16px;
        padding: 2.5rem;
        margin: 2rem 0;
        border: 1px solid rgba(99, 102, 241, 0.2);
    }
    
    .project-tag {
        display: inline-block;
        background: rgba(99, 102, 241, 0.15);
        color: var(--primary-color);
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
    }
    
    /* Blog Cards */
    .blog-card {
        background: var(--background-card);
        border-radius: 12px;
        padding: 2rem;
        margin: 1.5rem 0;
        border: 1px solid rgba(148, 163, 184, 0.1);
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .blog-card:hover {
        border-color: var(--primary-color);
        transform: translateY(-2px);
    }
    
    .blog-date {
        font-size: 0.85rem;
        color: var(--text-secondary);
        margin-bottom: 0.5rem;
    }
    
    /* Contact Form */
    .contact-section {
        background: var(--background-card);
        border-radius: 12px;
        padding: 2rem;
        margin-top: 4rem;
        border-top: 2px solid var(--primary-color);
    }
    
    .contact-form-container {
        background: var(--background-card);
        border-radius: 12px;
        padding: 2rem;
        border: 1px solid rgba(99, 102, 241, 0.2);
    }
    
    /* Style Streamlit form elements */
    div[data-testid="stForm"] {
        background: var(--background-card);
        border-radius: 12px;
        padding: 1.5rem;
        border: 1px solid rgba(99, 102, 241, 0.2);
    }
    
    /* Style input fields - unified styling with more specific selectors */
    .stTextInput input,
    .stTextInput > div > div > input,
    input[type="text"],
    input[type="email"] {
        background-color: #0f172a !important;
        color: #f1f5f9 !important;
        border: 1px solid rgba(148, 163, 184, 0.2) !important;
        border-radius: 6px !important;
    }
    
    .stTextArea textarea,
    .stTextArea > div > div > textarea,
    textarea {
        background-color: #0f172a !important;
        color: #f1f5f9 !important;
        border: 1px solid rgba(148, 163, 184, 0.2) !important;
        border-radius: 6px !important;
    }
    
    .stTextInput input:focus,
    .stTextInput > div > div > input:focus,
    input[type="text"]:focus,
    input[type="email"]:focus,
    .stTextArea textarea:focus,
    .stTextArea > div > div > textarea:focus,
    textarea:focus {
        border-color: #6366f1 !important;
        box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.2) !important;
        outline: none !important;
    }
    
    /* Ensure all input containers have same background */
    .stTextInput > div,
    .stTextArea > div,
    .stTextInput > div > div,
    .stTextArea > div > div {
        background-color: transparent !important;
    }
    
    /* Style primary button - override Streamlit's red button */
    button[kind="primary"],
    .stButton > button[kind="primary"],
    button[data-testid="baseButton-primary"],
    div[data-testid="stForm"] button {
        background-color: #6366f1 !important;
        background: #6366f1 !important;
        color: white !important;
        border: none !important;
        border-radius: 6px !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
    }
    
    button[kind="primary"]:hover,
    .stButton > button[kind="primary"]:hover,
    button[data-testid="baseButton-primary"]:hover,
    div[data-testid="stForm"] button:hover {
        background-color: #4f46e5 !important;
        background: #4f46e5 !important;
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.4) !important;
        transform: translateY(-1px) !important;
    }
    
    button[kind="primary"]:active,
    .stButton > button[kind="primary"]:active,
    button[data-testid="baseButton-primary"]:active,
    div[data-testid="stForm"] button:active {
        background-color: #4338ca !important;
        background: #4338ca !important;
        transform: translateY(0) !important;
    }
    
    /* Override Streamlit's default button colors */
    button[kind="primary"]:not(:disabled),
    .stButton > button[kind="primary"]:not(:disabled) {
        background-color: #6366f1 !important;
        background: #6366f1 !important;
    }
    
    .contact-reasons {
        list-style: none;
        padding: 0;
        margin: 1.5rem 0;
    }
    
    .contact-reasons li {
        padding: 0.75rem 0;
        color: var(--text-secondary);
        line-height: 1.6;
        position: relative;
        padding-left: 1.5rem;
    }
    
    .contact-reasons li:before {
        content: "→";
        position: absolute;
        left: 0;
        color: var(--primary-color);
        font-weight: 600;
    }
    
    /* Philosophical Section */
    .philosophical-section {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.1) 0%, rgba(139, 92, 246, 0.05) 100%);
        border-radius: 16px;
        padding: 3rem;
        margin: 3rem 0;
        border: 1px solid rgba(99, 102, 241, 0.2);
    }
    
    /* Social Links */
    .social-link {
        display: inline-block;
        color: var(--text-secondary);
        text-decoration: none;
        margin-right: 1rem;
        transition: color 0.2s ease;
    }
    
    .social-link:hover {
        color: var(--primary-color);
    }
    
    /* Social Icons */
    .social-icons {
        display: flex;
        gap: 1rem;
        align-items: center;
        margin-top: 1rem;
    }
    
    .social-icon {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 40px;
        height: 40px;
        border-radius: 8px;
        background: rgba(99, 102, 241, 0.1);
        transition: all 0.3s ease;
        text-decoration: none;
    }
    
    .social-icon:hover {
        background: var(--primary-color);
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.4);
    }
    
    .social-icon svg {
        width: 20px;
        height: 20px;
        fill: var(--text-secondary);
        transition: fill 0.3s ease;
    }
    
    .social-icon:hover svg {
        fill: white;
    }
    
    .footer-social-icons {
        display: flex;
        gap: 0.75rem;
        justify-content: center;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .footer-social-icons .social-icon {
        width: 36px;
        height: 36px;
    }
    
    .footer-social-icons .social-icon svg {
        width: 18px;
        height: 18px;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background-color: var(--background-card);
    }
    
    /* Profile Image */
    .profile-img {
        border-radius: 50%;
        width: 120px;
        height: 120px;
        object-fit: cover;
        border: 3px solid var(--primary-color);
        margin: 0 auto 1.5rem auto;
        display: block;
    }
    
    .sidebar-bio {
        font-size: 0.95rem;
        line-height: 1.6;
        color: var(--text-secondary);
        margin: 1rem 0;
        padding: 1rem;
        background: rgba(99, 102, 241, 0.05);
        border-radius: 8px;
        border-left: 2px solid var(--primary-color);
    }
    
    /* Accent line */
    .accent-line {
        height: 3px;
        background: linear-gradient(90deg, var(--primary-color) 0%, transparent 100%);
        margin: 2rem 0;
        width: 100px;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Force override Streamlit's default button colors */
    .stButton > button {
        background-color: #6366f1 !important;
    }
    
    /* Additional form styling to ensure consistency */
    div[data-testid="stForm"] input,
    div[data-testid="stForm"] textarea {
        background-color: #0f172a !important;
        color: #f1f5f9 !important;
    }
    
    /* Style for legal links text */
    .legal-link {
        color: #475569 !important;
        text-decoration: underline !important;
        cursor: pointer !important;
        font-size: 0.85rem !important;
    }
    
    .legal-link:hover {
        color: #64748b !important;
    }
    
    
    /* Spacing utilities */
    .spacer {
        margin-top: 3rem;
    }
    
    .small-spacer {
        margin-top: 1.5rem;
    }
    
    /* Hero Section */
    .hero-headline {
        font-size: 2.5rem;
        font-weight: 700;
        line-height: 1.2;
        color: var(--text-primary);
        margin-bottom: 1.5rem;
    }
    
    .hero-subheadline {
        font-size: 1.25rem;
        line-height: 1.6;
        color: var(--text-secondary);
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)


# ============================================================================
# NAVIGATION
# ============================================================================

def get_image_base64(image_path):
    """Convert image to base64 string"""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


def render_navigation():
    """Render sidebar navigation"""
    with st.sidebar:
        # Profile image (if available)
        profile_path = None
        img_type = "jpeg"
        
        # Check for different image formats
        for ext in ['jpeg', 'jpg', 'png']:
            test_path = f"assets/images/profile.{ext}"
            if os.path.exists(test_path):
                profile_path = test_path
                img_type = "png" if ext == "png" else "jpeg"
                break
        
        if profile_path:
            img_base64 = get_image_base64(profile_path)
            st.markdown(f"""
                <div style='text-align: center; margin-bottom: 1.5rem;'>
                    <img src='data:image/{img_type};base64,{img_base64}' 
                         style='border-radius: 50%; 
                                width: 120px; 
                                height: 120px; 
                                object-fit: cover; 
                                border: 3px solid #6366f1;
                                box-shadow: 0 4px 6px rgba(99, 102, 241, 0.3);'/>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("### Jakob Figur")
        st.markdown("**Technical Consultant @ Digistore24**  \n**AI Engineer & Researcher**")
        
        # Bio
        st.markdown("""
        <div class='sidebar-bio'>
        Architecting the bridge between business complexity and AI-driven efficiency. 
        From Fullstack Development to Strategic AI Consulting.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<div class='accent-line'></div>", unsafe_allow_html=True)
        
        selected = option_menu(
            menu_title=None,
            options=["Identity", "Experience", "Projects", "Blog", "Papers"],
            icons=["house", "briefcase", "lightbulb", "pencil", "file-text"],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "transparent"},
                "icon": {"color": "#94a3b8", "font-size": "18px"},
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "5px 0",
                    "padding": "10px 15px",
                    "--hover-color": "#1e293b",
                    "color": "#94a3b8",
                },
                "nav-link-selected": {
                    "background-color": "#6366f1",
                    "color": "white",
                },
            },
        )
        
        st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)
        
        # Social Links with Icons
        st.markdown("#### Connect")
        st.markdown("""
        <div class='social-icons'>
            <a href='https://www.linkedin.com/in/jakob-figur-2b9501367/' target='_blank' class='social-icon' title='LinkedIn'>
                <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
                </svg>
            </a>
            <a href='https://github.com/jakobfigur' target='_blank' class='social-icon' title='GitHub'>
                <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/>
                </svg>
            </a>
            <a href='https://x.com/JakobFigur' target='_blank' class='social-icon' title='X'>
                <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
                </svg>
            </a>
        </div>
        """, unsafe_allow_html=True)
        
    return selected


# ============================================================================
# PAGE: IDENTITY (HOME)
# ============================================================================

def page_identity():
    """Landing page - Identity & Vision"""
    
    # Hero Section
    st.markdown("""
    <div class='hero-headline'>
    Synthesizing High-Scale Business Logic with Agentic Intelligence.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='hero-subheadline'>
    Building the symbiosis between human intuition and machine efficiency. 
    I help organizations navigate the AI revolution through robust engineering and strategic foresight.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='accent-line'></div>", unsafe_allow_html=True)
    
    # The Four Core Pillars
    st.markdown("## Core Competencies")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='pillar-card'>
            <div class='pillar-number'>Pillar 01</div>
            <div class='pillar-title'>Strategic Systems Consulting</div>
            <div class='pillar-content'>
            Managing high-revenue vendors by translating complex business requirements into technical reality. 
            Specialized in scalability and multi-million Euro ecosystems where precision and reliability are non-negotiable.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='pillar-card'>
            <div class='pillar-number'>Pillar 03</div>
            <div class='pillar-title'>Human-AI Symbiosis</div>
            <div class='pillar-content'>
            Exploring the duality of AI—balancing deep technical execution with the philosophical impact of 
            Human Amplification. Designing systems that enhance rather than replace human capability.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='pillar-card'>
            <div class='pillar-number'>Pillar 02</div>
            <div class='pillar-title'>Proven AI Impact</div>
            <div class='pillar-content'>
            Tangible results: <strong>Automated 30% of B2B support tickets</strong> (~400/month) and 
            <strong>reduced manual onboarding workload by 80%</strong> through targeted AI integration 
            and custom automation frameworks.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='pillar-card'>
            <div class='pillar-number'>Pillar 04</div>
            <div class='pillar-title'>AI-First Transformation</div>
            <div class='pillar-content'>
            Authoring strategic frameworks (like the 'AI-First Company' paper) to transition organizations 
            into AI-native environments. Designing transformation roadmaps that balance innovation with operational stability.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # The Human Perspective
    st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='philosophical-section'>
        <h2 style='margin-top: 0;'>The Human Perspective</h2>
        <p style='font-size: 1.1rem; line-height: 1.8; color: #cbd5e1;'>
        In an era of rapid automation, my work is driven by the conviction that AI should 
        <strong>amplify human potential</strong>, not replace it. I analyze both the immense positive 
        potential and the ethical, philosophical challenges of AI to help businesses navigate this 
        revolution with a balanced, long-term vision.
        </p>
        <p style='font-size: 1.1rem; line-height: 1.8; color: #cbd5e1;'>
        The question isn't whether to adopt AI—it's how to integrate it in ways that preserve what makes 
        us uniquely human: creativity, empathy, and strategic thinking. Technology should serve humanity, 
        not the other way around.
        </p>
    </div>
    """, unsafe_allow_html=True)


# ============================================================================
# PAGE: EXPERIENCE (TIMELINE)
# ============================================================================

def page_experience():
    """Professional timeline and experience"""
    
    st.markdown("# Professional Experience")
    st.markdown("<div class='accent-line'></div>", unsafe_allow_html=True)
    
    st.markdown("""
    <p style='font-size: 1.1rem; margin-bottom: 3rem;'>
    A trajectory from full-stack engineering to strategic AI consulting—each role building 
    toward the synthesis of technical excellence and business transformation.
    </p>
    """, unsafe_allow_html=True)
    
    # Timeline
    st.markdown("""
    <div class='timeline-item'>
        <div class='timeline-dot'></div>
        <div class='timeline-period'>July 2024 – Present</div>
        <div class='timeline-title'>Technical Consultant</div>
        <div class='timeline-company'>Digistore24 GmbH</div>
        <div class='timeline-description'>
        Managing strategic technical consulting for high-revenue vendor relationships in a multi-million Euro ecosystem. 
        Translating complex business requirements into scalable technical solutions.
        </div>
        <div class='timeline-impact'>
        <strong>Key Impact:</strong> Authored the internal 'AI-First Company' strategic paper, defining organizational 
        transformation frameworks. Contributed to AI-powered onboarding system, reducing manual workload by 80% through 
        custom AI test cases and intelligent automation.
        </div>
    </div>
    
    <div class='timeline-item'>
        <div class='timeline-dot'></div>
        <div class='timeline-period'>July 2020 – December 2024</div>
        <div class='timeline-title'>Software & Systems Architect</div>
        <div class='timeline-company'>Independent / Freelance</div>
        <div class='timeline-description'>
        Developing bespoke automation systems and custom software architectures for private clients. 
        Specializing in transforming complex business ideas into production-ready digital products. 
        Full ownership of architecture, implementation, and deployment.
        </div>
        <div class='timeline-impact'>
        <strong>Focus Areas:</strong> Custom automation frameworks, AI integration, system architecture design, 
        and strategic technical consulting for transformation projects.
        </div>
    </div>
    
    <div class='timeline-item'>
        <div class='timeline-dot'></div>
        <div class='timeline-period'>July 2021 – June 2024</div>
        <div class='timeline-title'>Web Developer</div>
        <div class='timeline-company'>fuxteufelsweb GmbH & Co. KG</div>
        <div class='timeline-description'>
        Custom software architecture and specialized business solutions beyond standard frameworks. 
        Designed and implemented tailored systems for clients requiring bespoke technical approaches.
        </div>
        <div class='timeline-impact'>
        <strong>Expertise:</strong> Custom CMS development, API design, complex data workflows, 
        and integration of third-party systems into cohesive business platforms.
        </div>
    </div>
    
    <div class='timeline-item'>
        <div class='timeline-dot'></div>
        <div class='timeline-period'>March 2020 – June 2021</div>
        <div class='timeline-title'>Full-Stack Developer</div>
        <div class='timeline-company'>day4 solutions GmbH</div>
        <div class='timeline-description'>
        Full-stack development with Angular and Node.js. Engineered robust, scalable web applications 
        with focus on clean architecture and maintainable code.
        </div>
        <div class='timeline-impact'>
        <strong>DevOps:</strong> Designed and implemented automated CI/CD pipelines using Jenkins and GitLab 
        for high-availability production environments. Reduced deployment time by 60% and improved system reliability.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Technical Proficiency
    st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)
    st.markdown("## Technical Proficiency")
    st.markdown("""
    <p style='font-size: 1rem; margin-bottom: 2rem; color: var(--text-secondary);'>
    Bridging strategic AI consulting with hands-on engineering execution.
    </p>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='card'>
        <h3 style='margin-top: 0;'>AI Strategy & Quality Assurance</h3>
        <p>
        <strong>Advanced Prompt Engineering</strong><br>
        Designing high-precision prompts for complex business logic and multi-step reasoning tasks.<br><br>
        
        <strong>AI Quality Assurance</strong><br>
        Specialist in designing and verifying AI test cases to ensure reliability. 
        Proven impact: 80% workload reduction in onboarding processes.<br><br>
        
        <strong>Strategic AI Transformation</strong><br>
        Authoring frameworks and concept papers for organizational "AI-First" transitions and long-term integration.
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='card'>
        <h3 style='margin-top: 0;'>Engineering & Architecture</h3>
        <p>
        <strong>Core Languages</strong><br>
        Python, TypeScript, Node.js, Angular, PHP<br><br>
        
        <strong>Infrastructure & DevOps</strong><br>
        CI/CD Pipelines (Jenkins, GitLab), automated software delivery, high-availability production environments.<br><br>
        
        <strong>Architecture & Databases</strong><br>
        API Design, System Scalability, Relational Databases (PostgreSQL), custom web architectures.
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='card'>
        <h3 style='margin-top: 0;'>Enterprise Automation & Ecosystems</h3>
        <p>
        <strong>Zendesk API & Automation</strong><br>
        Deep integration of AI workflows into enterprise-level support systems. 
        Automated 30% of B2B support tickets (~400/month).<br><br>
        
        <strong>Digistore24 Platform Expertise</strong><br>
        Technical optimization and integration for high-revenue vendor ecosystems. 
        Managing multi-million Euro technical relationships.<br><br>
        
        <strong>Process Mapping & Translation</strong><br>
        Converting manual business requirements into automated, scalable technical workflows 
        with measurable efficiency gains.
        </p>
        </div>
        """, unsafe_allow_html=True)


# ============================================================================
# PAGE: PROJECTS
# ============================================================================

def get_projects_data():
    """Return hardcoded projects data"""
    return [
        {
            'id': 'example-project',
            'title': 'Example AI Platform',
            'subtitle': 'Advanced Machine Learning Infrastructure',
            'tags': ['AI/ML', 'Python', 'Cloud'],
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
            'challenge': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'solution': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident.',
            'tech_stack': [
                'Python & FastAPI',
                'TensorFlow / PyTorch',
                'Docker & Kubernetes',
                'PostgreSQL & Redis',
                'AWS / Azure Cloud'
            ],
            'impact': [
                ('<strong>85%</strong>', 'efficiency increase'),
                ('<strong>$500K+</strong>', 'annual cost savings'),
                ('<strong>10,000+</strong>', 'daily active users'),
                ('<strong>99.9%</strong>', 'system uptime')
            ]
        }
    ]


def page_projects():
    """Featured projects and case studies"""

    st.markdown("# Projects")
    st.markdown("<div class='accent-line'></div>", unsafe_allow_html=True)

    st.markdown("""
    <p style='font-size: 1.1rem; margin-bottom: 3rem;'>
    Selected projects demonstrating the intersection of strategic thinking and technical execution.
    </p>
    """, unsafe_allow_html=True)

    # Get projects data
    projects = get_projects_data()

    # Project selection state
    if 'selected_project' not in st.session_state:
        st.session_state.selected_project = None

    if st.session_state.selected_project:
        # Show selected project details
        project = next((p for p in projects if p['id'] == st.session_state.selected_project), None)

        if project:
            if st.button("← Back to all projects"):
                st.session_state.selected_project = None
                st.rerun()

            st.markdown("<div class='small-spacer'></div>", unsafe_allow_html=True)

            # Project header
            tags_html = ''.join([f"<span class='project-tag'>{tag}</span>" for tag in project['tags']])
            st.markdown(f"""
            <div class='project-card'>
                {tags_html}
                <h2 style='margin-top: 1.5rem; color: #f1f5f9;'>{project['title']}</h2>
                <h3 style='color: #94a3b8; font-weight: 400; margin-top: 0.5rem;'>
                {project['subtitle']}
                </h3>
                <p style='font-size: 1.1rem; margin-top: 1.5rem; line-height: 1.8;'>
                {project['description']}
                </p>
            </div>
            """, unsafe_allow_html=True)

            # Project details
            col1, col2 = st.columns(2)

            with col1:
                st.markdown(f"""
                <div class='card'>
                <h3 style='margin-top: 0;'>The Challenge</h3>
                <p>{project['challenge']}</p>
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class='card'>
                <h3 style='margin-top: 0;'>The Solution</h3>
                <p>{project['solution']}</p>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                tech_list = '<br>'.join([f'• {tech}' for tech in project['tech_stack']])
                st.markdown(f"""
                <div class='card'>
                <h3 style='margin-top: 0;'>Technical Stack</h3>
                <p>{tech_list}</p>
                </div>
                """, unsafe_allow_html=True)

                impact_html = '<br>'.join([f'{metric} {desc}' for metric, desc in project['impact']])
                st.markdown(f"""
                <div class='card'>
                <h3 style='margin-top: 0;'>Impact</h3>
                <p>{impact_html}</p>
                </div>
                """, unsafe_allow_html=True)

    else:
        # Show project cards overview
        for project in projects:
            tags_html = ''.join([f"<span class='project-tag'>{tag}</span>" for tag in project['tags']])
            st.markdown(f"""
            <div class='blog-card'>
                {tags_html}
                <h3 style='margin: 0.75rem 0;'>{project['title']}</h3>
                <p style='color: #94a3b8;'>{project['subtitle']}</p>
                <p style='margin-top: 1rem;'>{project['description']}</p>
            </div>
            """, unsafe_allow_html=True)

            if st.button(f"View Project: {project['title']}", key=f"project_{project['id']}"):
                st.session_state.selected_project = project['id']
                st.rerun()


# ============================================================================
# PAGE: INSIGHTS (BLOG)
# ============================================================================

def load_blog_posts():
    """Load blog posts from content directory"""
    content_dir = Path("content")
    posts = []
    
    if content_dir.exists():
        for md_file in sorted(content_dir.glob("*.md"), reverse=True):
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Extract title (first # heading)
                title = "Untitled"
                for line in content.split('\n'):
                    if line.startswith('# '):
                        title = line.replace('# ', '').strip()
                        break
                
                posts.append({
                    'title': title,
                    'filename': md_file.stem,
                    'content': content,
                    'file': md_file.name
                })
    
    return posts


def page_blog():
    """Blog articles and insights"""

    st.markdown("# Blog")
    st.markdown("<div class='accent-line'></div>", unsafe_allow_html=True)

    st.markdown("""
    <p style='font-size: 1.1rem; margin-bottom: 3rem;'>
    Thoughts on AI, engineering, and building the future.
    </p>
    """, unsafe_allow_html=True)
    
    # Load blog posts
    posts = load_blog_posts()
    
    if not posts:
        st.info("Articles coming soon. Check back for insights on AI engineering and technical strategy.")
        return
    
    # Blog post selection
    if 'selected_post' not in st.session_state:
        st.session_state.selected_post = None
    
    if st.session_state.selected_post:
        # Show selected post
        post = next((p for p in posts if p['filename'] == st.session_state.selected_post), None)
        
        if post:
            if st.button("← Back to all articles"):
                st.session_state.selected_post = None
                st.rerun()
            
            st.markdown(f"<div class='small-spacer'></div>", unsafe_allow_html=True)
            st.markdown(post['content'], unsafe_allow_html=True)
    else:
        # Show post list
        for post in posts:
            st.markdown(f"""
            <div class='blog-card'>
                <div class='blog-date'>Recent</div>
                <h3 style='margin: 0.5rem 0;'>{post['title']}</h3>
                <p>Click to read more...</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"Read: {post['title']}", key=post['filename']):
                st.session_state.selected_post = post['filename']
                st.rerun()


# ============================================================================
# PAGE: PAPERS (CONCEPT PAPERS)
# ============================================================================

def load_papers():
    """Load concept papers from papers directory"""
    papers_dir = Path("papers")
    papers = []

    if papers_dir.exists():
        for md_file in sorted(papers_dir.glob("*.md"), reverse=True):
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Extract title (first # heading)
                title = "Untitled"
                for line in content.split('\n'):
                    if line.startswith('# '):
                        title = line.replace('# ', '').strip()
                        break

                papers.append({
                    'title': title,
                    'filename': md_file.stem,
                    'content': content,
                    'file': md_file.name
                })

    return papers


def page_papers():
    """Research papers and concept documents"""

    st.markdown("# Research & Concept Papers")
    st.markdown("<div class='accent-line'></div>", unsafe_allow_html=True)

    st.markdown("""
    <p style='font-size: 1.1rem; margin-bottom: 3rem;'>
    Strategic frameworks, research, and deep-dive analyses on AI transformation and technical architecture.
    </p>
    """, unsafe_allow_html=True)

    # Load papers
    papers = load_papers()

    if not papers:
        st.info("Papers coming soon. Check back for in-depth research and strategic frameworks.")
        return

    # Paper selection
    if 'selected_paper' not in st.session_state:
        st.session_state.selected_paper = None

    if st.session_state.selected_paper:
        # Show selected paper
        paper = next((p for p in papers if p['filename'] == st.session_state.selected_paper), None)

        if paper:
            if st.button("← Back to all papers"):
                st.session_state.selected_paper = None
                st.rerun()

            st.markdown(f"<div class='small-spacer'></div>", unsafe_allow_html=True)
            st.markdown(paper['content'], unsafe_allow_html=True)
    else:
        # Show paper cards
        for paper in papers:
            st.markdown(f"""
            <div class='blog-card'>
                <div class='blog-date'>Research Paper</div>
                <h3 style='margin: 0.5rem 0;'>{paper['title']}</h3>
                <p>Click to read the full paper...</p>
            </div>
            """, unsafe_allow_html=True)

            if st.button(f"Read: {paper['title']}", key=f"paper_{paper['filename']}"):
                st.session_state.selected_paper = paper['filename']
                st.rerun()


# ============================================================================
# FOOTER WITH CONTACT
# ============================================================================

def render_footer():
    """Render footer with contact form"""
    
    st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)
    st.markdown("---")
    
    # 2-column layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("## Let's Connect")
        st.markdown("""
        <p style='font-size: 1.05rem; line-height: 1.8; margin-bottom: 1.5rem;'>
        I'm always open to discussing the intersection of business logic, engineering, 
        and the evolving landscape of AI. Whether you want to exchange ideas, talk about 
        technical challenges, or just connect—feel free to reach out.
        </p>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <ul class='contact-reasons'>
            <li>Technical Architecture Exchange</li>
            <li>AI Transformation Strategies</li>
            <li>Professional Networking</li>
        </ul>
        """, unsafe_allow_html=True)
    
    with col2:
        # Additional inline styles to ensure form styling works
        st.markdown("""
        <style>
        /* Force form inputs to match theme */
        div[data-testid="stForm"] input[type="text"],
        div[data-testid="stForm"] input[type="email"],
        div[data-testid="stForm"] textarea {
            background-color: #0f172a !important;
            color: #f1f5f9 !important;
            border: 1px solid rgba(148, 163, 184, 0.2) !important;
        }
        
        /* Force button to be indigo */
        div[data-testid="stForm"] button[type="submit"],
        div[data-testid="stForm"] button[kind="primary"] {
            background-color: #6366f1 !important;
            background: #6366f1 !important;
            color: white !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
        with st.form(key='contact_form'):
            name = st.text_input("Name", key="contact_name")
            email = st.text_input("Email", key="contact_email")
            message = st.text_area("Message", height=120, key="contact_message")
            
            submitted = st.form_submit_button("Send Message", type="primary", use_container_width=True)
            
            if submitted:
                if name and email and message:
                    st.success("Message sent. I'll get back to you soon.")
                    # TODO: Integrate with email service or form backend
                else:
                    st.warning("Please fill out all fields.")
    
    st.markdown("<div class='small-spacer'></div>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: center; color: #64748b; font-size: 0.9rem;'>
        <p>© 2025 Jakob Figur | Technical Consultant & AI Engineer & Researcher</p>
        <div class='footer-social-icons'>
            <a href='https://www.linkedin.com/in/jakob-figur-2b9501367/' target='_blank' class='social-icon' title='LinkedIn'>
                <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
                </svg>
            </a>
            <a href='https://github.com/jakobfigur' target='_blank' class='social-icon' title='GitHub'>
                <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/>
                </svg>
            </a>
            <a href='https://x.com/JakobFigur' target='_blank' class='social-icon' title='X'>
                <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
                </svg>
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ============================================================================
# MAIN APP
# ============================================================================

def main():
    """Main application logic"""
    
    # Render navigation and get selected page
    selected_page = render_navigation()
    
    # Route to selected page
    if selected_page == "Identity":
        page_identity()
    elif selected_page == "Experience":
        page_experience()
    elif selected_page == "Projects":
        page_projects()
    elif selected_page == "Blog":
        page_blog()
    elif selected_page == "Papers":
        page_papers()

    # Render footer on all pages
    render_footer()


if __name__ == "__main__":
    main()
