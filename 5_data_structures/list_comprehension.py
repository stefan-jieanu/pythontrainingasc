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

from functools import reduce


all_people = [{'name':'Reuven', 'age':48, 'hobbies':['Python', 'cooking', 'reading']},
                {'name':'Atara', 'age':27, 'hobbies':['horses', 'cooking', 'art', 'reading']},
                {'name':'Shikma', 'age':13, 'hobbies':['Python', 'piano', 'cooking', 'reading']},
                {'name':'Amotz', 'age':60, 'hobbies':['biking', 'cooking']}]

# Really loved lambda exprexsions so this is why I wanted to first start with this <3
# (1) Return the average age of all people
age_average = sum(person['age'] for person in all_people) / len(all_people)
print(f"Age average: {age_average}");

# (1.b) or (optionally) all people under a given age.
age_limit = 40
filter_list = list(filter(lambda person: person['age'] < age_limit, all_people))
age_average_with_limit = sum(person['age'] for person in filter_list) / len(filter_list)
print(f"Age average with limit: {age_average_with_limit}")

# Solution using a function
# (1) Return the average age of all people, or (optionally) all people under a given age.
def age_average_func(people, max_age=None):
    if max_age is not None:
        people = list(filter(lambda person: person['age'] < max_age, people))
    
    return sum(person['age'] for person in people) / len(people)

print(f"(v2) Age average: {age_average_func(all_people)}")
print(f"(v2) Age average with limit {age_average_func(all_people, 40)}")


# (2) Return a set of the different hobbies enjoyed by people in our database.
people_hobbies = set(reduce(lambda acc, value: acc + value['hobbies'], all_people, []))
print(f"People hobbies: {",".join(people_hobbies)}")

# (3) Count how many hobbies each person has
hobby_counts = {person['name']: len(person['hobbies']) for person in all_people}
print(f"Each person hobbies: {hobby_counts}")