from flask import Flask

app = Flask(__name__)

@app.route('/createGame')
def create_game():
    return 'creates game!'

@app.route('/finishGame')
def finish_game():
    return 'finish game!'

@app.route('/')
def f():
    return 'game!'

if __name__ == "__main__":
    app.run(debug=True)