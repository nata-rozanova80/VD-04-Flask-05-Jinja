from flask import Flask, render_template, request
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/blog')  # Исправлено: route должен быть одинарным слэшем
def blog():
    return render_template('blog.html')

@app.route('/contacts')  # Исправлено: route должен быть одинарным слэшем
def contacts():
    return render_template('contacts.html')


@app.route('/search')
def search():
    query = request.args.get('query')  # Получаем строку запроса из URL
    results = perform_search(query)  # Вызов функции для поиска
    return render_template('search_results.html', query=query, results=results)

def perform_search(query):
        # Получаем HTML-контент страницы
    html_content = render_template('index.html')  # Получаем HTML-контент страницы
    soup = BeautifulSoup(html_content, 'html.parser')

    # Извлекаем текст из определенных элементов
    search_elements = soup.find_all(['h3', 'p'])  # Ищем в заголовках h3 и параграфах p
    results = []

    # Проверяем каждый элемент на наличие запроса
    for element in search_elements:
        if query.lower() in element.get_text().lower():
            results.append(element.get_text())  # Добавляем текст элемента в результаты

        if not results:
            results.append('Ничего не найдено.')

        return results


if __name__ == '__main__':  # Исправлено: __name__ и '__main__' вместо name и main
    app.run(debug=True)
