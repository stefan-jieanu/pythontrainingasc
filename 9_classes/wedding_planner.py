from dataclasses import dataclass

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
        
class TableFullException(Exception):
    def __init__(self, ):
        super().__init__("Table is full!")

@dataclass
class Person:
    first_name: str
    last_name: str

    # assuming all Person instances with the same first ana last name are the same person (as per requirements)
    def __eq__(self, other: Person):
        return self.first_name == other.first_name and self.last_name == other.last_name


@dataclass
class Table:
    guests: list[Person]
    empty_seats: float # infinity for standing

    def add_to_table(self, person: Person) -> None:
        if(self.empty_seats == 0):
            raise TableFullException()
        if(person in self.guests):
            return
        self.guests.append(person)
        self.empty_seats = self.empty_seats - 1

    def remove_from_table(self, person: Person) -> None:
        if(person not in self.guests):
            return
        self.guests.remove(person)
        self.empty_seats = self.empty_seats + 1


class GuestList():
    def __init__(self, max_seats_per_table: int = 10):
        self.max_seats_per_table = max_seats_per_table
        self.tables: dict[str, Table] = {}
        self.standing: Table = Table([], float('inf'))
    #1
    def get_guests_count(self) -> float:
        return sum([self.max_seats_per_table - table.empty_seats for table in self.tables.values()]) + len(self.standing.guests)
    
    #2
    def get_guests_at_table(self, table_no: int | str | None) -> list[Person]:
        table_key = str(table_no)
        if(table_key not in self.tables.keys()):
            return []
        return self.tables[table_key].guests

    #3
    def get_guests_standing(self) -> list[Person]:
        return self.standing.guests
    
    #4
    def assign(self, person: Person, table_no: int | str | None) -> None:
        table_key = str(table_no)
        #cleanup possible previous assignment
        if(person in self.standing.guests):
            self.standing.remove_from_table(person)
        else:
            pre_assigned_at_table_no = next((no for no, table in self.tables.items() if person in table.guests), None)

            if(table_key and pre_assigned_at_table_no == table_key):
                return
            if(pre_assigned_at_table_no):
                if(self.tables[pre_assigned_at_table_no].empty_seats == self.max_seats_per_table - 1):
                    del self.tables[pre_assigned_at_table_no]
                else:
                    self.tables[pre_assigned_at_table_no].remove_from_table(person)

        #assign to new table
        if(not table_key):
            self.standing.add_to_table(person)
        elif(table_key in self.tables.keys()):
            self.tables[table_key].add_to_table(person)
        else:
            self.tables[table_key] = Table([person], self.max_seats_per_table - 1)

    #5
    def free_space(self, table_no: int | str) -> float:
        table_key = str(table_no)
        if(table_key not in self.tables):
            return self.max_seats_per_table
        return self.tables[table_key].empty_seats
    
    #6
    def guests(self) -> list[Person]:
        def sort_by_name(guests: list[Person]) -> list[Person]:
            return sorted(guests, key=lambda guest: f"{guest.last_name} {guest.first_name}")
            
        # standing guests at the end?
        sorted_tables = [table.guests for _, table in sorted(self.tables.items(), key=lambda tuple: tuple[0])] + [self.standing.guests]
        return [guest for guestList in sorted_tables for guest in sort_by_name(guestList)]



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


#1
print("Total guests: ", gl.get_guests_count())
print("\n")

#2
print("Guests at table 1: \n", gl.get_guests_at_table(1))
print("\n")

#3
print("Guests standing: \n", gl.get_guests_standing())
print("\n")

#4 
# a. Existing Hadassah Hartman guest moves from standing to table 1
gl.assign(Person('Hadassah', 'Hartman'), 1)
print("Guests at table 1 after assigning Hadassah Hartman is seated: \n", gl.get_guests_at_table(1))
print("\n")

print("Guests standing after assigning Hadassah Hartman is seated: \n", gl.get_guests_standing())
print("\n")

print("Total guests after assigning Hadassah Hartman is seated: ", gl.get_guests_count())
print("\n")

# b. New John Doe is seated at table 1
gl.assign(Person("John", "Doe"), 1)
print("Guests at table 1 after assigning John Doe is seated: \n", gl.get_guests_at_table(1))
print("\n")

print("Total guests after assigning John Doe is seated: ", gl.get_guests_count())
print("\n")

# c. Existing John Doe moves from table 1 to standing
gl.assign(Person("John", "Doe"), None)
print("Guests at table 1 after assigning John Doe is standing: \n", gl.get_guests_at_table(1))
print("\n")

print("Guests standing after assigning John Doe is standing: \n", gl.get_guests_standing())
print("\n")

#5
print("Free space at table 1: ", gl.free_space(1))
print("\n")

#6
print("All guests: \n", gl.guests())
