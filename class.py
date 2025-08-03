from abc import ABC, abstractmethod

#  Base Device and Smartphone with Encapsulation & Inheritance ===
class Device(ABC):
    def __init__(self, brand, model):
        self._brand = brand
        self._model = model

    @abstractmethod
    def specs(self):
        pass

    def __str__(self):
        return f"{self._brand} {self._model}"

class Smartphone(Device):
    def __init__(self, brand, model, storage_gb, camera_mp):
        super().__init__(brand, model)
        self.__storage_gb = storage_gb
        self.__camera_mp = camera_mp

    def specs(self):
        return {
            "Brand": self._brand,
            "Model": self._model,
            "Storage (GB)": self.__storage_gb,
            "Camera (MP)": self.__camera_mp
        }

    def upgrade_storage(self, additional_gb):
        if additional_gb > 0:
            self.__storage_gb += additional_gb

# === Polymorphism with Vehicles ===
class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Driving "

class Plane(Vehicle):
    def move(self):
        return "Flying "

class Boat(Vehicle):
    def move(self):
        return "Sailing "

# === Execution ===
if __name__ == "__main__":
    # Smartphone demo
    phone = Smartphone("Samsung", "Galaxy Z Fold5", 256, 108)
    phone.upgrade_storage(128)
    print("Smartphone Info:")
    print(phone)
    print(phone.specs())
    
    print("\nVehicle Movements:")
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        print(f"{v.__class__.__name__}: {v.move()}")
