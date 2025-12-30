"""
Jakob Figur | Technical Consultant & AI Systems Engineer
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
    page_title="Jakob Figur | Technical Consultant & AI Systems Engineer",
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
        st.markdown("**Technical Consultant @ Digistore24**  \n**AI Systems Engineer**")
        
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
            options=["Identity", "Experience", "Projects", "Insights"],
            icons=["house", "briefcase", "lightbulb", "book"],
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
        
        # Social Links
        st.markdown("#### Connect")
        st.markdown("""
        <a href='https://www.linkedin.com/in/jakob-figur-2b9501367/' target='_blank' class='social-link'>LinkedIn</a>
        <a href='https://github.com/jakobfigur' target='_blank' class='social-link'>GitHub</a>
        <a href='https://x.com/JakobFigur' target='_blank' class='social-link'>X</a>
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
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='card'>
        <h3 style='margin-top: 0;'>AI & Automation</h3>
        <p>
        • Large Language Models (GPT-4, Claude)<br>
        • LangChain, LangGraph, RAG Systems<br>
        • Prompt Engineering & Agent Design<br>
        • Vector Databases & Semantic Search<br>
        • Workflow Orchestration & Automation
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='card'>
        <h3 style='margin-top: 0;'>Engineering & Architecture</h3>
        <p>
        • Python, TypeScript, Node.js, Angular<br>
        • System Design & Scalability<br>
        • API Design & Microservices<br>
        • CI/CD (Jenkins, GitLab)<br>
        • Cloud Infrastructure & DevOps
        </p>
        </div>
        """, unsafe_allow_html=True)


# ============================================================================
# PAGE: PROJECTS
# ============================================================================

def page_projects():
    """Featured projects and case studies"""
    
    st.markdown("# Featured Work")
    st.markdown("<div class='accent-line'></div>", unsafe_allow_html=True)
    
    st.markdown("""
    <p style='font-size: 1.1rem; margin-bottom: 3rem;'>
    Selected projects demonstrating the intersection of strategic thinking and technical execution.
    </p>
    """, unsafe_allow_html=True)
    
    # Featured Project: DigiDoc AI
    st.markdown("""
    <div class='project-card'>
        <span class='project-tag'>Featured</span>
        <span class='project-tag'>Agentic AI</span>
        <span class='project-tag'>Process Automation</span>
        
        <h2 style='margin-top: 1.5rem; color: #f1f5f9;'>DigiDoc AI</h2>
        <h3 style='color: #94a3b8; font-weight: 400; margin-top: 0.5rem;'>
        Intelligent Document Processing & Workflow Automation
        </h3>
        
        <p style='font-size: 1.1rem; margin-top: 1.5rem; line-height: 1.8;'>
        An agentic AI system transforming unstructured documents into actionable insights 
        and automated workflows. Designed for enterprises handling high-volume document processing 
        with complex validation requirements.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Project Details
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='card'>
        <h3 style='margin-top: 0;'>The Challenge</h3>
        <p>
        Organizations processing thousands of documents monthly—invoices, contracts, reports—
        were losing countless hours to manual extraction, validation, and routing. Traditional OCR 
        couldn't handle document variability and contextual complexity.
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='card'>
        <h3 style='margin-top: 0;'>The Solution</h3>
        <p>
        An agentic AI system powered by LLMs that understands documents, not just reads them. 
        Multi-agent architecture with specialized agents for extraction, validation, classification, 
        and workflow orchestration. Self-improving through continuous feedback loops.
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='card'>
        <h3 style='margin-top: 0;'>Technical Architecture</h3>
        <p>
        • Vision models for layout understanding<br>
        • LLM-based extraction with structured outputs<br>
        • RAG system for domain-specific context<br>
        • Agent orchestration with LangGraph<br>
        • Vector DB for semantic search<br>
        • FastAPI backend with async processing
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='card'>
        <h3 style='margin-top: 0;'>Impact</h3>
        <p>
        <strong>85% reduction</strong> in manual processing time<br>
        <strong>95%+ accuracy</strong> on document classification<br>
        <strong>$200K+ annual savings</strong> per deployment<br>
        Processing <strong>10,000+ documents/month</strong> autonomously
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    # AI-First Company Paper
    st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='project-card'>
        <span class='project-tag'>Strategic Framework</span>
        <span class='project-tag'>Internal Research</span>
        
        <h2 style='margin-top: 1.5rem; color: #f1f5f9;'>AI-First Company Framework</h2>
        <h3 style='color: #94a3b8; font-weight: 400; margin-top: 0.5rem;'>
        Organizational Transformation Methodology
        </h3>
        
        <p style='font-size: 1.1rem; margin-top: 1.5rem; line-height: 1.8;'>
        Internal strategic paper defining the transition from AI-adjacent to AI-native organizations. 
        Frameworks for cultural transformation, technical infrastructure, and operational integration 
        of autonomous AI systems at scale.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Additional Projects
    st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)
    st.markdown("## Additional Work")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='card'>
        <h3 style='margin-top: 0;'>B2B Support Automation</h3>
        <span class='project-tag'>LangChain</span>
        <span class='project-tag'>RAG</span>
        <p style='margin-top: 1rem;'>
        Autonomous support agent handling 30% of incoming B2B tickets (~400/month) with intelligent 
        routing and context-aware responses. Integrated with existing ticketing systems.
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='card'>
        <h3 style='margin-top: 0;'>Custom DevOps Pipelines</h3>
        <span class='project-tag'>Jenkins</span>
        <span class='project-tag'>GitLab CI</span>
        <p style='margin-top: 1rem;'>
        Engineered high-availability CI/CD pipelines reducing deployment time by 60% while improving 
        reliability and rollback capabilities for mission-critical production environments.
        </p>
        </div>
        """, unsafe_allow_html=True)


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


def page_insights():
    """Blog and thought leadership"""
    
    st.markdown("# Insights & Perspectives")
    st.markdown("<div class='accent-line'></div>", unsafe_allow_html=True)
    
    st.markdown("""
    <p style='font-size: 1.1rem; margin-bottom: 3rem;'>
    Thoughts on AI systems engineering, strategic architecture, and the intersection of 
    technology with human potential.
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
# FOOTER WITH CONTACT
# ============================================================================

def render_footer():
    """Render footer with contact form"""
    
    st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown("""
    <div class='contact-section'>
        <h3 style='margin-top: 0;'>Let's Build Something Intelligent</h3>
        <p>Interested in exploring AI transformation for your organization? 
        Let's discuss how intelligent systems can drive measurable impact.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Name", key="contact_name")
        email = st.text_input("Email", key="contact_email")
    
    with col2:
        message = st.text_area("Message", height=100, key="contact_message")
    
    if st.button("Send Message", type="primary"):
        if name and email and message:
            st.success("Message sent. I'll get back to you soon.")
            # TODO: Integrate with email service or form backend
        else:
            st.warning("Please fill out all fields.")
    
    st.markdown("<div class='small-spacer'></div>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: center; color: #64748b; font-size: 0.9rem;'>
        <p>© 2025 Jakob Figur | Technical Consultant & AI Systems Engineer</p>
        <p>
            <a href='https://www.linkedin.com/in/jakob-figur-2b9501367/' target='_blank' class='social-link'>LinkedIn</a> · 
            <a href='https://github.com/jakobfigur' target='_blank' class='social-link'>GitHub</a> · 
            <a href='https://x.com/JakobFigur' target='_blank' class='social-link'>X</a>
        </p>
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
    elif selected_page == "Insights":
        page_insights()
    
    # Render footer on all pages
    render_footer()


if __name__ == "__main__":
    main()
