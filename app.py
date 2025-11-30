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
        'titre': 'Définitions des Relations Internationales',
        'description': 'Concepts clés et approches théoriques des relations internationales.',
        'url': '/cours/definitions-ri'
    },
    {
        'titre': 'Économie du XXe siècle',
        'description': 'Évolution économique mondiale et transformations du système économique international.',
        'url': '/cours/economie-20e'
    },
    {
        'titre': 'Diplomatie culturelle',
        'description': 'Soft power et influence culturelle dans les relations internationales.',
        'url': '/cours/diplomatie-culturelle'
    },
    {
        'titre': 'Migrations internationales',
        'description': 'Flux migratoires, enjeux démographiques et géopolitiques des migrations.',
        'url': '/cours/migrations'
    },
    {
        'titre': 'Afrique et colonisation',
        'description': 'Histoire coloniale, décolonisation et enjeux contemporains du continent africain.',
        'url': '/cours/afrique-colonisation'
    },
    {
        'titre': 'L\'ONU et l\'intégration régionale',
        'description': 'Organisations internationales, système onusien et processus d\'intégration régionale.',
        'url': '/cours/onu-integration'
    },
    {
        'titre': 'Organisations internationales',
        'description': 'Acteurs multilatéraux et leur rôle dans la gouvernance mondiale.',
        'url': '/cours/organisations-internationales'
    },
    {
        'titre': 'Qu\'est-ce que l\'Europe ?',
        'description': 'Construction européenne, identité européenne et défis de l\'intégration.',
        'url': '/cours/quest-ce-que-europe'
    }
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

if __name__ == '__main__':
    app.run(debug=True)