# Day 83 — Flask Developer Portfolio (Python only)

A responsive developer portfolio built with Python Flask, Jinja templates, HTML and CSS. This version contains **no JavaScript**.

## Run locally

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS / Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## Personalize

- Replace `static/images/profile-placeholder.svg` with your own portrait (keep the filename or update the template).
- Change the contact email in `app.py`.
- Update project names, descriptions, stacks and links in `app.py`.

## No JavaScript

The mobile navigation uses a native HTML checkbox and CSS. Entrance effects, smooth scrolling and responsive behavior are CSS-only. The copyright year is generated on the Flask server with Python's `datetime`. No JavaScript file or script tag is included.
