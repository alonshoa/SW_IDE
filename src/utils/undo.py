class Undo:
    def __init__(self):
        self.states = []

    def addState(self, state):
        self.states.append(state)

    def getState(self):
        return self.states.pop()