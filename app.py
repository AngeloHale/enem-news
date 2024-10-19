from flask import Flask, render_template
import requests


app = Flask(__name__)

# Chave da API NewsAPI
API_KEY = '7e2295d2472443538c69312b6131c529'

# Função para buscar as notícias de uma categoria específica
def fetch_news(category):
    api_url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
    response = requests.get(api_url)
    news_data = response.json()
    return news_data.get('articles', [])

@app.route('/')
@app.route('/<category>')
def home(category='general'):
    # Busca as notícias da categoria selecionada
    articles = fetch_news(category)
    return render_template('index.html', articles=articles, category=category)

if __name__ == '__main__':
    app.run(debug=True)
