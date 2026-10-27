import os
from flask import Flask
арр = Flask(name)
@app.route('/')
def hello() :
  secret = os.environ.get('MY_SECRET_MESSAGE', 'не задана')
  return f"Приложение работает! Секрет: {secret}"
if name == 'main':
  port = int(os.environ.get('PORT', 5000))
  app.run(host = '0.0.0.0', port = port)
