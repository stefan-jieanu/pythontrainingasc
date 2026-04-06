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

class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __repr__(self):
        return f"Person('{self.first}', '{self.last}')"

    def __eq__(self, other):
        return self.first == other.first and self.last == other.last

    def __hash__(self):
        return hash((self.first, self.last))

class TableFull(Exception):
    def __init__(self, table):
        super().__init__(f"Table {table} is full.")

class GuestList:
    def __init__(self):
        self.guests = {}
        self.tables = {}
        self.max_table_size = 10
    
    def assign(self, person, table):
        # Remove from old table if already assigned
        if person in self.guests:
            old_table = self.guests[person]
            if old_table is not None and old_table in self.tables:
                self.tables[old_table].remove(person)

        if table is not None:
            if table not in self.tables:
                self.tables[table] = []
            if len(self.tables[table]) >= self.max_table_size:
                raise TableFull(table)
            self.tables[table].append(person)
        self.guests[person] = table

    def __len__(self):
        return len(self.guests)

    def table(self, table_number):
        return self.tables.get(table_number, [])
    
    def unassigned(self):
        return [person for person, table in self.guests.items() if table is None]
    
    def free_space(self):
        return {table: self.max_table_size - len(guests) for table, guests in self.tables.items()}

    def get_guests(self):
        assigned = [(person, table) for person, table in self.guests.items() if table is not None]
        unassigned = [(person, float('inf')) for person, table in self.guests.items() if table is None]
        
        all_guests = assigned + unassigned
        all_guests.sort(key=lambda x: (x[1], x[0].last, x[0].first))
        
        return [person for person, table in all_guests]


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
gl.assign(Person('Jonathon', 'Sheppard'), 2)


# (1)
print("Total guests:", len(gl))

# (2)
print("Table 1:", gl.table(1))

# (3)
print("Unassigned guests:", gl.unassigned())

# (4)
p = Person('Joanna', 'Shaffer')
gl.assign(p, 2)

# (5)
print("Free space:", gl.free_space())

# (6)
print("All guests:", gl.get_guests())
