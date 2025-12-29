# Jakob Figur | Technical Consulting & AI

A modern, high-end personal brand website built with Streamlit. Focused on technical consulting and AI engineering with a clean, dark, and professional design.

## 🎯 Features

- **Dark, Modern Design** — Lean aesthetics with carefully crafted typography and indigo accents
- **Responsive Layout** — Optimized for all screen sizes
- **Modular Architecture** — Clean, maintainable code structure
- **Dynamic Blog System** — Markdown-based content management
- **Interactive Navigation** — Smooth sidebar navigation with multiple sections

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or download this repository**

```bash
cd jakob-figur-io
```

2. **Create a virtual environment (recommended)**

```bash
python -m venv venv

# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the application**

```bash
streamlit run app.py
```

The website will open automatically in your default browser at `http://localhost:8501`

## 📁 Project Structure

```
jakob-figur-io/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── content/              # Blog posts (Markdown files)
│   └── the-ai-pivot.md  # Sample blog post
└── README.md            # This file
```

## ✍️ Adding Blog Posts

To add new blog posts:

1. Create a new Markdown file in the `content/` directory
2. Start with a `# Title` heading (this becomes the blog title)
3. Write your content using standard Markdown syntax
4. The post will automatically appear in the "Insights" section

**Example:**

```markdown
# My New Blog Post

This is the introduction to my post...

## Section 1

Content here...
```

## 🎨 Customization

### Updating Personal Information

Edit `app.py` and modify:

- **Line 18**: Page title and favicon
- **Sidebar** (render_navigation function): Contact information and links
- **Content sections**: Update experiences, projects, and personal details

### Styling

All custom CSS is in the `st.markdown()` block at the top of `app.py`. Modify colors, spacing, and design elements there:

- `--primary-color`: Main accent color (default: Indigo #6366f1)
- `--secondary-color`: Secondary accents (default: Slate Grey #475569)
- `--background-dark`: Main background
- `--text-primary`: Primary text color

### Adding New Sections

To add a new navigation item:

1. Add the option to the `option_menu()` in `render_navigation()`
2. Create a new `page_yourname()` function
3. Add the route in the `main()` function

## 🛠️ Technology Stack

- **Streamlit** — Web framework
- **streamlit-option-menu** — Enhanced navigation
- **Pillow** — Image processing (for future enhancements)
- **python-dotenv** — Environment configuration

## 📝 Configuration

For environment-specific settings (API keys, email service, etc.), create a `.env` file:

```env
# Example .env file
CONTACT_EMAIL=your-email@example.com
ANALYTICS_ID=your-analytics-id
```

Then load in `app.py`:

```python
from dotenv import load_dotenv
import os

load_dotenv()
email = os.getenv('CONTACT_EMAIL')
```

## 🚢 Deployment

### Streamlit Cloud (Recommended)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Deploy!

### Other Options

- **Docker**: Create a Dockerfile and deploy to any container platform
- **Heroku**: Use the Streamlit buildpack
- **AWS/GCP/Azure**: Deploy as a containerized application

## 🔧 Development

To run in development mode with auto-reload:

```bash
streamlit run app.py --server.runOnSave true
```

## 📫 Contact Integration

The contact form is currently a UI component. To make it functional:

1. Integrate with an email service (SendGrid, Mailgun, etc.)
2. Add a backend endpoint to handle form submissions
3. Or use a form service like Formspree or Basin

Example with Formspree:

```python
import requests

if st.button("Send Message"):
    response = requests.post(
        "https://formspree.io/f/YOUR_FORM_ID",
        data={"email": email, "message": message}
    )
```

## 🎯 Roadmap

- [ ] Add project images and screenshots
- [ ] Integrate analytics (Google Analytics / Plausible)
- [ ] Add RSS feed for blog posts
- [ ] Implement search functionality
- [ ] Add dark/light theme toggle
- [ ] Integrate contact form with email service

## 📄 License

This is a personal website template. Feel free to use it as inspiration for your own brand website.

---

**Built with ⚡ by Jakob Figur**  
Technical Consultant & AI Engineer

