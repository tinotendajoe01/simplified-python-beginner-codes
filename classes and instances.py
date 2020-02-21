'''a python class is like a blueprint ofcreating an instance
a class is like a blue print for a house, you will need the attributes and methods to build a house from a blueprint.
literally you can think of a python class as a class of students and the attributes or features of a class includes names of students, age ,gender and thier avarage perfomance. so a class here is more like  a representative blue print holding the expected details of the instance/objects (students in this case)'''

class Pharmacy:
    #initialise the class fuction by defining the instances/object features (student features in this example)
    def __init__(self, first, last, age,gender):
        self.first =first
        self.last =last
        self.age = age
        self.gender=gender
        self.email = first + '.' + last + '@gmail.com'
#create a func inside the class ,for calling out full student name, see line 25 and line 26 for alternative method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

#pass in the values you have specified in the init method above for each student
student_a = Pharmacy('joe', 'thomas',21,'male')
student_b = Pharmacy('alice', 'baile',24,'female')
 #ONCE you have pass in the instances the student details will be run automatically in the class fucntion NB: instances must be passes in the right order as in the initialised func
#now you can run the following comands depending on what you want to pull out of your class

print(student_a.email)
print(student_b.email)
print(student_a.fullname())
print('{} {}' .format(student_a.first, student_a.last))