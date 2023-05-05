from flask import Flask

app = Flask(__name__)

#Has to receive some game object
@app.route('/createGame')
def create_game(game):
    #Deserialize into a Game object
    return 'Creates game!'

@app.route('/addUsers')
def finish_game(sessionid, users):
    #Deserialize
    return 'Add users to a game!'

if __name__ == "__main__":
    app.run(debug=True)