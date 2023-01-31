"""Python refresher course - Class Inheritance Section"""

class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True # do not need to pass in a parameter for this

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})" # !r is shorthand for the repr method
      
    def disconnect(self):
        self.connected = False
        print("Disconnected.")

# printer = Device("printer", "USB") # creates a new Device object
# print(printer) # prints the new Device object
# printer.disconnect() # uses the disconnect function/method on our new Device object



# creating a new class that inherits the functionality of Device
class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by) # get the "super class" from the parent & initialize those existing fields
        self.capacity = capacity
        self.remaining_pages = capacity # this has the same value b/c it's cut from the same cloth....or something

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)" # ugh

    # this one also makes my brain hurt
    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected.")
            return # we return here so we can exit the function if not connected
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages
        
printer = Printer("Epson", "USB", 500) 
printer.print(20) # Printing 20 pages.
print(printer) # Device 'Epson' (USB) (480 pages remaining)

printer.disconnect() # Disconnected.
