from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):
    """
    The Command interface declares a method for executing a command.
    """

    @abstractmethod
    def execute(self) -> None:
        pass

    @property
    def result(self):
        return self._result


class StartInletPumpCommand(Command):
    """
    Some commands can implement simple operations on their own.
    """

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"StartInletPumpCommand: Starting Inlet Pump"
              f"({self._payload})")
        self._result=1 # 1 - Success

class StopInletPumpCommand(Command):
    """
    Some commands can implement simple operations on their own.
    """

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"StopInletPumpCommand: Stopping Inlet Pump"
              f"({self._payload})")
        self._result = 1


class OpenOutletValveCommand(Command):
    """
    Some commands can implement simple operations on their own.
    """

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"StartOutletPumpCommand: Starting Outlet Pump"
              f"({self._payload})")
        self._result = 1

class CloseOutletValveCommand(Command):
    """
    Some commands can implement simple operations on their own.
    """

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"StopOutletPumpCommand: Stopping Outlet Pump"
              f"({self._payload})")
        self._result = 1
class TriggerDrumMotorClockWiseCommand(Command):
    """
    Some commands can implement simple operations on their own.
    """

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"TriggerDrumMotorClockWiseCommand: Turning Drum Moter Clockwise"
              f"({self._payload})")
        self._result = 1
class TriggerDrumMotorCounterClockWiseCommand(Command):
    """
    Some commands can implement simple operations on their own.
    """

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"TriggerDrumMotorCounterClockWiseCommand: Turning Drum Moter Counter Clockwise"
              f"({self._payload})")
        self._result = 1

class StartDryerCommand(Command):
    """
    Some commands can implement simple operations on their own.
    """

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"StartDryerCommand: Starting Dryer"
              f"({self._payload})")
        self._result = 1

class StopDryerCommand(Command):
    """
    Some commands can implement simple operations on their own.
    """

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"StopDryerCommand: Stopping Dryer"
              f"({self._payload})")
        self._result = 1


class Controller:
    """
    The Invoker is associated with one or several commands. It sends a request
    to the command.
    """

    _currentCommand = None

    """
    Initialize commands.
    """

    def setCommand(self, command: Command):
        self._currentCommand = command


    def executeCommand(self) -> None:
        """
        The Invoker does not depend on concrete command or receiver classes. The
        Invoker passes a request to a receiver indirectly, by executing a
        command.
        """
        if isinstance(self._currentCommand, Command):
            #print("Execute Command sequence")
            self._currentCommand.execute()





if __name__ == "__main__":
    """
    The client code can parameterize an invoker with any commands.
    """

    contoller = Controller()
    contoller.setCommand(StartInletPumpCommand("Collecting Water!"))
    contoller.executeCommand()
