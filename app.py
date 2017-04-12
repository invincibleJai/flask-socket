from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)


@socketio.on('echo')
def handle_my_custom_namespace_event(jsn):
    print('received json: ' + str(jsn))
    return {'msg': jsn}

if __name__ == "__main__":
    socketio.run(app, port=5012)
