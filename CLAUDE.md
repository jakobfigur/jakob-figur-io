# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal portfolio website for Jakob Figur built with **Streamlit** and **Python**. The site is a single-page application with navigation through a sidebar menu, demonstrating that clean, modern websites can be built with Streamlit beyond typical data apps.

**Tech Stack**: Python, Streamlit, streamlit-option-menu, Pillow, custom CSS

## Development Commands

### Setup and Running

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run development server (opens at http://localhost:8501)
streamlit run app.py

# Run with auto-reload on save
streamlit run app.py --server.runOnSave true
```

## Architecture

### Single-File Application

The entire application lives in `app.py` (~1200 lines). This is intentional for simplicity and reflects the project's "vibe-coded" philosophy.

**Key sections in app.py:**
- **Lines 1-525**: Page config, CSS variables, and comprehensive custom styling
- **Lines 527-628**: Navigation rendering (sidebar with profile, bio, social links)
- **Lines 630-724**: Identity page (landing/hero with 4 core competency pillars)
- **Lines 726-872**: Experience page (timeline view of professional history)
- **Lines 874-1015**: Projects page (featured work and case studies)
- **Lines 1017-1096**: Insights page (blog post listing and rendering)
- **Lines 1098-1189**: Footer with contact form
- **Lines 1191-1217**: Main routing logic

### CSS Customization

CSS is defined inline in `st.markdown()` at the top of app.py. Key CSS variables (lines 28-35):

```css
--primary-color: #6366f1     /* Indigo accent */
--secondary-color: #475569   /* Slate grey */
--background-dark: #0f172a   /* Main dark background */
--background-card: #1e293b   /* Card backgrounds */
--text-primary: #f1f5f9      /* Primary text color */
--text-secondary: #94a3b8    /* Secondary text color */
```

The design system includes custom components:
- `.card` - Standard content cards with left border accent
- `.pillar-card` - Core competency cards with top border
- `.timeline-item` - Career timeline entries with dots
- `.project-card` - Featured project showcases
- `.blog-card` - Blog post previews
- `.contact-form-container` - Styled form elements

### Content Management

**Blog Posts**: Markdown files in `content/` directory are automatically discovered and rendered.

- Each `.md` file becomes a blog post
- First `# Heading` is extracted as the title
- Posts are sorted by filename in reverse order
- Click-to-expand interface with session state management

**Assets**: Static files in `assets/` directory:
- `assets/images/profile.{jpeg,jpg,png}` - Profile photo for sidebar (auto-detected format)
- `assets/icons/` - Icon assets
- `assets/images/` - Other images

### State Management

The app uses Streamlit session state minimally:
- `st.session_state.selected_post` - Tracks which blog post is currently displayed (None = list view)

### Navigation Flow

Navigation is handled by `streamlit-option-menu` in the sidebar:
1. User selects page from sidebar menu
2. `render_navigation()` returns selected page name
3. `main()` routes to appropriate page function
4. Footer is rendered on all pages

## Content Customization

### Updating Personal Information

**Sidebar** (line 567-568): Name and title
**Experience Timeline** (lines 744-806): Career history with periods, titles, companies, descriptions
**Projects** (lines 891-1015): Featured work and case studies
**Core Competencies** (lines 659-704): The four pillar cards on Identity page

### Contact Form

Current contact form (lines 1153-1165) collects input but doesn't send emails. To make functional:
- Integrate with Formspree, SendGrid, or similar service
- Add form handler in the `if submitted:` block

### Styling Customization

To change the color scheme, modify CSS variables at lines 28-35, then adjust component-specific colors as needed. The design uses a consistent indigo (`#6366f1`) accent color throughout.

## Important Implementation Details

### Streamlit Component Override

Extensive CSS overrides force Streamlit's default components to match the dark theme (lines 257-335). This includes:
- Input fields background and border colors
- Button colors (Streamlit defaults to red, overridden to indigo)
- Form element styling
- Focus states with custom box-shadow

### Profile Image Handling

The app checks for profile images in multiple formats (lines 546-551):
```python
for ext in ['jpeg', 'jpg', 'png']:
    test_path = f"assets/images/profile.{ext}"
```

Images are base64-encoded for inline rendering to avoid serving static files.

### Social Links

Social icons are rendered as inline SVG (lines 608-626 and 1171-1187) for:
- LinkedIn
- GitHub
- X (Twitter)

Update URLs at these locations to change social links.

## File Structure

```
jakob-figur-io/
├── app.py                    # Main application (all code)
├── requirements.txt          # Python dependencies
├── content/                  # Blog posts as Markdown
│   └── *.md                 # Auto-discovered posts
├── assets/
│   ├── images/
│   │   └── profile.*        # Profile photo (jpeg/jpg/png)
│   └── icons/               # Icon assets
├── README.md                # Project documentation
└── CLAUDE.md                # This file
```

## Design Philosophy

This project intentionally uses a **single-file architecture** and **inline CSS** rather than separating concerns into modules. This reflects the "vibe-coded" rapid iteration approach mentioned in the README. The monolithic structure makes it easy to see the entire application at once and modify any part quickly.

The website proves Streamlit can be used beyond data apps by heavily customizing the UI with CSS while leveraging Streamlit's reactive framework for navigation and state management.
