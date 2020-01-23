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

    @first_name.setter
    def first_name(self, new_first_name):
        if type(new_first_name) is str:
            self.__first_name = new_first_name
        else:
            raise TypeError("Please provide a string value.")

    @property
    def last_name(self):
        try:
            return self.__last_name
        except AttributeError:
            return 0

    @last_name.setter
    def last_name(self, new_last_name):
        if type(new_last_name) is str:
            self.__last_name = new_last_name
        else:
            raise TypeError("Please provide a string value.")

    @property
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return 0

    @age.setter
    def age(self, age):
        if type(new_age) is int:
            self.__new_age = new_age
        else:
            raise TypeError("Please provide an integer value.")

    @property
    def cohort_number(self):
        try:
            return self.__cohort_number
        except AttributeError:
            return 0

    @property
    def full_name(self):
        try:
            return self.__full_name
        except AttributeError:
            return 0

a = Student()
a.first_name = "Ryan"
a.last_name = "Cunningham"
a.
print(a.first_name, a.last_name)
#a.first_name = 123


#for prop, value in x.__dict__.items():
#    print(f'{prop}:\n{value}\n')

# Define getters for all properties.
# Define a setter for all but the read only property.
# Ensure that only the appropriate value can be assigned to each.
# The full name property should return first name and last name separated by a space. It's value cannot be set.