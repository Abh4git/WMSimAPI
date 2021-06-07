from __future__ import annotations
from abc import ABC, abstractmethod
import time
from src.commands.commands import Controller, StartInletPumpCommand, \
                TriggerDrumMotorCounterClockWiseCommand, OpenOutletValveCommand, CloseOutletValveCommand,\
                StopInletPumpCommand, TriggerDrumMotorClockWiseCommand, StartDryerCommand, StopDryerCommand


class Context:
    """
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the Context.
    """

    _state = None
    _controller =None
    _statename=None
    """
    A reference to the current state of the Context.
    """

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        """
        The Context allows changing the State object at runtime.
        """
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self



    """
    The Context delegates part of its behavior to the current State object.
    """

    def mainRequest(self):
        self._state.performMainAction()

    def subRequest(self):
        self._state.performSubAction()


class State(ABC):
    """
    The base State class declares methods that all Concrete State should
    implement and also provides a backreference to the Context object,
    associated with the State. This backreference can be used by States to
    transition the Context to another State.
    """

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def performMainAction(self) -> None:
        pass

    @abstractmethod
    def performSubAction(self) -> None:
        pass

    @property
    def statename(self):
        return self._statename

    @statename.setter
    def statename(self, statename) -> None:
        self._statename = statename


class WaterCollection(State):
    def performMainAction(self) :
        print("Water Collection ...")
        self.statename = "Water Collection"
        print("Water Collection completed, state change initiated.")
        self.context.transition_to(Washing())



    def performSubAction(self) -> None:
        print("Water Collection Subaction.")


class Washing(State):
    def performMainAction(self) -> None:
        self.statename="Washing"
        print("Washing ...")

    def performSubAction(self) -> None:
        print("Washing completed, initiating state change.")
        self.context.transition_to(Rinsing())


class Rinsing(State):
    def performMainAction(self) -> None:
        print("Rinsing ...")
        self.statename = "Rinsing"
        print("Rinsing completed, initiating state change.")
        self.context.transition_to(Draining())

    def performSubAction(self) -> None:
        print("Rinsing Subaction.")
class Draining(State):
    def performMainAction(self) -> None:
        print("Draining ...")


    def performSubAction(self) -> None:
        print("Draining completed, initiating state change.")
        self.context.transition_to(Drying())

class Drying(State):
    def performMainAction(self) -> None:
        self.statename = "Drying"
        print(" Drying ...")

    def performSubAction(self) -> None:
        print("Drying Completed.")

if __name__ == "__main__":
    # The client code.
    _stateInfo = "START"

    print (_stateInfo)
    context = Context(WaterCollection())

    controller = Controller()

    controller.setCommand(StartInletPumpCommand("Start Inlet Pump"))
    controller.executeCommand()
    time.sleep(5)  # 5 seconds
    controller.setCommand(StopInletPumpCommand("Stop Inlet Pump"))
    controller.executeCommand()
    context.mainRequest() #Washing
    controller.setCommand(TriggerDrumMotorClockWiseCommand("Drum Clockwise"))
    controller.executeCommand()
    time.sleep(5)  # 5 seconds
    controller.setCommand(TriggerDrumMotorCounterClockWiseCommand("Drum Counter Clockwise"))
    controller.executeCommand()
    context.subRequest()  #Rinse
    controller.setCommand(OpenOutletValveCommand("Open Outlet Valve"))
    controller.executeCommand()
    time.sleep(5)  # 5 seconds
    controller.setCommand(CloseOutletValveCommand("Close Outlet valve"))
    controller.executeCommand()
    #Water input
    controller.setCommand(StartInletPumpCommand("Start Inlet Pump"))
    controller.executeCommand()
    time.sleep(5)  # 5 seconds
    controller.setCommand(StopInletPumpCommand("Stop Inlet Pump"))
    controller.executeCommand()
    #do drum turning
    controller.setCommand(TriggerDrumMotorClockWiseCommand("Drum Clockwise"))
    controller.executeCommand()
    time.sleep(5)  # 5 seconds
    controller.setCommand(TriggerDrumMotorCounterClockWiseCommand("Drum Counter Clockwise"))
    controller.executeCommand()
    #Now drain the water
    context.mainRequest() #Draining
    controller.setCommand(OpenOutletValveCommand("Open Outlet valve"))
    controller.executeCommand()
    time.sleep(5)  # 5 seconds
    controller.setCommand(CloseOutletValveCommand("Close Outlet Valve"))
    controller.executeCommand()

    context.subRequest()#Drying
    controller.setCommand(StartDryerCommand("Start Dryer "))
    controller.executeCommand()
    time.sleep(5)  # 5 seconds
    controller.setCommand(StopDryerCommand("Stop Dryer"))
    controller.executeCommand()
    _stateInfo = "END"
    print (_stateInfo)