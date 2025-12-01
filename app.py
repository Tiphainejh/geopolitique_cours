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
    {
        'titre': 'Les aires culturelles aujourd\'hui',
        'description': 'Étude critique des aires culturelles : origines académiques, théorie du choc des civilisations, globalisation et pertinence contemporaine.',
        'url': '/cours/seance5'
    },
    {
        'titre': 'L\'Inde : géographie, démographie et puissance émergente',
        'description': 'Analyse complète de l\'Inde : territoire immense, diversité exceptionnelle, économie en croissance et positionnement géopolitique stratégique.',
        'url': '/cours/seance6'
    },
    {
        'titre': 'L\'Amérique latine : influences américaine et européenne',
        'description': 'Histoire complète de l\'influence nord-américaine (1776-présent) et européenne (1980-présent) sur l\'Amérique latine : expansionnisme, néolibéralisme, Mercosur, néopopulisme et géopolitique contemporaine.',
        'url': '/cours/seance7'
    },
    {
        'titre': 'Le Moyen-Orient : Géopolitique et Conflits',
        'description': 'Analyse approfondie des dynamiques géopolitiques du Moyen-Orient, incluant les conflits historiques et contemporains, les enjeux énergétiques, et les influences internationales dans la région.',
        'url': '/cours/seance8'
    },
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

@app.route('/cours/seance3')
def cours_seance3():
    return render_template('cours_seance3.html')

@app.route('/cours/seance4')
def cours_seance4():
    return render_template('cours_seance4.html')

@app.route('/cours/seance5')
def cours_seance5():
    return render_template('cours_seance5.html')

@app.route('/cours/seance6')
def cours_seance6():
    return render_template('cours_seance6.html')

@app.route('/cours/seance7')
def cours_seance7():
    return render_template('cours_seance7.html')

@app.route('/cours/seance8')
def cours_seance8():
    return render_template('cours_seance8.html')
if __name__ == '__main__':
    app.run(debug=True)