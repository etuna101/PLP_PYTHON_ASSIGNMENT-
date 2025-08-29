# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"

# Derived class (Inheritance)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)   # call parent constructor
        self.__storage = storage         # encapsulated (private attribute)
        self.battery = battery
    
    # Getter for encapsulated storage
    def get_storage(self):
        return self.__storage
    
    # Setter for encapsulated storage
    def set_storage(self, new_storage):
        if new_storage > 0:
            self.__storage = new_storage
        else:
            print("Invalid storage size ")
    
    def call(self, contact):
        print(f"Calling {contact} from {self.device_info()}")

    def charge(self):
        print(f" {self.device_info()} is charging...")

# Create objects
phone1 = Smartphone("Apple", "iPhone 15", 256, "90%")
phone2 = Smartphone("Samsung", "Galaxy S24", 512, "80%")

# Use methods
phone1.call("Alice")
phone2.charge()
print("Phone1 storage:", phone1.get_storage())

# Encapsulation in action
phone1.set_storage(512)
print("Updated Phone1 storage:", phone1.get_storage())
