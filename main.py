from flask import Flask,jsonify,request
app = Flask(__name__)
@app.route("/")  
def index():
    return "<html><head><title>Python Flask ile Restful api servisi</title></head><body><b>Kullanım şekilleri</b> <br>    oluşan url + / filmler 'i yeni sekmeye yaz' <br>url/filmler/Tur</body></html>"

filmler = [
    {
        'film_adi':'Harry Potter',
        'Yayin_yili':'2002',
        'Tur':'kurgu'
    },
    {
        'film_adi':'Avengers',
        'Yayin_yili':'2015',
        'Tur':'aksiyon'
    },
    {
        'film_adi':'Batman vs Superman',
        'Yayin_yili':'2016',
        'Tur':'aksiyon'
    }
]
@app.route('/filmler')
def get_filmler():
    json_data = jsonify({'filmler':filmler})
    return json_data
@app.route('/filmler/<string:Tur>')
def get_movie_by_genre(Tur):
    film_liste=[]
    for film in filmler:
        if Tur == film['Tur']:
            film_liste.append(
                {
                    'film_adi':film['film_adi'],
                    'Tur':film['Tur'],
                    'Yayin_yili':film['Yayin_yili']
                }
            )
    return jsonify({'filmler':film_liste})
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=81)
