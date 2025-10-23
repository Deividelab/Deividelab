from __future__ import annotations


import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional


GITHUB_USERNAME_RE = re.compile(r"^[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,38}[a-zA-Z0-9])?$")


DEFAULT_STACK: Dict[str, List[Dict[str, str]]] = {
"Linguagens": [
{"name": "Python", "color": "3776AB", "logo": "python"},
{"name": "JavaScript", "color": "F7DF1E", "logo": "javascript", "logoColor": "black"},
{"name": "TypeScript", "color": "3178C6", "logo": "typescript"},
{"name": "HTML5", "color": "E34F26", "logo": "html5"},
{"name": "CSS3", "color": "1572B6", "logo": "css3"},
],
"Frameworks & Bibliotecas": [
{"name": "Django", "color": "092E20", "logo": "django"},
{"name": "Flask", "color": "000000", "logo": "flask"},
{"name": "FastAPI", "color": "009688", "logo": "fastapi"},
{"name": "React", "color": "20232A", "logo": "react", "logoColor": "61DAFB"},
{"name": "Node.js", "color": "339933", "logo": "node.js"},
],
"DevOps & Ferramentas": [
{"name": "Docker", "color": "2496ED", "logo": "docker"},
{"name": "GitHub Actions", "color": "2088FF", "logo": "github-actions"},
{"name": "Git", "color": "F05033", "logo": "git"},
{"name": "VSCode", "color": "0078D4", "logo": "visual-studio-code"},
{"name": "Linux", "color": "FCC624", "logo": "linux", "logoColor": "black"},
],
"Cloud & Bancos de Dados": [
{"name": "AWS", "color": "232F3E", "logo": "amazon-aws"},
{"name": "Google Cloud", "color": "4285F4", "logo": "google-cloud"},
{"name": "PostgreSQL", "color": "336791", "logo": "postgresql"},
{"name": "MongoDB", "color": "47A248", "logo": "mongodb"},
{"name": "SQLite", "color": "07405E", "logo": "sqlite"},
],
"IA & Data": [
{"name": "TensorFlow", "color": "FF6F00", "logo": "tensorflow"},
{"name": "PyTorch", "color": "EE4C2C", "logo": "pytorch"},
{"name": "Pandas", "color": "150458", "logo": "pandas"},
{"name": "NumPy", "color": "013243", "logo": "numpy"},
],
}




def build_badge(name: str, color: str, logo: str, logo_color: str = "white") -> str:
"""Retorna a URL de um badge do shields.io formatado para usar em markdown."""
label = name.replace(" ", "%20")
logo = logo.replace(" ", "%20")
return f"https://img.shields.io/badge/{label}-{color}?style=for-the-badge&logo={logo}&logoColor={logo_color}"




def validate_github_username(username: str) -> bool:
return bool(GITHUB_USERNAME_RE.match(username))




def load_stack_from_json(path: Path) -> Dict[str, List[Dict[str, str]]]:
try:
with path.open("r", encoding="utf-8") as f:
data = json.load(f)
# Expect structure similar to DEFAULT_STACK
if not isinstance(data, dict):
raise ValueError("Arquivo JSON deve conter um objeto de categorias.")
return data
except Exception as e:
