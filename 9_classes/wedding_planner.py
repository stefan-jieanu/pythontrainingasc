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


from collections import namedtuple

Person = namedtuple("Person", ["first", "last"])

class TableFull(Exception):
    pass

class GuestList:
    def __init__(self):
        self._seats = {}

    def assign(self, person, table):
        if table is not None:
            count_at_table = sum(
                1 for p, m in self._seats.items() if m == table and p != person
            )
            if count_at_table >= 10:
                raise TableFull
        self._seats[person] = table

    def total_guests(self):
        return len(self._seats)

    def at_table(self, table_num):
        return [p for p, m in self._seats.items() if m == table_num]

    def unassigned(self):
        return [p for p, m in self._seats.items() if m is None]

    def free_space(self):
        out = {}
        for table in {m for m in self._seats.values() if m is not None}:
            occupied = sum(1 for m in self._seats.values() if m == table)
            out[table] = 10 - occupied
        return out

    def guests(self):
        def sort_key(p):
            m = self._seats[p]
            table_order = float("inf") if m is None else m
            return (table_order, p.last, p.first)

        return sorted(self._seats.keys(), key=sort_key)


if __name__ == "__main__":
    gl = GuestList()
    gl.assign(Person("Marcel", "Victor"), 1)
    gl.assign(Person("Bogdan", "Bejenaru"), 1)
    gl.assign(Person("Cosmin", "Matei"), 3)
    gl.assign(Person("Luca", "Lalea"), 1)
    gl.assign(Person("Maria", "Batista"), 2)
    gl.assign(Person("Dorin", "Muresan"), 2)
    gl.assign(Person("Elvira", "Suciu"), None)
    gl.assign(Person("Estera", "Rica"), 2)
    gl.assign(Person("Mariana", "Stanescu"), 3)
    gl.assign(Person("Tiberiu", "Castor"), None)
    gl.assign(Person("Ovidiu", "Moldovan"), 3)
    gl.assign(Person("Daniel", "Vidraru"), 2)
    print("Total guests:", gl.total_guests())
    print("Table 1:", gl.at_table(1))
    print("Unassigned:", gl.unassigned())
    print("Free space per table:", gl.free_space())
    print("Sorted guest list:", gl.guests())