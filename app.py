from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/weather')
def weather():
    return render_template('weather.html')

@app.route('/health')
def health():
    return render_template('health.html')

@app.route('/consultation')
def consultation():
    return render_template('consultation.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)