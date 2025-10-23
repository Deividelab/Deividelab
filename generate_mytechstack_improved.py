name: Generate README

on:
  push:
    branches: [ main, master ]
  workflow_dispatch:

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Run generator
        run: |
          python generate_mytechstack_improved.py --username seu_usuario -o README.md

      - name: Commit and push changes
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add README.md
          git commit -m "chore: atualizar README gerado automaticamente" || echo "Sem alterações"
          git push
