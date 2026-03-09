"""Build script that renders the Flask/Jinja2 template into static HTML."""
import json
import os
import shutil

from jinja2 import Environment, FileSystemLoader

# Load meme data
with open("memes.json", encoding="utf-8") as f:
    memes = json.load(f)

# Render template
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("index.html")
html = template.render(memes=memes)

# Create output directory
os.makedirs("_site", exist_ok=True)

# Write rendered HTML
with open("_site/index.html", "w", encoding="utf-8") as f:
    f.write(html)

# Copy static assets
if os.path.exists("_site/static"):
    shutil.rmtree("_site/static")
shutil.copytree("static", "_site/static")

print("Build complete: _site/")
