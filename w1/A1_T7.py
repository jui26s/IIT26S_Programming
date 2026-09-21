print("Calculate fuel consumption")
Feed=(input("Enter traveldistance (killometers): "))
Distance=float(Feed)
Feed=(input("Enter fuel usage (liters): "))
FuelUsage=float(Feed)
Consumption=FuelUsage / Distance * 100
Consumption=float(Consumption)
print(f"Fuel consumption is {Consumption} liters per 100 kilometers")
