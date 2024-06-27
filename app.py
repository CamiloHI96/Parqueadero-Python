from flask import Flask, render_template

app = Flask(__name__)

# Ruta de inicio
@app.route('/')
def home():
    return render_template('index.html')

# Ruta de inicio
@app.route('/index.html')
def inicio():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)