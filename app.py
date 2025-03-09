from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

# Dummy Data
projects = [
    {"name": "Text-to-Morse-Code Converter", "description": "A GUI-based Morse Code converter.", "link": "#"},
    {"name": "Inventory Management System", "description": "Open-source inventory tracking tool.", "link": "#"},
    {"name": "Cybersecurity Tool", "description": "A custom Python script for security analysis.", "link": "#"}
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)