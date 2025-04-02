from jinja2 import Environment, FileSystemLoader
import json
import os

print("Running build.py...")

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader("templates"))

# Load data
with open("data/projects.json", encoding="utf-8") as f:
    projects = json.load(f)

with open("data/certifications.json", encoding="utf-8") as f:
    certifications = json.load(f)

# Render the index template
template = env.get_template("index.html")
rendered_html = template.render(
    projects=projects,
    certifications=certifications
)

# Write to output file
os.makedirs("output", exist_ok=True)
with open("output/index.html", "w", encoding="utf-8") as f:
    f.write(rendered_html)

print("✅ Site built at /output/index.html")

import shutil

# Copy static files (e.g. images, css) into output/
static_src = "static"
static_dest = os.path.join("output", "static")

# Remove existing static folder if it exists
if os.path.exists(static_dest):
    shutil.rmtree(static_dest)

# Copy again
shutil.copytree(static_src, static_dest)
print("✅ Copied static files to /output")
