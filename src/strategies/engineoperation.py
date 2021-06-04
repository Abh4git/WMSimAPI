from __future__ import annotations
from abc import ABC, abstractmethod
from src.statemachines.statemachine import WaterCollection, Context

import time
from src.commands.commands import Controller, StartInletPumpCommand, \
                TriggerDrumMotorCounterClockWiseCommand, OpenOutletValveCommand, CloseOutletValveCommand,\
                StopInletPumpCommand, TriggerDrumMotorClockWiseCommand, StartDryerCommand, StopDryerCommand


class EngineContext():
    """
    The Context defines the interface of interest to clients.
    """

    def __init__(self, strategy: Strategy) -> None:
        """
        Usually, the Context accepts a strategy through the constructor, but
        also provides a setter to change it at runtime.
        """

        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """

        self._strategy = strategy

    def do_operation(self) -> None:
        """
        The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        """

        # ...

        print("Context: EngineContext")
        result = self._strategy.do_algorithm()
        print(",".join(result))

        # ...


class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def do_algorithm(self):
        pass


"""
Concrete Strategies implement the algorithm while following the base Strategy
interface. The interface makes them interchangeable in the Context.
"""


class EcoModeStrategy(Strategy):
    def do_algorithm(self) :
        _stateInfo = "START"

        print(_stateInfo)
        context = Context(WaterCollection())

        controller = Controller()

        controller.setCommand(StartInletPumpCommand("Start Inlet Pump"))
        controller.executeCommand()
        time.sleep(5)  # 5 seconds
        controller.setCommand(StopInletPumpCommand("Stop Inlet Pump"))
        controller.executeCommand()
        context.mainRequest()  # Washing
        controller.setCommand(TriggerDrumMotorClockWiseCommand("Drum Clockwise"))
        controller.executeCommand()
        time.sleep(5)  # 5 seconds
        controller.setCommand(TriggerDrumMotorCounterClockWiseCommand("Drum Counter Clockwise"))
        controller.executeCommand()
        context.subRequest()  # Rinse
        controller.setCommand(OpenOutletValveCommand("Open Outlet Valve"))
        controller.executeCommand()
        time.sleep(5)  # 5 seconds
        controller.setCommand(CloseOutletValveCommand("Close Outlet valve"))
        controller.executeCommand()
        # Water input
        controller.setCommand(StartInletPumpCommand("Start Inlet Pump"))
        controller.executeCommand()
        time.sleep(5)  # 5 seconds
        controller.setCommand(StopInletPumpCommand("Stop Inlet Pump"))
        controller.executeCommand()
        # do drum turning
        controller.setCommand(TriggerDrumMotorClockWiseCommand("Drum Clockwise"))
        controller.executeCommand()
        time.sleep(5)  # 5 seconds
        controller.setCommand(TriggerDrumMotorCounterClockWiseCommand("Drum Counter Clockwise"))
        controller.executeCommand()
        # Now drain the water
        context.mainRequest()  # Draining
        controller.setCommand(OpenOutletValveCommand("Open Outlet valve"))
        controller.executeCommand()
        time.sleep(5)  # 5 seconds
        controller.setCommand(CloseOutletValveCommand("Close Outlet Valve"))
        controller.executeCommand()

        context.subRequest()  # Drying
        controller.setCommand(StartDryerCommand("Start Dryer "))
        controller.executeCommand()
        time.sleep(5)  # 5 seconds
        controller.setCommand(StopDryerCommand("Stop Dryer"))
        controller.executeCommand()
        _stateInfo = "END"
        print(_stateInfo)
        return "Ecomode run successfully"


class DeepCleanModeStrategy(Strategy):
    def do_algorithm(self) :
        _stateInfo = "START"
        print(_stateInfo)
        context = Context(WaterCollection())

        controller = Controller()

        controller.setCommand(StartInletPumpCommand("Start Inlet Pump"))
        controller.executeCommand()
        time.sleep(5)  # 5 seconds
        controller.setCommand(StopInletPumpCommand("Stop Inlet Pump"))
        controller.executeCommand()
        context.mainRequest()  # Washing
        controller.setCommand(TriggerDrumMotorClockWiseCommand("Drum Clockwise"))
        controller.executeCommand()
        time.sleep(5)  # 5 seconds
        controller.setCommand(TriggerDrumMotorCounterClockWiseCommand("Drum Counter Clockwise"))
        controller.executeCommand()
        context.subRequest()  # Rinse
        controller.setCommand(OpenOutletValveCommand("Open Outlet Valve"))
        controller.executeCommand()
        time.sleep(5)  # 5 seconds
        controller.setCommand(CloseOutletValveCommand("Close Outlet valve"))
        controller.executeCommand()
        # Water input
        controller.setCommand(StartInletPumpCommand("Start Inlet Pump"))
        controller.executeCommand()
        time.sleep(5)  # 5 seconds
        controller.setCommand(StopInletPumpCommand("Stop Inlet Pump"))
        controller.executeCommand()
        # do drum turning
        controller.setCommand(TriggerDrumMotorClockWiseCommand("Drum Clockwise"))
        controller.executeCommand()
        time.sleep(5)  # 5 seconds
        controller.setCommand(TriggerDrumMotorCounterClockWiseCommand("Drum Counter Clockwise"))
        controller.executeCommand()
        # Now drain the water
        context.mainRequest()  # Draining
        controller.setCommand(OpenOutletValveCommand("Open Outlet valve"))
        controller.executeCommand()
        time.sleep(5)  # 5 seconds
        controller.setCommand(CloseOutletValveCommand("Close Outlet Valve"))
        controller.executeCommand()

        context.subRequest()  # Drying
        controller.setCommand(StartDryerCommand("Start Dryer "))
        controller.executeCommand()
        time.sleep(5)  # 5 seconds
        controller.setCommand(StopDryerCommand("Stop Dryer"))
        controller.executeCommand()
        _stateInfo = "END"
        print(_stateInfo)

        return "Deep Clean Mode run successfully"


if __name__ == "__main__":
    # The client code picks a concrete strategy and passes it to the context.
    # The client should be aware of the differences between strategies in order
    # to make the right choice.

    context = EngineContext(EcoModeStrategy())
    print("Client: Strategy is set to Eco .")
    context.do_operation()
    print()

    print("Client: Strategy is set to Deep Clean.")
    context.strategy = DeepCleanModeStrategy()
    context.do_operation()
