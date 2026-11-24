from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    projects = [
        {"number": "01", "name": "Me2Sell", "type": "Business management · Marketplace", "description": "A sales and inventory platform that helps business owners manage stock, track sales, staff and showcase products.", "stack": ["React", "Firebase", "Tailwind CSS"], "link": "https://me2sell.com"},
        {"number": "02", "name": "FreeInvoice247", "type": "Productivity · Web tool", "description": "A simple invoice and receipt generator designed to help freelancers and businesses create professional documents.", "stack": ["React", "Vite", "Firebase"], "link": "https://freeinvoice247.web.app"},
        {"number": "03", "name": "100 Days of Python", "type": "Learning · 100-day challenge", "description": "A hands-on journey building practical Python projects—from automation and APIs to Flask applications.", "stack": ["Python", "Flask", "APIs"], "link": "https://github.com/ENYO360"},
    {"number": "04", "name": "Developer Portfolio", "type": "Personal · Flask", "description": "A vibrant portfolio that brings my work, learning journey and developer story together in one place.", "stack": ["Python", "Flask", "HTML/CSS"], "link": "https://github.com/ENYO360"},
    ]
    journey = [
        ("2026", "Building and shipping", "Developing real-world web and mobile products, including Me2Sell and useful business tools."),
        ("100 Days", "Python challenge", "Practising Python daily through projects covering automation, data, APIs and Flask web apps."),
        ("Before", "Frontend to full-stack", "Growing from responsive interfaces with React into backend development, databases and APIs."),
    ]
    return render_template("index.html", projects=projects, journey=journey,
                          contact_email="hello@example.com",
                          current_year=datetime.now().year)

if __name__ == "__main__":
    app.run(debug=True)
