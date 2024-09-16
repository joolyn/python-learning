class Dog:
	species = "Canis familiaris"

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def description(self):
		return f"{self.name} is {self.age} years old"

	def sound(self, sound):
		return f"{self.name} says {sound}"

miles = Dog("Miles", 1)
budy = Dog("Budy", 2)

print(miles.sound("AUUU"))