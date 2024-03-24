import json

def load_configuration():
    with open('./config/config.json','r') as tokenfile:
        global Token, Server_id, message
        tokenl = json.load(tokenfile)
        Token = tokenl['token']
        Server_id = tokenl['server_id']
        message = tokenl['raid_message']

load_configuration()

if __name__ == '__main__':
    print("This module shouldn't be open alone, please open the main app.")
