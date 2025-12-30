# Assets

Images, icons and visual stuff for the website.

## Structure

```
assets/
├── images/
│   ├── profile.jpg       # Profile pic (if I use one)
│   └── projects/         # Project screenshots
│
└── icons/
    └── logo.png          # Logo/Personal brand icon
```

## Quick Specs

**Profile Picture**  
Square, ~400x400px, under 200KB

**Project Screenshots**  
PNG for UI, JPG for photos, max 1200px wide

**Icons**  
PNG/SVG, ~128x128px

## Usage

```python
from PIL import Image

# Load image
img = Image.open("assets/images/profile.jpg")
st.image(img, width=300)

# Or directly
st.image("assets/images/projects/screenshot.png", 
         caption="Project XY", 
         use_column_width=True)
```

## Tips

- Compress everything (TinyPNG etc.)
- No spaces in filenames
- Keep originals as backup
