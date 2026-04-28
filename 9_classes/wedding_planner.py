# It's time for a wedding. But we have a bunch of guests, and we need to organize them in some way.  
# We're going to do that with a GuestList class. We'll create an instance of this class, and add our guests (as named tuples) into the guest list, 
# along with a table number. We'll then be able to ask our class for a complete guest list by table, as well as a report of which tables aren't yet full.

# Here's how the class should work:
# Person should be a named tuple, with "first" and "last" attributes    
# gl = GuestList()    
# gl.assign(Person('Waylon', 'Dalton'), 1)    
# gl.assign(Person('Justine', 'Henderson'), 1)    
# gl.assign(Person('Abdullah', 'Lang'), 3)   
# gl.assign(Person('Marcus', 'Cruz'), 1)   
# gl.assign(Person('Thalia', 'Cobb'), 2)   
# gl.assign(Person('Mathias', 'Little'), 2)    
# gl.assign(Person('Eddie', 'Randolph'), None)    
# gl.assign(Person('Angela', 'Walker'), 2)    
# gl.assign(Person('Lia', 'Shelton'), 3)    
# gl.assign(Person('Hadassah', 'Hartman'), None)    
# gl.assign(Person('Joanna', 'Shaffer'), 3)    
# gl.assign(Person('Jonathon', 'Sheppard'), 2)

# In the above code, I've created a guest list.  Each Person is then created and assigned to a table. 
# If we assign a person to table None, they aren't assigned.

# We will assume, for the purposes of this exercise, that everyone in the world has a unique name.

# We will also assume that a maximum of 10 people can be added to a given table.
# Attempting to add more than 10 people to a table results in a TableFull exception.

# Now we want to run a few reports on our guest list. Implement methods for the the GuestList class that will return:

# (1) How many guests are there, total?  

# (2) What guests are at a given table?

# (3) What guests aren't assigned to any table?  

# (4) Given a Person object, we should be able to assign them to a table:
#  p = Person('Joanna', 'Shaffer')   
#  gl.assign(p, 3)

# If the person is already in the system, but is assigned to another table (or to no table at all), then they will now be assigned to a new table.
# If the person isn't already in the system, then they will be added and then assigned to a table.
# If there is no room at the table (i.e., there are already 10 guests there), then we should raise a TableFull exception.

# (5) We should also be able to learn how much space is available at each table:
#    gl.free_space()

# The above should return a dictionary of table names (keys) and remaining space (values) for each table.

# (6) We should be able to say
#    gl.guests()

# and get a list of all guests, sorted first by table number, then by last name, and finally by first name.

class TableFull(Exception):
    def __str__(self):
        return "Table is full!"


class Person:
    def __init__(self, first, last):
        self.name = (first, last)
        
    def __eq__(self, value):
        return self.name == value.name

class GuestList:
    def __init__(self):
        self.list = []

    def __number_of_person_at_table(self, table):
        persons_at_table = 0
        for person in self.list:
            if(person and person["table"] == table):
                persons_at_table += 1

        return persons_at_table
    
    def __person_at_table(self, table):
        persons_at_table = []
        for person in self.list:
            if(person and person["table"] == table):
                persons_at_table.append(person)

        return persons_at_table
    
    def __get_person(self, person):
        for assigned_person in self.list:
            if(assigned_person["person"] == person):
                return assigned_person
    
    def get_total_persons(self):
        return len(self.list)

    def get_number_of_persons_by_table(self, table):
        return self.__number_of_person_at_table(table)
    
    def get_persons_by_table(self, table):
        return self.__person_at_table(table)

    def assign(self, person: Person, table):
        if(table is not None and self.__number_of_person_at_table(table) > 10):
            raise TableFull()

        assigned_person = self.__get_person(person)
        if(assigned_person):
            assigned_person["table"] = table
        else:
            person_info = {
                "person": person,
                "table": table
            }

            self.list.append(person_info)


    def free_space(self):
        tables = list({item["table"] for item in self.list})
        salon = {}
        for table in tables:
            if(table is None):
                salon[table] = {"unasigned": self.__number_of_person_at_table(table)}
            else:
                salon[table] = {"remaining": 10 - self.__number_of_person_at_table(table)}
        
        return salon

    def guests(self):
        return sorted(
            self.list,
            key=lambda x: (
                x["table"] if x["table"] is not None else 999,
                x["person"].name[1],
                x["person"].name[0]
            )
        )


gl = GuestList()    
gl.assign(Person('Waylon', 'Dalton'), 1)    
gl.assign(Person('Justine', 'Henderson'), 1)    
gl.assign(Person('Abdullah', 'Lang'), 3)   
gl.assign(Person('Marcus', 'Cruz'), 1)   
gl.assign(Person('Thalia', 'Cobb'), 2)   
gl.assign(Person('Mathias', 'Little'), 2)    
gl.assign(Person('Eddie', 'Randolph'), None)    
gl.assign(Person('Angela', 'Walker'), 2)    
gl.assign(Person('Lia', 'Shelton'), 3)    
gl.assign(Person('Hadassah', 'Hartman'), None)    
gl.assign(Person('Joanna', 'Shaffer'), 3)    
gl.assign(Person('Joanna', 'Shaffer'), 2)    
gl.assign(Person('Jonathon', 'Sheppard'), 2)

print(f"Total Persons: {gl.get_total_persons()}")

print(f"Number of persons at table two: {gl.get_number_of_persons_by_table(2)}")

print(f"Number of unasigned: {gl.get_number_of_persons_by_table(None)}")

print(f"Unasigned persons: {gl.get_persons_by_table(None)}")

print(gl.free_space())
print(gl.guests())