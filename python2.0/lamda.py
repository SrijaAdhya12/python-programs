people = [{"name": "Srija", "age": 20}, 
          {"name": "Pritam", "age": 21}, 
          {"name": "Mario", "age": 22}
]

#lambda function
people.sort(lambda person: person['age'])

double= lambda x: x*2