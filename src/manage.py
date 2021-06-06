import os

from flask_script import Manager
from src import create_app
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO, emit, disconnect

#importing additional routes
from flask import Flask, render_template, request

from src.service.routes import engineroute

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.app_context().push()
socketio = SocketIO(app,cors_allowed_origins="*")
#CORS(app,resources={ r'/*': {'origins': '*'}}, supports_credentials=True)
# Set CORS options on app configuration
CORS(app, resources={ r'/*': {'origins': [
    'http://localhost:3000' # React
      # React
  ]}}, supports_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'
#Adding additional routes


app.add_url_rule('/api/engine', view_func=engineroute.startEngine,methods=['POST'])
app.add_url_rule('/api/engine', view_func=engineroute.stopEngine,methods=['PUT'])


#@app.after_request
#def after_request(response):
#  response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
#  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
#  response.headers.add('Access-Control-Allow-Credentials', 'true')
#  return response

manager = Manager(app)

@manager.command
def run():
    print('[INFO] Run server at http://localhost:5000')
    socketio.run(app=app,debug=True,host='0.0.0.0', port=5000,cors_allowed_origins="*")
    #app.run(debug=True, host='0.0.0.0')

#from app.main import create_app

#A default route here
@app.route('/')
def home():
   return "Washing Machine Simulator API!"

if __name__ == '__main__':
    print('[INFO] Starting server at http://localhost:5000')
    #app.run(debug=True, host='0.0.0.0',port=5000)
    socketio.run(app=app,debug=True, host='0.0.0.0', port=5000,cors_allowed_origins="*")

api_v2_cors_config = {
  "origins": [
    'http://localhost:3000'  # React
  # React
  ],
  "methods": ["OPTIONS", "GET", "POST"],
  "allow_headers": ["Authorization", "Content-Type"]
}


@socketio.on('connect')
#@cross_origin(**api_v2_cors_config)
def connect_web():
    print('[INFO] Web client connected: {}'.format(request.sid))
    emit('my response', {'data': 'Connected'})


@socketio.on('my event')
def test_message(message):
    emit('my response', {'data': message['data']})

@socketio.on('my broadcast event')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)


#@cross_origin(**api_v2_cors_config)
#@socketio.on('message')
#def handle_message(message): # Should it take an argument ?
#    print("Message recieved" + message)

@socketio.on('disconnect')
#@cross_origin(**api_v2_cors_config)
def disconnect_web():
    print('[INFO] Web client disconnected: {}'.format(request.sid))


if __name__ == '__main__':
    manager.run()