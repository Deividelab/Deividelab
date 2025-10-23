def generate_readme(username):
    readme_content = f"""\
# 👋 Olá, eu sou {username}!

Sou um desenvolvedor apaixonado por tecnologia e aprendizado constante. 🚀  

## 🧠 My Tech Stack

### 💻 Linguagens
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

---

✨ _Gerado automaticamente com Python_
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    print("✅ README.md gerado com sucesso!")


if __name__ == "__main__":
    user = input("Digite seu nome de usuário do GitHub: ").strip()
    generate_readme(user)
