from flask import Flask, render_template_string

app = Flask(__name__)

# ==========================================
# НАСТРОЙКА ТЕКСТА: Меняй текст в кавычках
# ==========================================
GREETING_TITLE = "С Днем Рождения, Папа!"
GREETING_MESSAGE = "Дорогой папа, поздравляю тебя с днем рождения! Желаю тебе крепкого здоровья, бесконечной энергии и чтобы каждый день приносил только радость. Спасибо тебе за твою поддержку, мудрость и за то, что ты всегда рядом."
SENDER_NAME = "Твой сын"
# ==========================================

# Весь HTML и CSS код теперь хранится прямо здесь
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #e0e5ec;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            padding: 20px;
            box-sizing: border-box;
        }
        .card {
            background: white;
            padding: 50px 40px;
            border-radius: 20px;
            box-shadow: 10px 10px 20px #a3b1c6, -10px -10px 20px #ffffff;
            max-width: 600px;
            text-align: center;
        }
        h1 {
            color: #2c3e50;
            margin-top: 0;
            font-size: 2.2em;
        }
        p.message {
            color: #34495e;
            line-height: 1.8;
            font-size: 1.2em;
            margin: 25px 0;
        }
        p.sender {
            margin-top: 30px;
            font-style: italic;
            font-weight: bold;
            color: #7f8c8d;
            font-size: 1.1em;
            text-align: right;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>{{ title }}</h1>
        <p class="message">{{ message }}</p>
        <p class="sender">— {{ sender }}</p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    # Рендерим HTML-строку и передаем в нее наши переменные
    return render_template_string(HTML_TEMPLATE, 
                                  title=GREETING_TITLE, 
                                  message=GREETING_MESSAGE, 
                                  sender=SENDER_NAME)

if __name__ == '__main__':
    app.run(debug=True)

