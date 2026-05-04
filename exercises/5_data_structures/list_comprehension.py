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


all_people = [
    {'name': 'Reuven', 'age': 48, 'hobbies': ['Python', 'cooking', 'reading']},
    {'name': 'Atara', 'age': 27, 'hobbies': ['horses', 'cooking', 'art', 'reading']},
    {'name': 'Shikma', 'age': 13, 'hobbies': ['Python', 'piano', 'cooking', 'reading']},
    {'name': 'Amotz', 'age': 60, 'hobbies': ['biking', 'cooking']},
]


# (1) Average age, with optional upper-age filter
def average_age(people, under=None):
    ages = [p['age'] for p in people if under is None or p['age'] < under]
    return sum(ages) / len(ages) if ages else 0


# (2) All unique hobbies across everyone
unique_hobbies = {hobby for p in all_people for hobby in p['hobbies']}

# (3) Hobby count per person
hobby_counts = {p['name']: len(p['hobbies']) for p in all_people}


print(average_age(all_people))          # all
print(average_age(all_people, under=50)) # under 50 only
print(unique_hobbies)
print(hobby_counts)
