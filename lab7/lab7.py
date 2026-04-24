class Vehicle:
    def __init__(self, vid, model, year):
        self.vid = vid
        self.model = model
        self.year = year

    def __eq__(self, other):
        return self.vid == other.vid

    def is_new(self, n):
        return (2026 - self.year) <= n

    def __str__(self):
        return f"VID: {self.vid:<5} | {self.model:<15} ({self.year})"

class Car(Vehicle):
    def __init__(self, vid, model, year, fuel_type, doors):
        super().__init__(vid, model, year)
        self.fuel_type = fuel_type
        self.doors = doors

    def __str__(self):
        return f"[Car]        {super().__str__()} | Fuel: {self.fuel_type:<8} | {self.doors} Doors"

class Truck(Vehicle):
    def __init__(self, vid, model, year, max_load, axles):
        super().__init__(vid, model, year)
        self.max_load = max_load
        self.axles = axles

    def __str__(self):
        return f"[Truck]      {super().__str__()} | Load: {self.max_load}kg | {self.axles} Axles"

class Motorcycle(Vehicle):
    def __init__(self, vid, model, year, engine_cc, type):
        super().__init__(vid, model, year)
        self.engine_cc = engine_cc
        self.type = type

    def __str__(self):
        return f"[Motorcycle] {super().__str__()} | Eng: {self.engine_cc}cc | Type: {self.type}"


def save_fleet_to_file(vehicles, filename):

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for v in vehicles:
                type_name = v.__class__.__name__

                if type_name == "Car":
                    line = f"Car, {v.vid}, {v.model}, {v.year}, {v.fuel_type}, {v.doors}"
                elif type_name == "Truck":
                    line = f"Truck, {v.vid}, {v.model}, {v.year}, {v.max_load}, {v.axles}"
                elif type_name == "Motorcycle":
                    line = f"Motorcycle, {v.vid}, {v.model}, {v.year}, {v.engine_cc}, {v.type}"

                f.write(line + "\n")
        print(f"Filo başarıyla '{filename}' dosyasına kaydedildi.")
    except Exception as e:
        print(f"Dosya kaydedilirken bir hata oluştu: {e}")


def load_fleet_from_file(filename):
    reconstructed_vehicles = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                data = [item.strip() for item in line.strip().split(',')]

                if not data or data[0] == "":
                    continue

                vehicle_type = data[0]

                if vehicle_type == "Car":
                    obj = Car(data[1], data[2], int(data[3]), data[4], int(data[5]))
                elif vehicle_type == "Truck":
                    obj = Truck(data[1], data[2], int(data[3]), int(data[4]), int(data[5]))
                elif vehicle_type == "Motorcycle":
                    obj = Motorcycle(data[1], data[2], int(data[3]), int(data[4]), data[5])
                else:
                    print(f"Bilinmeyen araç türü atlandı: {vehicle_type}")
                    continue

                reconstructed_vehicles.append(obj)

        return reconstructed_vehicles
    except FileNotFoundError:
        print(f"Hata: '{filename}' dosyası bulunamadı.")
        return []
    except Exception as e:
        print(f"Dosya okunurken bir hata oluştu: {e}")
        return []


vehicles_list = [
    Car("V001", "Tesla Model 3", 2023, "Electric", 4),
    Car("V002", "Toyota Corolla", 2018, "Petrol", 4),
    Truck("T101", "Volvo FH16", 2019, 25000, 6),
    Truck("T102", "Mercedes Actros", 2021, 18000, 4),
    Motorcycle("M301", "Yamaha R1", 2024, 998, "Sport"),
    Motorcycle("M302", "Harley Davidson", 2015, 1200, "Cruiser")
]

save_fleet_to_file(vehicles_list, "fleet.txt")

loaded_vehicles = load_fleet_from_file("fleet.txt")

print(f"\nLoading fleet data from 'fleet.txt'...")
print(f"{len(loaded_vehicles)} vehicles loaded successfully.")

print("\n--- All Vehicles ---")
for v in loaded_vehicles:
    print(v)

print("\n--- Recent Vehicles (Last 4 Years) ---")
for v in loaded_vehicles:
    if v.is_new(4):
        print(v)

print("\n--- Electric Cars Only ---")
for v in loaded_vehicles:
    if isinstance(v, Car) and v.fuel_type == "Electric":
        print(v)

