from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # Получаем текущую дату и время
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return render_template_string('''
         <html>
             <head>
                 <title>Текущая дата и время</title>
             </head>
             <body>
                 <h1>Текущая дата и время:</h1>
                 <p>{{ current_time }}</p>
             </body>
         </html>
     ''', current_time=current_time)


if __name__ == '__main__':
    app.run(debug=True)