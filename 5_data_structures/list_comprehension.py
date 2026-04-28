# We have a list of dictionaries, in which each dict represents a person. That dict will then have three key-value pairs:
# - name
# - age
# - hobbies

# The final value, "hobbies", will be a list of strings describing the person's hobbies.

# For example, here is a list of people:

#     all_people = [{'name':'Reuven', 'age':48, 'hobbies':['Python', 'cooking', 'reading']},
#                   {'name':'Atara', 'age':27, 'hobbies':['horses', 'cooking', 'art', 'reading']},
#                   {'name':'Shikma', 'age':13, 'hobbies':['Python', 'piano', 'cooking', 'reading']},
#                   {'name':'Amotz', 'age':60, 'hobbies':['biking', 'cooking']}]

# Using the power of list comprehensions in python let's create some reports from this data.

# (1) Return the average age of all people, or (optionally) all people under a given age.
# (2) Return a set of the different hobbies enjoyed by people in our database.
# (3) Count how many hobbies each person has


all_people = [{'name':'Reuven', 'age':48, 'hobbies':['Python', 'cooking', 'reading']},
                {'name':'Atara', 'age':27, 'hobbies':['horses', 'cooking', 'art', 'reading']},
                {'name':'Shikma', 'age':13, 'hobbies':['Python', 'piano', 'cooking', 'reading']},
                {'name':'Amotz', 'age':60, 'hobbies':['biking', 'cooking']}]

# (1) Return the average age of all people, or (optionally) all people under a given age.
def age_average_func(people, max_age=None):
    if max_age is not None:
        people = [person for person in people if person['age'] < max_age]
    return sum(person['age'] for person in people) / len(people)

print(f"Age average: {age_average_func(all_people)}")
print(f"Age average with limit {age_average_func(all_people, 40)}")

# (2) Return a set of the different hobbies enjoyed by people in our database.
def hobbies_set_func(people):
    hobbies = set()
    for person in people:
        for hobby in person['hobbies']:
            hobbies.add(hobby)
    return hobbies

print(f"Hobbies set: {hobbies_set_func(all_people)}")

# (3) Count how many hobbies each person has
hobby_counts = [f"{person['name']}: {len(person['hobbies'])}" for person in all_people]
print(f"Each person hobbies: {hobby_counts}")
