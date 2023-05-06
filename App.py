from flask import Flask, abort
from flask import request
import uuid

game_info = {}

app = Flask(__name__)

#Has to receive some game object
@app.route('/initGame', methods = ['POST'])
def create_game():

    username = request.get_json()['username']
    sessionid = uuid.uuid4()
    game_info[str(sessionid)] = [username]
    
    return {'sessionid': sessionid}, 201

@app.route('/addUser', methods = ['PUT'])
def addUsers():

    data = request.get_json()
    username = data['username']
    sessionid = str(data['sessionid'])

    if(sessionid not in game_info):
        abort(404, f'Game {sessionid} not found!")

    for uname in game_info[sessionid]:
        if(uname == username):
            abort(409, f'User {username} already exists in this game!")

    game_info[sessionid] = game_info[sessionid] + [username]
    return {'message': f'User {username} added with success!'}, 201

if __name__ == "__main__":
    app.run(debug=True)