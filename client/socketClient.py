import socketio

sio = socketio.Client()
sio.connect("http://localhost:5000/")
print('my sid is', sio.sid)


@sio.event
def message(data):
    print('I received a message!')
    print(data)


@sio.event
def connect():
    print("I'm connected!")


@sio.event
def disconnect():
    print("I'm disconnected!")