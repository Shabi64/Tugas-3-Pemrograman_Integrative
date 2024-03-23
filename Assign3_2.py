from lab import BMI

# Example usage:
person1 = BMI(70, 1.75)  # Weight: 70 kg, Height: 1.75 meters
person2 = BMI(65, 1.70)  # Weight: 65 kg, Height: 1.70 meters

print("Person 1's BMI:", person1.BMI_Value())
print("Person 2's BMI:", person2.BMI_Value())

# Testing equality
print("Are person1 and person2 equal?", person1 == person2)  # Output: False

# Creating a person with the same attributes as person1
person3 = BMI(70, 1.75)
print("Are person1 and person3 equal?", person1 == person3)  # Output: True
