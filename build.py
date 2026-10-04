from jinja2 import Environment, FileSystemLoader
import json
import os
from datetime import datetime
import shutil

print("Running build.py...")

env = Environment(loader=FileSystemLoader("templates"))

with open("data/projects.json", encoding="utf-8") as f:
    projects = json.load(f)

with open("data/certifications.json", encoding="utf-8") as f:
    certifications = json.load(f)

with open("data/site_content.json", encoding="utf-8") as f:
    site = json.load(f)

common = {
    "projects": projects,
    "certifications": certifications,
    "site": site,
    "current_year": datetime.now().year,
}

os.makedirs("docs", exist_ok=True)

template = env.get_template("index.html")
with open("docs/index.html", "w", encoding="utf-8") as f:
    f.write(template.render(**common))
print("✅ Site built at /docs/index.html")

fabric_template = env.get_template("fabric.html")
with open("docs/fabric.html", "w", encoding="utf-8") as f:
    f.write(fabric_template.render(**common))
print("✅ Fabric page built at /docs/fabric.html")

static_src = "static"
static_dest = os.path.join("docs", "static")
if os.path.exists(static_dest):
    shutil.rmtree(static_dest)
shutil.copytree(static_src, static_dest)
print("✅ Copied static files to /docs")
