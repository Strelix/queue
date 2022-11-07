import customtkinter

customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode('dark')

active_colour = '#c242f5'
secondary_colour = '#9830c2'


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
            return app.error('One of your responses is invalid, please make sure the responses are integers.')
        except:
            return app.error('We\'ve had an error with making this vehicle.')

    def getInfo(self):  # Returns the properties of veh
        return self.__wheel_count, self.__model_type, \
               self.__door_count, self.__seat_count

    def getModel(self):  # Gets the mdoel type of veh (or could use just getInfo()[1])
        return self.__model_type


class Queue:
    def __init__(self):
        self.__list = [] # Where the list items are stored
        self.__maxItems = 3 # Maximum list items

    def addItem(self, item):
        if not len(self.__list) >= self.__maxItems:
            return self.__list.append(item) # Appends it if it can "fit"

        app.error(f"You've reached the maximum limit of vehicles. {self.__maxItems}")

    def getItems(self):
        return self.__list

    def getMax(self):
        return self.__maxItems

    def isQueueEmpty(self):
        if len(self.__list) == 0:
            return True
        return False

    def removeItem(self, which):
        if not self.isQueueEmpty():
            if which == 'all':
                self.__list = []
                return True
            elif which == 'last':
                ind = len(self.__list) - 1
                return self.__list.pop(ind)
            else:
                return self.__list.pop(0)
        return False


QUEUE = Queue()

class Page:
    def __init__(self):
        self.currentPage = 'add'
        self.items = []

        self.change_page('add')

    def removeItems(self):
        [item.destroy() for item in self.items]
        return True

    def addItemsToRemoveList(self, *all):
        [self.items.append(item) for item in all]

    def change_page(self, page, **info):
        if str(page) == 'add':
            self.currentPage = 'add'
            self.removeItems()

            if not QUEUE.getMax() > len(QUEUE.getItems()):
                app.error('Maximum items reached! Try removing a vehicle.', 'red')

                return

            app.createVehicleButton.configure(fg_color=active_colour, state='disabled')
            app.removeVehicleButton.configure(fg_color=secondary_colour, state='normal')

            app.modelText = customtkinter.CTkLabel(master=app.right_top_frame,
                                                   text='What model is the vehicle?', )
            app.modelText.pack(side=customtkinter.TOP)

            app.modelInput = customtkinter.CTkEntry(master=app.right_top_frame)
            app.modelInput.pack(side=customtkinter.TOP)

            app.doorsText = customtkinter.CTkLabel(master=app.right_top_frame,
                                                   text='How many doors should the vehicle have?')
            app.doorsText.pack(side=customtkinter.TOP)

            app.doors = customtkinter.CTkOptionMenu(master=app.right_top_frame, values=['2', '4'])
            app.doors.pack(side=customtkinter.TOP)

            app.wheelsText = customtkinter.CTkLabel(master=app.right_top_frame,
                                                    text='How many wheels should the vehicle have?')
            app.wheelsText.pack(side=customtkinter.TOP)

            app.wheels = customtkinter.CTkOptionMenu(master=app.right_top_frame, values=['3', '4', '6', '8'])
            app.wheels.set('4')
            app.wheels.pack(side=customtkinter.TOP)

            app.next = customtkinter.CTkButton(master=app.right_top_frame, text='NEXT', fg_color=active_colour,
                                               command=lambda: self.change_page('add_2', wheels=app.wheels.get(),
                                                                                doors=app.doors.get(),
                                                                                model=app.modelInput.get()),
                                               pady=5)
            app.next.pack(side=customtkinter.TOP)

            self.addItemsToRemoveList(app.next, app.wheels, app.doors, app.doorsText, app.modelInput, app.modelText,
                                      app.wheelsText)

        if str(page) == 'add_2':
            self.currentPage = 'add_2'
            self.removeItems()

            if info['model'] == None or info['model'] == ' ' or info['model'] == '':
                app.error('You\'ve not put a valid model. Please make sure to fill it.', 'red')
                self.removeItems()
                app.createVehicleButton.configure(state='normal', fg_color=secondary_colour)
                return

            app.seatsText = customtkinter.CTkLabel(master=app.right_top_frame,
                                                   text='How many seats should the vehicle have?')
            app.seatsText.pack(side=customtkinter.TOP)

            app.seats = customtkinter.CTkOptionMenu(master=app.right_top_frame,
                                                    values=['2', '3', '4', '5', '6', '8', '9'])
            app.seats.set('5')
            app.seats.pack(side=customtkinter.TOP)

            app.submit = customtkinter.CTkButton(master=app.right_top_frame, text='SUBMIT', fg_color=active_colour,
                                                 command=lambda: self.change_page(
                                                     'add_3', wheels=info['wheels'], doors=info['doors'],
                                                     model=info['model'], seats=app.seats.get()), pady=10)
            app.submit.pack(side=customtkinter.TOP)

            self.addItemsToRemoveList(app.submit, app.seats, app.seatsText)
        if str(page) == 'add_3':
            self.removeItems()
            app.createVehicleButton.configure(state='normal', fg_color=secondary_colour)

            vehicle = Vehicle(info['wheels'], info['model'], info['doors'], info['seats'])  # Creates Vehicle
            QUEUE.addItem(vehicle)  # Adds the vehicle to list
            app.update_list()

        if str(page) == 'remove':
            self.currentPage = 'remove'
            self.removeItems()

            app.what_text = customtkinter.CTkLabel(master=app.right_top_frame,
                                                   text='What would you like to remove from the list?')
            app.what_text.pack(side=customtkinter.TOP)

            app.what = customtkinter.CTkOptionMenu(master=app.right_top_frame,
                                                   values=['Last Item', 'Whole List', 'First Item'])
            app.what.set('First Item')
            app.what.pack(side=customtkinter.TOP)

            def submit():
                what = app.what.get()
                if what in ['Last Item', 0]:
                    QUEUE.removeItem('last')
                elif what in ['Whole list', 1]:
                    QUEUE.removeItem('all')
                else:
                    QUEUE.removeItem('first')

                return app.update_list()

            app.submit = customtkinter.CTkButton(master=app.right_top_frame, text='SUBMIT', fg_color=active_colour,
                                                 command=lambda: submit())
            app.submit.pack(side=customtkinter.TOP)


class Window(customtkinter.CTk):

    def update_list(self):
        array = []
        [array.append(item.getInfo()[1]) for item in QUEUE.getItems()]
        self.right_bottom_list.configure(text=array)

    def error(self, message='App error', colour='blue'):
        if colour == 'blue':
            colour = '#395E9C'
        elif colour == 'red':
            colour = '#eb4034'
        elif colour == 'green':
            colour = '#78de12'

        error_label = customtkinter.CTkLabel(master=self.left_container, text='ERROR: ' + message, text_color=colour,
                                             wraplength='150', pady=20)
        error_label.pack(side=customtkinter.TOP)

        self.after(3000, lambda: error_label.destroy())

    def __init__(self):
        super().__init__()

        self.title("QUEUE")
        self.minsize(625, 500)
        self.maxsize(625, 500)

        self.left_container = customtkinter.CTkFrame(master=self, width=200, height=500, corner_radius=20)
        self.left_container.pack(side=customtkinter.LEFT, padx=15, pady=15)
        self.left_container.pack_propagate(False)

        self.right_container = customtkinter.CTkFrame(master=self, width=500, height=500, corner_radius=20,
                                                      fg_color='#1A1A1A')
        self.right_container.pack(side=customtkinter.RIGHT, padx=15, pady=(15, 15))
        self.right_container.pack_propagate(False)

        self.right_top_frame = customtkinter.CTkFrame(master=self.right_container, width=500, height=225,
                                                      corner_radius=20)
        self.right_top_frame.pack(side=customtkinter.TOP, padx=0, pady=(0, 20))
        self.right_top_frame.pack_propagate(False)

        self.right_bottom_frame = customtkinter.CTkFrame(master=self.right_container, width=500, height=225,
                                                         corner_radius=20)
        self.right_bottom_frame.pack(side=customtkinter.BOTTOM, padx=0, pady=(0, 0))
        self.right_bottom_frame.pack_propagate(False)

        self.createVehicleButton = customtkinter.CTkButton(master=self.left_container, text='Create Vehicle',
                                                           fg_color=secondary_colour,
                                                           command=lambda: PAGE.change_page('add'))
        self.createVehicleButton.pack(pady=(20, 0), padx=(10, 10))

        self.removeVehicleButton = customtkinter.CTkButton(master=self.left_container, text='Remove Vehicle',
                                                           fg_color=secondary_colour,
                                                           command=lambda: PAGE.change_page('remove'))
        self.removeVehicleButton.pack(pady=(20, 0), padx=(10, 10))

        self.right_bottom_list_text = customtkinter.CTkLabel(master=self.right_bottom_frame, text='All Vehicles:')
        self.right_bottom_list_text.pack(side=customtkinter.TOP)

        self.right_bottom_list = customtkinter.CTkLabel(master=self.right_bottom_frame, text='[]')
        self.right_bottom_list.pack(side=customtkinter.TOP)


if __name__ == "__main__":
    app = Window()
    PAGE = Page()

    app.mainloop()
