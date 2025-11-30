from flask import Flask, render_template

app = Flask(__name__)

# Liste des cours pour la page d'accueil
cours_list = [
    {
        'titre': 'Démarches et enjeux de la géopolitique',
        'description': 'Introduction aux concepts fondamentaux de la géopolitique : relations entre pouvoir, espace et territoire, histoire de la discipline, méthodologies d\'analyse.',
        'url': '/cours/seance1'
    },
    {
        'titre': 'L\'État-nation, un cadre politique territorial indépassable ?',
        'description': 'Définitions et légitimation de l\'État, formes et caractéristiques étatiques, émergence de l\'État-nation, rapports au territoire.',
        'url': '/cours/seance2'
    },
    {
        'titre': 'Les conflits dans le monde contemporain',
        'description': 'Transformations des conflits, typologie des guerres, nouvelles échelles, crise de l\'État, émergence de nouveaux acteurs.',
        'url': '/cours/seance3'
    },
    {
        'titre': 'Quelles frontières pour l\'Europe ?',
        'description': 'Limites géographiques de l\'Europe, construction européenne, élargissements successifs, instruments IPA et PEV, défis contemporains.',
        'url': '/cours/seance4'
    },
    # ... autres cours
]
@app.route('/')
def index():
    return render_template('index.html', cours=cours_list)

@app.route('/cours/seance1')
def cours_seance1():
    return render_template('cours_seance1.html')

@app.route('/cours/seance2')
def cours_seance2():
    return render_template('cours_seance2.html')
@app.route('/cours/seance4')
def cours_seance4():
    return render_template('cours_seance4.html')
if __name__ == '__main__':
    app.run(debug=True)