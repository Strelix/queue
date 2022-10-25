class Vehicle:
    def __init__(self, wheel_count: int = 4, model: str = 'BMW', door_count: int = 4, seat_count: int = 5) -> object:
        """
            Wheels      - 4
            Model Type  - BMW
            Doors       - 4
            Seats       - 5
        """
        self.__wheel_count = wheel_count
        self.__model_type = model
        self.__door_count = door_count
        self.__seat_count = seat_count

        try:
            self.__wheel_count = int(wheel_count)
            self.__model_type = str(model)
            self.__door_count = int(door_count)
            self.__seat_count = int(seat_count)
        except:
            print('We\'ve had an error with making this vehicle.')

    def getInfo(self):
        return self.__wheel_count, self.__model_type, \
               self.__door_count, self.__seat_count

    def getModel(self):
        return self.__model_type
class Queue:
    def __init__(self):
        self.__list = []
        self.maxItems = 3

    def addItem(self, item):
        if not len(self.__list) >= 3:
            return self.__list.append(item)

    def getItems(self):
        return self.__list

    def removeItem(self):
        return self.__list.pop()


QUEUE = Queue()
Exit = False
from os import system as sys

clear = lambda: sys('cls')
commands = [['1', 'add', 'add_item'], ['2', 'remove', 'remove_item'], ['3', 'view', 'list'], ['4', 'exit']]
while not Exit:
    try:
        clear()
        print('What would you like to do? \
          \n 1. Add item to list \
          \n 2. Remove last item from list \
          \n 3. View List \
          \n 4. Exit')
        result = input(' > ')
        result = str(result).lower()
        for commands_ in commands:
            if result in commands_:
                if result in commands[3]:
                    Exit = True
                    print('Goodbye')
                if result in commands[0]:
                    model = str(input('what model is the vehicle? \n >  '))
                    wheels = int(input('How many wheels does the vehicle have? \n >  '))
                    doors = int(input('How many doors does the vehicle have? \n >  '))
                    seats = int(input('How many seats does the vehicle have? \n >  '))

                    try:
                        vehicle = Vehicle(wheels, model, doors, seats)
                        QUEUE.addItem(vehicle)

                        print(f'Added {vehicle.getModel()} to the list!')
                    except Exception as error_message:
                        print(f'You\'ve received an error, please try again. \n Error: {error_message}')

                if result in commands[1]:
                    print(f'{QUEUE.removeItem().getModel()} has just been removed!')
                if result in commands[2]:
                    if not QUEUE.getItems():
                        print('Vehicle list is empty!')
                    else:
                        for item in QUEUE.getItems():
                            print(item.getInfo())
    except Exception as error_message:
        print(f'You\'ve received an error, please try again. \n Error: {error_message}') # Stop the program from crashing
    finally:
        input('') # Let the user press enter again before continuting
