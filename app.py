from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    day_of_week = ['sun', 'mon', 'tue', 'wed', 'thr', 'fri', 'sat']
    days_in_month = 31
    return render_template('index.html', day_of_week=day_of_week, days_in_month=days_in_month)

@app.route('/blog')  # Исправлено: route должен быть одинарным слэшем
def blog():
    return render_template('blog.html')

@app.route('/contacts')  # Исправлено: route должен быть одинарным слэшем
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':  # Исправлено: __name__ и '__main__' вместо name и main
    app.run(debug=True)
