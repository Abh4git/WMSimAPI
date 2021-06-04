#All Routes are defined here
from flask_cors import CORS, cross_origin
from src.service.controllers.enginecontroller import EngineController
from flask import request


#Test route without any connections
def test():
    return "{testroutesuccess:'Test Route Success!'}"

api_v2_cors_config = {
  "origins": [
    'http://localhost:3000' , # React
  # React
  ],
  "methods": ["OPTIONS", "GET", "POST"],
  "allow_headers": ["Authorization", "Content-Type"]
}


@cross_origin(**api_v2_cors_config)
def startEngine():
    enginecontroller = EngineController()
    print(request.is_json)
    requestInfo =request.get_json()
    print(requestInfo)
    response=enginecontroller.startEngine(requestInfo['enginemode'])
    return response

@cross_origin(**api_v2_cors_config)
def stopEngine():
    enginecontroller = EngineController()
    print(request.is_json)
    requestInfo =request.get_json()
    print(requestInfo)
    response=enginecontroller.stopEngine()
    return response
