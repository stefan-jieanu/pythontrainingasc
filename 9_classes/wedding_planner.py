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

# In the above code, I've created a guest list. Each Person is then created and assigned to a table.
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

Person = namedtuple('Person', ['first', 'last'])

MAX_TABLE_SIZE = 10


class TableFull(Exception):
    pass


class GuestList:
    def __init__(self):
        self._guests = {}  # Person -> table number (or None)

    def assign(self, person, table):
        if table is not None:
            seats_taken = sum(1 for p, t in self._guests.items() if t == table and p != person)
            if seats_taken >= MAX_TABLE_SIZE:
                raise TableFull(f"Table {table} is full.")
        self._guests[person] = table

    def total(self):
        return len(self._guests)

    def at_table(self, table):
        return [p for p, t in self._guests.items() if t == table]

    def unassigned(self):
        return [p for p, t in self._guests.items() if t is None]

    def free_space(self):
        tables = {t for t in self._guests.values() if t is not None}
        return {t: MAX_TABLE_SIZE - sum(1 for v in self._guests.values() if v == t) for t in tables}

    def guests(self):
        return sorted(
            self._guests.keys(),
            key=lambda p: (self._guests[p] is None, self._guests[p], p.last, p.first)
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
gl.assign(Person('Jonathon', 'Sheppard'), 2)

print("Total guests:", gl.total())
print("At table 1:", gl.at_table(1))
print("Unassigned:", gl.unassigned())
print("Free space:", gl.free_space())
print("All guests:", gl.guests())
