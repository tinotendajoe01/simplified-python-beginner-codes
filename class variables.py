
'''inside a class instances are always not similar but however there are similar variables will be the same for every object of the class eg compulsory courses , bonus marks, lets take bonus marks as the cvariable for every pharmacy student and add it to our previous class code'''

class Pharmacy:
    add_bonus = 10
    #num_of_students = 0
    def __init__(self, first, last, age, gender, course, marks):
        self.first = first
        self.last = last
        self.age = age
        self.course = course
        self.gender = gender
        self.email = first + '.' + last + '@gmail.com'
        self.marks = marks

        Pharmacy.num_of_students += 1
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
#use the apply method to asign the additional marks to every student,but define the bonus marks .see line 5
    def apply_bonus(self):
        self.marks= int(self.marks + Pharmacy.add_bonus)

student_a = Pharmacy('joe', 'thomas', 21, 'male', 'physiology', 500)
student_b = Pharmacy('alice', 'baile', 24, 'female', 'anatomy', 45)

print(student_a.marks)
student_a.apply_bonus()
print(student_a.marks)

#print(student_a.__dict__) #student infomation
#print(Pharmacy.__dict__)
student_a.add_bonus = 20 # this changes the bonus for student a only
#print(Pharmacy.add_bonus)
print(student_a.add_bonus)
print(student_b.add_bonus)
#print(Pharmacy.num_of_students)