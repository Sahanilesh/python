distance = int(input("Enter total travel distance: "))

if distance < 3:
    transportionMode = "Walk"
elif distance <= 15:
    transportionMode = "Bike"
else:
    transportionMode = "Car"
print("AI recommends you the transport of: ", transportionMode)