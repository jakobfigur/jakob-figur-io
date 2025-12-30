# Personal Website · Jakob Figur

My personal brand website, vibe-coded with Python, Streamlit & Cursor.

An experiment: Can you build a clean, high-end website with Streamlit? Turns out: Yes.

## 💭 The Vibe

Dark. Modern. Lean. No bullshit, just content. Indigo accents, lots of whitespace, precise typography.

The goal: A website that shows who I am and what I do – Technical Consulting & AI Engineering – without the typical portfolio clichés.

## 🛠 Tech Stack

- **Streamlit** as framework (because: why not?)
- **Python** (obviously)
- **Markdown** for blog posts
- **Pure CSS** for the dark theme
- **Cursor** for rapid iteration

## 🚀 Local Setup

If you want to run this locally:

```bash
# Virtual Environment
python -m venv venv
source venv/bin/activate

# Dependencies
pip install -r requirements.txt

# Run
streamlit run app.py
```

Opens automatically at `http://localhost:8501`

## 📁 Structure

```
jakob-figur-io/
├── app.py                 # The heart of it all
├── requirements.txt       # Dependencies
├── content/              # Blog posts as Markdown
│   └── the-ai-pivot.md  
├── assets/               # Images, icons etc.
│   ├── images/
│   └── icons/
└── README.md
```

## ✍️ Adding Blog Posts

Just drop a new `.md` file in `content/`:

```markdown
# Post Title

Intro...

## Section

Content...
```

The post automatically appears in the "Insights" section.

## 🎨 Customization

### Content

Everything in `app.py`:
- **Line 18**: Page title & favicon
- **Sidebar** (`render_navigation`): Contact info & links
- **Experience Timeline** (`page_expertise`): My career stations
- **Projects** (`page_solutions`): Case studies

### Design

CSS variables at the top of `app.py`:

- `--primary-color`: Indigo (#6366f1)
- `--secondary-color`: Slate Grey (#475569)
- `--background-dark`: Main BG
- `--text-primary`: Text color

Just change them for different colors/vibes.

## 🚀 Deployment

Runs anywhere Python runs:

- **Streamlit Cloud** – Free tier, 2 min setup
- **Docker** – Container and you're good
- **Any VPS** – Python + `streamlit run app.py`

```bash
# Develop with auto-reload
streamlit run app.py --server.runOnSave true
```

## 📝 TODO

- [ ] Add project screenshots
- [ ] Make contact form functional (Formspree or similar)
- [ ] Optional analytics
- [ ] Maybe add profile pic to sidebar
- [ ] Write more blog posts

## 💭 Learnings

- Streamlit is surprisingly good for this
- Custom CSS > Component libraries for clean design
- Markdown-based CMS = simplicity wins
- Cursor makes iteration incredibly fast

---

**Vibe-coded with ⚡ and Cursor**  
Jakob Figur · Technical Consultant & AI Engineer
