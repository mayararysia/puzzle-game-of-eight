
class Node:
    # def __init__(self, value, parent, cost):
    def __init__(self, value, cost):
        self._value = value
        self._cost = cost

    def getValue(self):
        return self._value

    # def getParent(self):
    #     return self._parent

    def getCost(self):
        return self._cost

    def setValue(self, newValue):
        self._value = newValue

    # def setParent(self, newValue):
    #     self._parent = newValue

    def setCost(self, newValue):
        self._cost = newValue
