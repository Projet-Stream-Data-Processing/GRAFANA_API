from flask import Flask, render_template, jsonify

from mongodb import get_stations_infos, get_stations_bikes

app = Flask(__name__)




@app.route('/')
def main():
    return "ca marche ! regarde la doc mnt."


@app.route('/api/stations_info')
def get_stations_info():
    data = get_stations_infos()
    return jsonify({"lignes":data})


@app.route('/api/stations_bikes')
def get_stations_bikes():
    data = get_stations_bikes()
    return "test"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8888)