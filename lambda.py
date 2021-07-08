people = [
  {"name": "Harry", "house": "Gryffindor"},
  {"name": "Cho", "house": "Ravenclaw"},
  {"name": "Draco", "house": "Slytherin"}
]

# lambda is a function that gets person's name so we can sort
people.sort(key=lambda person: person['name'])

print(people)