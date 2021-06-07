from flask import  jsonify
import json
from src.strategies.engineoperation import EngineContext, EcoModeStrategy, DeepCleanModeStrategy
from src.statemachines.statemachine import Context
from multiprocessing import Process

class EngineController:




    def __init__(self):
        pass


    def obj_dict(self,obj):
        return obj.to_json()

    def run_task(self, currentcontext):

        currentcontext.do_operation()
        return 1

    def startEngine(self, enginemode):
        if (enginemode==1) :
            context = EngineContext(EcoModeStrategy())
            #self.context = context
            print("Mode Eco detected.")
        else:
            context = EngineContext(DeepCleanModeStrategy())
            #self.context=context
            print("Mode DeepClean detected.")
        p = Process(target=self.run_task,args=(context,))
        p.start()
        #p.join()
        #await context.do_operation()
        return jsonify({"Started":"Success"})

    def stopEngine(self):
        return jsonify({"Stopped": "Success"})

    def getCurrentState(self):
        state="Washing"
        return jsonify({"State": state})