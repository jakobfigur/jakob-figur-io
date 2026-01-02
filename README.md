# Personal Website · Jakob Figur

My personal brand website - a journey from Streamlit prototype to production-ready Astro site.

## 🚀 The Evolution

**Phase 1: Streamlit Experiment**
Started with a bold question: Can you build a clean, high-end website with Streamlit? Turns out: Yes, you can. Built the entire site in Python with Streamlit for rapid iteration and testing. Perfect for prototyping and getting content structure right.

**Phase 2: Production Reality**
When it came time to deploy for real, we hit Streamlit's limits. The biggest issue: clickable cards. We wanted native, intuitive UX where entire cards are clickable - something trivial in HTML but fundamentally limited in Streamlit (which requires `st.button()` for interactions).

**Phase 3: Migration to Astro**
Decided to go "full retarded" and migrate to Astro for production. Why Astro?
- Native HTML/CSS control = clickable cards without hacks
- Static site generation = blazing fast performance
- Better SEO out of the box
- Content Collections for type-safe markdown management
- Still keeps the same dark, modern vibe

The Streamlit prototype helped us nail the content and design. Astro gives us the UX polish for production.

## 💭 The Vibe

Dark. Modern. Lean. No bullshit, just content. Indigo accents, lots of whitespace, precise typography.

The goal: A website that shows who I am and what I do – Technical Consulting & AI Engineering – without the typical portfolio clichés.

## Tech Stack

**Current (Production):**
- **Astro** - Static site framework
- **TypeScript** - Type safety
- **Content Collections** - Type-safe markdown CMS
- **Nginx** - Static file serving
- **Docker** - Containerized deployment

**Previous (Prototype):**
- ~~Streamlit~~ - Used for rapid prototyping
- ~~Python~~ - Replaced with TypeScript/Astro

## Local Development

```bash
# Install dependencies
npm install

# Run dev server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

Opens at `http://localhost:4321` (dev) or `http://localhost:8501` (production container)

## Docker Deployment

```bash
# Build the image
docker build -t jakob-figur-io .

# Run the container
docker run -d --name jakob-website --restart unless-stopped -p 8501:8501 jakob-figur-io
```

The Dockerfile uses multi-stage build:
1. **Build stage**: Node.js builds the Astro static site
2. **Production stage**: Nginx serves the static files

## Structure

```
jakob-figur-io/
├── src/
│   ├── pages/                # Page routes
│   │   ├── index.astro       # Identity page
│   │   ├── experience.astro  # Work history
│   │   ├── projects.astro    # Featured projects
│   │   ├── blog/             # Blog posts
│   │   │   ├── index.astro   # Blog listing
│   │   │   └── [slug].astro  # Individual posts
│   │   └── papers/           # Research papers
│   │       ├── index.astro   # Papers listing
│   │       └── [slug].astro  # Individual papers
│   ├── layouts/
│   │   └── BaseLayout.astro  # Main layout with nav/footer
│   ├── content/              # Content collections
│   │   ├── blog/             # Blog posts (markdown)
│   │   ├── papers/           # Research papers (markdown)
│   │   └── config.ts         # Content schema
│   └── styles/
│       └── global.css        # Dark theme styles
├── astro.config.mjs          # Astro configuration
├── tsconfig.json             # TypeScript config
├── Dockerfile                # Multi-stage build
├── nginx.conf                # Nginx configuration
└── deploy.sh                 # Deployment script
```

## Adding Content

### Blog Posts

Create a new `.md` file in `src/content/blog/`:

```markdown
---
title: "Your Post Title"
date: "2025-01-02"
---

Your content here...

## Sections

More content...
```

The post automatically appears on `/blog` with a clickable card.

### Research Papers

Same as blog posts, but in `src/content/papers/`:

```markdown
---
title: "Your Paper Title"
date: "2025-01-02"
---

Abstract...

## Introduction

Content...
```

## Customization

### Design Tokens

CSS variables in `src/styles/global.css`:

```css
:root {
  --primary-color: #6366f1;        /* Indigo accent */
  --secondary-color: #475569;      /* Slate grey */
  --background-dark: #0f172a;      /* Main background */
  --background-card: #1e293b;      /* Card background */
  --text-primary: #f1f5f9;         /* Primary text */
  --text-secondary: #94a3b8;       /* Secondary text */
}
```

### Navigation

Update `src/layouts/BaseLayout.astro` to modify navigation links or footer.

### Content

- **Identity page**: `src/pages/index.astro` - Hero section and core competencies
- **Experience**: `src/pages/experience.astro` - Work timeline and skills
- **Projects**: `src/pages/projects.astro` - Featured project cards

## CI/CD Pipeline

Automatic deployment via GitHub Actions:

1. Push to `main` branch
2. GitHub Actions triggers
3. SSH into Hetzner server
4. Pulls latest code
5. Rebuilds Docker image
6. Restarts container
7. Site is live

Configuration: `.github/workflows/deploy.yml`

## 💭 Learnings

**From the Streamlit Phase:**
- Streamlit is surprisingly good for rapid prototyping
- Python is great for quick iteration and testing
- Custom CSS > Component libraries for clean design
- Got the content and structure right before committing to tech

**From the Astro Migration:**
- Framework choice matters for UX details
- Static sites are perfect for portfolios (speed + SEO)
- Content Collections provide great DX for markdown content
- Multi-stage Docker builds keep production images lean
- Sometimes you need to migrate to get the polish right

**Overall:**
- Prototype fast, migrate when needed
- UX polish matters for production
- Cursor makes both prototyping AND migration incredibly fast

---

**Built with ⚡ Astro and Cursor**
Jakob Figur · Technical Consultant & AI Engineer & Researcher
