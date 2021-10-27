print("Welcome to the Miles Per Hour Conversion App")

# User input
mph = float(input("What is your speed in miles per hour: "))

# Use a conversion ratio of 1 mph = 0.4474 mps
mps = round(mph * 0.4474, 2)
print(f"Your speed in meters per second is: { mps }")