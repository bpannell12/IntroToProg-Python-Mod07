# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   BPannell, 5.27.2024,Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# TODO Create a Person Class
class Person:
    """
    A collection of functions that create the Person records using the first and last names.
    Includes error handling for invalid name entries.
    ChangeLog: (Who, When, What)
    BPannell, 5.27.2024,Created Class
    """
    # TODO Add first_name and last_name properties to the constructor
    def __init__(self,first_name: str,last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    # TODO Create a getter and setter for the first_name property
    @property
    def first_name(self)->str:
        ''' Returns the first name with a starting capital letter
        :return: First name, ensuring first letter is capitalized
        '''
        return self._first_name.title()

    @first_name.setter
    def first_name(self,value:str) -> None:
        '''Sets the first name and checks for value errors
        :param value: The first name to set
        '''
        if value.isalpha():
            self._first_name = value
        else:
            raise ValueError("First name contains only alphabet letters.")

    # TODO Create a getter and setter for the last_name property
    @property
    def last_name(self)->str:
        ''' Returns the last name with a starting capital letter
        :return: Last name, ensuring first letter is capitalized
        '''
        return self._last_name.title()

    @last_name.setter
    def last_name(self, value: str) -> None:
        '''
        Sets the last name and checks for value errors
        :param value: The last name to set
        '''
        if value.isalpha():
            self._last_name = value
        else:
            raise ValueError("Last name contains only alphabet letters.")

    # TODO Override the __str__() method to return Person data
    def __str__(self) -> str:
        return f'{self.first_name},{self.last_name}'

# TODO Create a Student class the inherits from the Person class
class Student(Person):
    """
    A collection of functions that combine the Person records with the course name to create a complete registration
    record.

    ChangeLog: (Who, When, What)
    BPannell, 5.27.2024,Created Class
    """


    def __init__(self, first_name: str, last_name: str, course_name: str):
        super().__init__(first_name,last_name) # TODO call to the Person constructor and pass it the first_name and last_name data
        self.course_name = course_name

    # TODO add an assignment to the course_name property using the course_name parameter
    # TODO add the getter for course_name
    @property
    def course_name(self) -> str:
        '''
        Returns the course name
        :return: Course name
        '''
        return self._course_name

    # TODO add the setter for course_name
    @course_name.setter
    def course_name(self, value) -> None:
        self._course_name = value

# TODO Override the __str__() method to return the Student data
    def __str__(self) -> str:
        return f'{super().__str__()},{self.course_name}'

# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing functions that work with Json files: read data from an existing file, write data back
    to the file with error handling for both processes
    ChangeLog: (Who, When, What)
    BPannell, 5.27.2024,Created Class
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list[Student]) -> list[Student]:
        """ This function reads data from a json file and loads it into a list of rows

        ChangeLog: (Who, When, What)
        BPannell, 5.27.2024, Created function

        :param file_name: string data with name of file to read from
        :param student_data: list of rows to be filled with file data

        :return: list
        """

        file_data = []
        file = None
        try:
            file = open(file_name, "r")
            file_data = json.load(file)
            file.close()
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)

        finally:
            if file is not None and not file.closed:
                file.close()
        for row in file_data:
                student_data.append(
                    Student(row['first_name'],row['last_name'],row['course_name'])
                )
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list[Student]):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        BPannell, 5.27.2024,Created function

        :param file_name: string data with name of file to write to
        :param student_data: list of rows to be written to the file

        :return: None
        """

        file_data = []
        for student in student_data:
            file_data.append({'first_name': student.first_name,
                              'last_name': student.last_name,
                              'course_name': student.course_name})

        file=None
        try:
            file = open(file_name, "w")
            json.dump(file_data, file)
            file.close()
            IO.output_student_and_course_names(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message,error=e)
        finally:
            if file is not None and not file.closed:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A group of functions that handle user input and output including formatting and error handling

    ChangeLog: (Who, When, What)
    BPannell, 5.27.2024,Created Class
    BPannell, 5.27.2024,Added menu output and input functions
    BPannell, 5.27.2024,Added a function to display the data
    BPannell, 5.27.2024,Added a function to display custom error messages
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays error messages to the user

        ChangeLog: (Who, When, What)
        BPannell, 5.27.2024,Created function

        :param message: string with message to display in case of error
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        BPannell, 5.27.2024,Created function


        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function collects user input for the menu choice

        ChangeLog: (Who, When, What)
        BPannell, 5.27.2024,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list[Student]):
        """ This function displays the current data set of student and course names

        ChangeLog: (Who, When, What)
        BPannell, 5.27.2024,Created function

        :param student_data: list of dictionary rows to be displayed

        :return: None
        """

        print("-" * 50)
        for student in student_data:
            print(f'Student {student.first_name} '
                  f'{student.last_name} is enrolled in {student.course_name}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list[Student])->list[Student]:
        """ This function collects user input: first name, last name and course name.

        ChangeLog: (Who, When, What)
        BPannell, 5.27.2024,Created function

        :param student_data: list of rows to be filled with input data

        :return: list
        """

        try:
            student_first_name = input("Enter the student's first name: ")
            student_last_name = input("Enter the student's last name: ")
            course_name = input("Please enter the name of the course: ")
            student = Student(student_first_name,
                              student_last_name,
                              course_name)
            student_data.append(student)
            print()
            print(f'You have registered {student_first_name} {student_last_name} for {course_name}.')
        except ValueError as e:
            IO.output_error_messages(message="One of the values was the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data

# Define the Data Variables
students: list[Student] = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.

# Start of main body

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)
print(students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

print("Program Ended")
