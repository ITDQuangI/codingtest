from abc import ABC, abstractmethod

###############################################################################
#### Initialize a car abstract class
###############################################################################
class Car(ABC):
    'Car abstract class'

    def __init__(self):
        self.detail = {'wheels': 4, 'doors': 4, 'seets': 5}

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def info(self):
        pass


class BMWCar(Car):
    'Class for BMW Car'

    def __init__(self):
        super().__init__()
        self._maxSpeed = 200

    def run(self, *, lock=None, event=None):
        if lock is not None:
            lock.acquire()
            [print(self._maxSpeed) for _ in range(10)]
            lock.release()
        else:
            if event is not None:
                for _ in range(10):
                    print(self._maxSpeed)
                    event[0].set()
                    event[1].clear()
                    event[1].wait()
                event[0].set()
            else:
                [print(self._maxSpeed) for _ in range(10)]
        return True

    def info(self):
        [print("%s = %s" %(key, value)) for key, value in self.detail.items()]
        print("maxSpeed = %s" %self._maxSpeed)
        return True

class ToyotaCar(BMWCar):
    'Class for Toyota Car'

    def __init__(self):
        super().__init__()
        self._maxSpeed = 100
