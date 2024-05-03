"""
Purpose:
Sandbox playground for FSM (finite state machine) implementations
in python.

Instructions:
TBD
"""

from enum import Enum, auto
from typing import Callable
from typing import TypeVar

# TypeVar transition: Callable[[InputStates], Tuple[MovingStates, List[SideEffects]]]


"""
DRAFT TWO: How can we leverage some metaprogramming? 
or decorators?
"""

class States(Enum):
    A = auto()
    B = auto()
    C = auto()

class Transition(Enum):
    T1 = auto()
    T2 = auto()

class StateMachine():
    def __init__(self):
        self.transitions : dict = {}
        self.state: States = States.A

    def add_transition(self, transition: Transition, before: States, after: States) -> None:
        self.transitions[before] = {transition: after}
        print(self.transitions)
        return
    
    def execute(self, transition: Transition) -> States:
        if (new_state := self.transitions.get(self.state, {}).get(transition)):
            self.state =  new_state
            return
        
        print(f"Cannot transition from {self.state} for transition {transition}")


def main2():
    mach = StateMachine()
    mach.add_transition(Transition.T1, States.A, States.B)
    mach.add_transition(Transition.T2, States.B, States.C)
    mach.add_transition(Transition.T2, States.C, States.A)


    print(mach.state)
    mach.execute(Transition.T1)
    print(mach.state)
    mach.execute(Transition.T2)
    print(mach.state)
    mach.execute(Transition.T2)
    print(mach.state)
    mach.execute(Transition.T2)
    print(mach.state)







"""

DRAFT ONE: there are multiple enums with classes. they can use dictionaries
to attempt to draw out what is going on.
"""
# STANDING: {RIGHT_INPUT: WALKING}

class InputStates(Enum):
    UP_INPUT = auto()
    UP_RELEASE = auto()
    DOWN_INPUT = auto()
    DOWN_RELEASE = auto()
    RIGHT_INPUT = auto()
    RIGHT_RELEASE = auto()

class MovingStates(Enum):
    STANDING = auto()
    WALKING = auto()
    JUMPING = auto()
    DUCKING = auto()
    DIVING = auto()


class STANDING_STATE():
    def __init__(self):
        pass

    def Transition(self, input: InputStates):
        if (input == InputStates.RIGHT_INPUT):
            return MovingStates.WALKING
    

class Character():
    def __init__():
        self._moving: MovingStates


def main1():
    pass
    # ms = MovingStates
    # in = InputStates

    # FSM = {
    #     STANDING: { RIGHT_INPUT : WALKING # side effect
    #     }
    # }

    # if input in FSM[state]:
    #     return FSM[state].get('input', state)


"""
IDEAS

states from yaml?

"""

if __name__ == "__main__":
    main2()