# import customtkinter
#
# customtkinter.set_default_color_theme("dark-blue")
# customtkinter.set_appearance_mode('dark')
#

class Vehicle:
    def __init__(self, wheel_count: int = 4, model: str = 'BMW', door_count: int = 4, seat_count: int = 5) -> object:

        # Gives it default values with correct type if none are provided

        """
            HOVER (PyCharm)
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
        except ValueError:
            return print('One of your responses is invalid, please make sure the responses are integers.')
        except:
            return print('We\'ve had an error with making this vehicle.')

    def getInfo(self):  # Returns the properties of veh
        return self.__wheel_count, self.__model_type, \
               self.__door_count, self.__seat_count

    def getModel(self):  # Gets the mdoel type of veh (or could use just getInfo()[1])
        return self.__model_type


class Queue:
    def __init__(self):
        self.__list = []
        self.__maxItems = 3

    def addItem(self, item):
        if not len(self.__list) >= self.__maxItems:
            return self.__list.append(item)

        print(f"You've reached the maximum limit of vehicles. {self.__maxItems}")

    def getItems(self):
        return self.__list

    def isQueueEmpty(self):
        if len(self.__list) == 0:
            return True
        return False

    def removeItem(self):
        if not self.isQueueEmpty():
            return self.__list.pop(0)
        return False


QUEUE = Queue()
Exit = False  # If typed 4, the program should quit
from os import system as sys

clear = lambda: sys('clear')
commands = [['1', 'add', 'add_item'], ['2', 'remove', 'remove_item'], ['3', 'view', 'list'], ['4', 'exit']]
while not Exit:
    try:
        clear()  # Clears the page before each command
        print('What would you like to do? \
          \n 1. Add item to list \
          \n 2. Remove last item from list \
          \n 3. View List \
          \n 4. Exit')
        result = input(' > ')  # Users input
        result = str(result).lower()
        for commands_ in commands:
            if result in commands_:
                if result in commands[3]:
                    Exit = True
                    print('Goodbye')

                if result in commands[0]:
                    model = str(input('What model is the vehicle? \n >  '))
                    wheels = int(input('How many wheels does the vehicle have? (INT) \n >  '))
                    doors = int(input('How many doors does the vehicle have? (INT) \n >  '))
                    seats = int(input('How many seats does the vehicle have? (INT) \n >  '))

                    try:
                        vehicle = Vehicle(wheels, model, doors, seats)  # Creates Vehicle
                        QUEUE.addItem(vehicle)  # Adds the vehicle to list

                        print(f'Added {vehicle.getModel()} to the list!')
                    except Exception as error_message:
                        print(f'You\'ve received an error, please try again. \n Error: {error_message}')

                if result in commands[1]:
                    if not QUEUE.isQueueEmpty():
                        print(f'{QUEUE.removeItem().getModel()} has just been removed!')
                    else:
                        print('Vehicle list is already empty!')
                if result in commands[2]:
                    if not QUEUE.getItems():
                        print('Vehicle list is empty!')
                    else:
                        arr = [item.getInfo()[1] for item in
                               QUEUE.getItems()]  # Makes an array with all of the model types
                        print(arr)

    except Exception:
        print('We\'ve had an error with making this vehicle. Please use the correct data types (INTEGERS)')
        pass  # Stop the program from crashing
    finally:
        input('')  # Let the user press enter again before continuting
