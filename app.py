from flask import Flask, request, send_from_directory

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def load_static():
    return send_from_directory(app.static_folder, 'index.html')


# Ajouter des autres routes ici