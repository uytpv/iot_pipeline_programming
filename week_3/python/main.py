from person import Person

print("Program starting.")

print("Creating person...")
person = Person("John", "Doe", 30)
print("Person created.")

print("Name:", person.getFullname())
print("Age:", person.getAge())

print("Person has now birthday...")
person.ageUp()
print(f"New age: {person.getAge()}")

print("Program ending.")
