import sys

class Memento:
    def __init__(self, state):
        self.state = state

    def getState(self):
        return self.state

class Caretaker:
    def __init__(self):
        self.mementoList = []

    def add(self, state):
        self.mementoList.append(Memento(state))

    def get(self, index):
        return self.mementoList[index]

class Originator:
    def __init__(self):
        self.state = ""

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state

    def saveStateToMemento(self):
        return Memento(self.state)

    def getStateFromMemento(self, memento):
        self.state = memento.getState()

def main():
    originator = Originator()
    caretaker = Caretaker()
    while True:
        print("Enter your choice:")
        print("1. Write")
        print("2. Undo")
        print("3. Redo")
        print("4. Exit")
        choice = int(input())
        if choice == 1:
            print("Enter text:")
            text = input()
            originator.setState(text)
            caretaker.add(originator.saveStateToMemento())
            print("Text written successfully")
        elif choice == 2:
            if len(caretaker.mementoList) > 0:
                originator.getStateFromMemento(caretaker.get(len(caretaker.mementoList) - 1))
                caretaker.mementoList.pop()
                print("Undo successful")
            else:
                print("Nothing to undo")
        elif choice == 3:
            if len(caretaker.mementoList) > 0:
                originator.getStateFromMemento(caretaker.get(len(caretaker.mementoList) - 1))
                print("Redo successful")
            else:
                print("Nothing to redo")
        elif choice == 4:
            sys.exit()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
