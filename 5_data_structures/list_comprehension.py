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
def average_age(people):
    age_sum = 0
    for person in people:
        age_sum += person['age']
    return age_sum / len(people)

def average_age_list_comprehension(people):
    return sum([person['age'] for person in people]) / len(people)

print("(1) Return the average age of all people, or (optionally) all people under a given age.",average_age(all_people))
print("(1) Return the average age of all people, or (optionally) all people under a given age.",average_age_list_comprehension(all_people))
print("--------------------------------")
# (2) Return a set of the different hobbies enjoyed by people in our database.
def unique_hobbies(people):
    all_hobbies = set()
    for person in people:
        for hobby in person['hobbies']:
            all_hobbies.add(hobby)
    return all_hobbies

def unique_hobbies_list_comprehension(people):
    return set(hobby for person in people for hobby in person['hobbies'])
print("(2) Return a set of the different hobbies enjoyed by people in our database.\n",unique_hobbies_list_comprehension(all_people))
print("--------------------------------")
# (3) Count how many hobbies each person has    
def count_hobbies(people):
    return {person['name']: len(person['hobbies']) for person in people}

print("(3) Count how many hobbies each person has \n",count_hobbies(all_people))