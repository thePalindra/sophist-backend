from flask import Flask
import requests

#the user with id john creates a game
init_game_data = {'username': 'John'}
response = requests.post('http://localhost:5000/initGame', json=init_game_data)
print(response.json())

sessionid = response.json()['sessionid']

#several individuals are added to the party 
for name in ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank']:
    other_users = {'sessionid':sessionid, 'username': name}
    response = requests.put('http://localhost:5000/addUser', json = other_users)
    print(response.json())