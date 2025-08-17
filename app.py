from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {"name": "Text-to-Morse-Code Converter", "description": "A GUI-based Morse Code converter.", "link": "#"},
    {"name": "Inventory Management System", "description": "Open-source inventory tracking tool.", "link": "#"},
    {"name": "Cybersecurity Tool", "description": "Tool for scanning vulnerabilities.", "link": "#"}
]

@app.route('/')
def home():
    return render_template('home.html', projects=projects)

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/skills')
def skills_page():
    return render_template('skills.html')

@app.route('/projects')
def projects_page():
    return render_template('projects.html', projects=projects)

@app.route('/certifications')
def certifications_page():
    return render_template('certifications.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)