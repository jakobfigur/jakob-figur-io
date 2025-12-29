"""
Jakob Figur | Technical Consulting & AI
Personal Brand Website
"""

import streamlit as st
from streamlit_option_menu import option_menu
from pathlib import Path
import os

# ============================================================================
# PAGE CONFIG & STYLING
# ============================================================================

st.set_page_config(
    page_title="Jakob Figur | Technical Consulting & AI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Dark, Modern, Lean Design
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
    }
    
    h2 {
        font-weight: 600;
        letter-spacing: -0.01em;
        color: var(--text-primary);
        margin-top: 2.5rem;
        margin-bottom: 1rem;
    }
    
    h3 {
        font-weight: 500;
        color: var(--primary-color);
        margin-top: 1.5rem;
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
    
    /* Timeline */
    .timeline-item {
        position: relative;
        padding-left: 2.5rem;
        padding-bottom: 2rem;
        border-left: 2px solid var(--secondary-color);
        margin-left: 1rem;
    }
    
    .timeline-item:last-child {
        border-left: 2px solid transparent;
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
    
    .timeline-year {
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
        line-height: 1.6;
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
    
    /* Sidebar */
    .css-1d391kg {
        background-color: var(--background-card);
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
</style>
""", unsafe_allow_html=True)


# ============================================================================
# NAVIGATION
# ============================================================================

def render_navigation():
    """Render sidebar navigation"""
    with st.sidebar:
        st.markdown("### Jakob Figur")
        st.markdown("Technical Consultant & AI Engineer")
        st.markdown("<div class='accent-line'></div>", unsafe_allow_html=True)
        
        selected = option_menu(
            menu_title=None,
            options=["Identity", "Expertise", "Solutions", "Insights"],
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
        
        # Quick Contact
        st.markdown("##### Quick Connect")
        st.markdown("📧 contact@example.com")
        st.markdown("🔗 [LinkedIn](#) | [GitHub](#)")
        
    return selected


# ============================================================================
# PAGE: IDENTITY (HOME)
# ============================================================================

def page_identity():
    """Landing page - Identity & Vision"""
    
    # Hero Section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("# Architecting the Future of Business with Agentic AI")
        st.markdown("<div class='accent-line'></div>", unsafe_allow_html=True)
        
        st.markdown("""
        <p style='font-size: 1.2rem; margin-top: 2rem;'>
        Where <strong>technical consulting</strong> meets <strong>artificial intelligence</strong> — 
        building autonomous systems that don't just automate tasks, but understand context, 
        make decisions, and drive business transformation.
        </p>
        """, unsafe_allow_html=True)
        
        st.markdown("<div class='small-spacer'></div>", unsafe_allow_html=True)
        
        # Value Proposition
        st.markdown("""
        <div class='card'>
        <h3>The Synthesis</h3>
        <p>
        I bridge the gap between business requirements and AI capabilities. 
        Not just implementing models, but architecting intelligent systems that align 
        with strategic goals, scale with your growth, and create measurable impact.
        </p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("<div class='small-spacer'></div>", unsafe_allow_html=True)
        st.markdown("""
        <div style='background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%); 
                    border-radius: 16px; padding: 2rem; text-align: center;'>
            <h2 style='color: white; margin: 0;'>⚡</h2>
            <p style='color: white; margin-top: 1rem;'>Engineering Intelligence</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Core Focus Areas
    st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)
    st.markdown("## Core Focus Areas")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='card'>
        <h3>🎯 Strategic AI Consulting</h3>
        <p>Identifying high-impact AI opportunities and architecting implementation roadmaps 
        that align with business objectives.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='card'>
        <h3>🤖 Agentic Systems</h3>
        <p>Building autonomous AI agents that perceive, reason, and act — 
        moving beyond simple automation to intelligent decision-making.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='card'>
        <h3>⚙️ Process Transformation</h3>
        <p>Reimagining workflows with AI-first thinking, optimizing for both 
        human collaboration and machine intelligence.</p>
        </div>
        """, unsafe_allow_html=True)


# ============================================================================
# PAGE: EXPERTISE (CAREER)
# ============================================================================

def page_expertise():
    """Career timeline and experience"""
    
    st.markdown("# Expertise & Experience")
    st.markdown("<div class='accent-line'></div>", unsafe_allow_html=True)
    
    st.markdown("""
    <p style='font-size: 1.1rem; margin-bottom: 3rem;'>
    An evolution from technical consulting to AI engineering — 
    each step building toward the synthesis of business acumen and artificial intelligence.
    </p>
    """, unsafe_allow_html=True)
    
    # Timeline
    experiences = [
        {
            "year": "2024 - Present",
            "title": "AI Engineer & Technical Consultant",
            "company": "Independent Practice",
            "description": "Specializing in agentic AI systems and process automation. Building intelligent workflows that transform how businesses operate, with focus on LLM integration, RAG systems, and autonomous agents."
        },
        {
            "year": "2022 - 2024",
            "title": "Senior Technical Consultant",
            "company": "Digistore24",
            "description": "Led technical consulting initiatives for digital product ecosystem. Architected scalable solutions, optimized payment processing workflows, and advised on technical strategy for multi-million transaction platform."
        },
        {
            "year": "2020 - 2022",
            "title": "Solutions Architect",
            "company": "Enterprise Software",
            "description": "Designed and implemented enterprise-grade software architectures. Bridged business requirements with technical execution, leading cross-functional teams in delivering complex B2B solutions."
        },
        {
            "year": "2018 - 2020",
            "title": "Software Engineer",
            "company": "Tech Startup",
            "description": "Full-stack development in fast-paced startup environment. Built scalable web applications, implemented CI/CD pipelines, and contributed to product strategy."
        }
    ]
    
    for exp in experiences:
        st.markdown(f"""
        <div class='timeline-item'>
            <div class='timeline-dot'></div>
            <div class='timeline-year'>{exp['year']}</div>
            <div class='timeline-title'>{exp['title']}</div>
            <div class='timeline-company'>{exp['company']}</div>
            <div class='timeline-description'>{exp['description']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Skills & Technologies
    st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)
    st.markdown("## Technical Stack")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='card'>
        <h3>AI & Machine Learning</h3>
        <p>
        • Large Language Models (GPT-4, Claude, LLaMA)<br>
        • LangChain, LlamaIndex, CrewAI<br>
        • RAG Systems & Vector Databases<br>
        • Prompt Engineering & Fine-tuning<br>
        • Agentic Workflows & Orchestration
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='card'>
        <h3>Engineering & Architecture</h3>
        <p>
        • Python, TypeScript, Go<br>
        • Cloud Platforms (AWS, Azure, GCP)<br>
        • Microservices & API Design<br>
        • Docker, Kubernetes<br>
        • System Design & Scalability
        </p>
        </div>
        """, unsafe_allow_html=True)


# ============================================================================
# PAGE: SOLUTIONS (PROJECTS)
# ============================================================================

def page_solutions():
    """Featured projects and case studies"""
    
    st.markdown("# Solutions & Projects")
    st.markdown("<div class='accent-line'></div>", unsafe_allow_html=True)
    
    st.markdown("""
    <p style='font-size: 1.1rem; margin-bottom: 3rem;'>
    Real-world applications of AI engineering and technical consulting — 
    from concept to production-grade solutions.
    </p>
    """, unsafe_allow_html=True)
    
    # Featured Project: DigiDoc AI
    st.markdown("""
    <div class='project-card'>
        <span class='project-tag'>Featured Case Study</span>
        <span class='project-tag'>Agentic AI</span>
        <span class='project-tag'>Process Automation</span>
        
        <h2 style='margin-top: 1.5rem; color: #f1f5f9;'>DigiDoc AI</h2>
        <h3 style='color: #94a3b8; font-weight: 400; margin-top: 0.5rem;'>
        Intelligent Document Processing & Workflow Automation
        </h3>
        
        <p style='font-size: 1.1rem; margin-top: 1.5rem; line-height: 1.8;'>
        An agentic AI system that transforms unstructured documents into actionable insights 
        and automated workflows. Built for enterprises handling high-volume document processing.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Project Details
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='card'>
        <h3>The Challenge</h3>
        <p>
        Organizations were drowning in documents — invoices, contracts, reports — 
        spending countless hours on manual data extraction, validation, and routing. 
        Traditional OCR couldn't handle the complexity and variability of real-world documents.
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='card'>
        <h3>The Solution</h3>
        <p>
        An agentic AI system powered by LLMs that doesn't just extract text, but <em>understands</em> 
        documents. Multi-agent architecture with specialized agents for extraction, validation, 
        classification, and workflow orchestration. Self-improving through feedback loops.
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='card'>
        <h3>Technical Architecture</h3>
        <p>
        • <strong>Vision Models</strong> for layout understanding<br>
        • <strong>LLM-based extraction</strong> with structured outputs<br>
        • <strong>RAG system</strong> for domain-specific context<br>
        • <strong>Agent orchestration</strong> with LangGraph<br>
        • <strong>Vector DB</strong> for semantic search & retrieval<br>
        • <strong>FastAPI backend</strong> with async processing
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='card'>
        <h3>Impact</h3>
        <p>
        <strong>85% reduction</strong> in manual processing time<br>
        <strong>95%+ accuracy</strong> on document classification<br>
        <strong>$200K+ annual savings</strong> per deployment<br>
        Handling <strong>10,000+ documents/month</strong> autonomously
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Other Projects
    st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)
    st.markdown("## Additional Projects")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='card'>
        <h3>AI-Powered Customer Support</h3>
        <span class='project-tag'>LangChain</span>
        <span class='project-tag'>RAG</span>
        <p style='margin-top: 1rem;'>
        Autonomous support agent handling L1 queries with 70% resolution rate, 
        integrating with existing ticketing systems and knowledge bases.
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='card'>
        <h3>Predictive Analytics Dashboard</h3>
        <span class='project-tag'>ML Pipeline</span>
        <span class='project-tag'>Real-time</span>
        <p style='margin-top: 1rem;'>
        Real-time forecasting system for e-commerce, predicting inventory needs 
        and optimizing supply chain with ML models and live data integration.
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
    Thoughts on AI engineering, technical architecture, and the future of intelligent systems.
    </p>
    """, unsafe_allow_html=True)
    
    # Load blog posts
    posts = load_blog_posts()
    
    if not posts:
        st.info("📝 Blog posts coming soon. Check back for insights on AI engineering and technical consulting.")
        return
    
    # Blog post selection
    if 'selected_post' not in st.session_state:
        st.session_state.selected_post = None
    
    if st.session_state.selected_post:
        # Show selected post
        post = next((p for p in posts if p['filename'] == st.session_state.selected_post), None)
        
        if post:
            if st.button("← Back to all posts"):
                st.session_state.selected_post = None
                st.rerun()
            
            st.markdown(f"<div class='small-spacer'></div>", unsafe_allow_html=True)
            st.markdown(post['content'], unsafe_allow_html=True)
    else:
        # Show post list
        for post in posts:
            st.markdown(f"""
            <div class='blog-card' onclick=''>
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
        <p>Interested in exploring AI solutions for your business? Let's discuss how 
        agentic systems can transform your operations.</p>
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
            st.success("✓ Message sent! I'll get back to you soon.")
            # TODO: Integrate with email service or form backend
        else:
            st.warning("Please fill out all fields.")
    
    st.markdown("<div class='small-spacer'></div>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: center; color: #64748b; font-size: 0.9rem;'>
        <p>© 2025 Jakob Figur | Technical Consulting & AI Engineering</p>
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
    elif selected_page == "Expertise":
        page_expertise()
    elif selected_page == "Solutions":
        page_solutions()
    elif selected_page == "Insights":
        page_insights()
    
    # Render footer on all pages
    render_footer()


if __name__ == "__main__":
    main()

