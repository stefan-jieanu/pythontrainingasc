from typing import TypedDict
from functools import reduce

# We have a list of dictionaries, in which each dict represents a person. That dict will then have three key-value pairs:
# - name
# - age
# - hobbies

# The final value, "hobbies", will be a list of strings describing the person's hobbies.

# For example, here is a list of people:

all_people = [{'name':'Reuven', 'age':48, 'hobbies':['Python', 'cooking', 'reading']},
              {'name':'Atara', 'age':27, 'hobbies':['horses', 'cooking', 'art', 'reading']},
              {'name':'Shikma', 'age':13, 'hobbies':['Python', 'piano', 'cooking', 'reading']},
              {'name':'Amotz', 'age':60, 'hobbies':['biking', 'cooking']}]

# Using the power of list comprehensions in python let's create some reports from this data.

# (1) Return the average age of all people, or (optionally) all people under a given age.
# (2) Return a set of the different hobbies enjoyed by people in our database.
# (3) Count how many hobbies each person has

class Person(TypedDict):
  name: str
  age: int
  hobbies: list[str]


#1
def get_avg_age(people: list[Person]) -> int:
  ages = [p["age"] for p in people]
  return sum(ages) / len(ages)

print("Average age: ", get_avg_age(all_people))


def get_people_under(people: list[Person], age: int) -> list[Person]:
  return list(filter(lambda p: p["age"] < age, people))

print("People under 18: ", get_people_under(all_people, 18))


#2
def get_all_hobies(people: list[Person]) -> set[str]:
  hobbies = [p["hobbies"] for p in people] # [[], [], []]
  return reduce(lambda acc, curr: acc | set(curr), hobbies, set())

print ("Hobbies: ", get_all_hobies(all_people))


#3
def count_hobbies(people: list[Person]) -> list[dict[str, str | int]]:
  return [ {"name": p["name"], "no_of_hobbies": len(p["hobbies"])} for p in people]

print("Hobbies count", count_hobbies(all_people))