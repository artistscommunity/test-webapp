from flask import Flask
import requests


app = Flask(__name__)

@app.route('/')
def home():
  return 'works!'
  
@app.route('/test')
def test():
  r = requests.get('https://ewvdsggwrhwr.herokuapp.com/')
  return 'Server responded with: ' + r.text
  
if __name__ == '__main__':
  app.run()
