from __future__ import annotations
from abc import ABC, abstractmethod

class Context:
    """
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the Context.
    """

    _state = None
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


class WaterCollection(State):
    def performMainAction(self) -> None:
        print("Performing Water Collection Sequence")
        print("Checking Water level reached?")
        print("Water collection completed, initiating state change.")
        self.context.transition_to(Washing())

    def performSubAction(self) -> None:
        print("Water Collection SubAction sequence.")


class Washing(State):
    def performMainAction(self) -> None:
        print("Performing Washing Sequence")
        print("Washing completed, initiating state change.")
        self.context.transition_to(Washing())

    def performSubAction(self) -> None:
        print("Water Collection SubAction sequence.")


class Rinsing(State):
    def performMainAction(self) -> None:
        print("Performing Rinsing Sequence")
        print("Rinsing completed, initiating state change.")
        self.context.transition_to(Washing())

    def performSubAction(self) -> None:
        print("Rinsing SubAction sequence.")

class Draining(State):
    def performMainAction(self) -> None:
        print("Performing Draining Sequence")
        print("Draining completed, initiating state change.")
        self.context.transition_to(Washing())

    def performSubAction(self) -> None:
        print("Draining  SubAction sequence.")

class Drying(State):
    def performMainAction(self) -> None:
        print("Performing Drying Sequence")
        print("Washing completed, initiating state change.")

    def performSubAction(self) -> None:
        print("Drying SubAction sequence.")

if __name__ == "__main__":
    # The client code.

    context = Context(WaterCollection())
    context.mainRequest()
    context.subRequest()