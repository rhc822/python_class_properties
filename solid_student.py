"""
Define a Python class named Student. This class will have 5 properties:
First name (string)
Last name (string)
Age (integer)
Cohort number (integer)
Full name (read-only string)
"""

class Student:

    def __init__(self):
        self.__first_name = ""
        self.__last_name = ""
        self.__age = int()
        self.__cohort_number = int()
        self.__full_name = ""

    @property
    def first_name(self):
        try:
            return self.__first_name
        except AttributeError:
            return 0

    @property
        def last_name(self):
            try:
                return self.__last_name
            except AttributeError:
                return 0

    @property
        def age(self):
            try:
                return self.__age
            except AttributeError:
                return 0

    @property
        def last_name(self):
            try:
                return self.__cohort_number
            except AttributeError:
                return 0

    @property
        def last_name(self):
            try:
                return self.__full_name
            except AttributeError:
                return 0


x = Student("John")
print(x.first_name)
x.first_name = "bob"

# x.first_name = "Bob"



#for prop, value in x.__dict__.items():
#    print(f'{prop}:\n{value}\n')

# Define getters for all properties.
# Define a setter for all but the read only property.
# Ensure that only the appropriate value can be assigned to each.
# The full name property should return first name and last name separated by a space. It's value cannot be set.