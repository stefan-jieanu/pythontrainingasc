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

# Ciprian Serban
all_people = [
    {'name': 'Pamfil', 'age': 33, 'hobbies': ['dancing', 'writing', 'reading']},
    {'name': 'Lucian', 'age': 27, 'hobbies': ['climbing', 'traveling', 'photography', 'reading']},
    {'name': 'Radu', 'age': 13, 'hobbies': ['coding', 'guitar', 'traveling', 'reading']},
    {'name': 'Gheorghe', 'age': 60, 'hobbies': ['biking', 'singing']}
]

def average_age(people, max_age=None):
    filtered = [x['age'] for x in people if max_age is None or x['age'] < max_age]
    return sum(filtered) / len(filtered)

def all_hobbies(people):
    return {hobby for x in people for hobby in x['hobbies']}

def hobby_count(people):
    return {x['name']: len(x['hobbies']) for x in people}

print(average_age(all_people))
print(average_age(all_people, max_age=30))
print(all_hobbies(all_people))
print(hobby_count(all_people))