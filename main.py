from flask import Flask, render_template, jsonify

from mongodb import mongodb_stations_infos, mongodb_stations_bikes

app = Flask(__name__)


@app.route('/')
def main():
    return "<h1>ca marche !</h1>regarde la doc mnt. <b>#y a pas de doc.</b></br></br><h1>Documentation</h1>Infos sur les stations : <a href='./api/stations_infos'>/api/stations_infos</a></br>Vélo dispo dans chaque stations : <a href='./api/stations_bikes'>/api/stations_bikes</a>"


@app.route('/api/stations_infos')
def get_stations_info():
    data = mongodb_stations_infos()
    return jsonify(data)


@app.route('/api/stations_bikes')
def get_stations_bikes():
    data = mongodb_stations_bikes()
    print(data)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8888)