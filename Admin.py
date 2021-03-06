class User():
    """User info of a user"""

    def __init__(self, f_name, l_name, location, age, education):
        """root info for this program"""
        self.f_name = f_name.title()
        self.l_name = l_name.title()
        self.location = location.title()
        self.age = age
        self.education = education

    def describe_user(self):
        """Summary of the user"""
        print('  Hello ' + self.f_name , self.l_name + '!')
        print('Location: ' + self.location)
        print('Age: ' + str(self.age))
        print('Eduction: ' + self.education)

    def greeting(self):
        """A special personalised greeting to the user"""
        print(' ' + self.f_name + '! Thank You, for taking part in the survey.\n')


class Admin(User):
    """This is a baby class of the above class, It is being written to give priveliges to the Admin"""

    def __init__(self,  f_name, l_name, location, age, education):
        super().__init__(f_name, l_name, location, age, education)

        self.privileges = []
    
    def show_privileges(self):
        """This method will display the display the privileges of the admin"""
        
        print(' Following are the privileges of an admin: ')
        for privileges in self. privileges:
            print(' - ' + privileges)
    

mac = Admin('Harshwardhan', 'OP', 'Dehradun', 16, 'In High School')
mac.privileges = [
    'Can post unlimited posts',
    'No video limit',
    'Can add anyone',
    'Can remove anyone', 
    'Can contest any compititions'
]

mac.describe_user()
mac.show_privileges()
