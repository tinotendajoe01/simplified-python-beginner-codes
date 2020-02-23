
class Pharmacy:
    add_bonus = 10

    def __init__(self, first, last, age, gender, course, marks):
        self.first = first
        self.last = last
        self.age = age
        self.course = course
        self.gender = gender
        self.email = first + '.' + last + '@gmail.com'
        self.marks = marks


    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_bonus(self):
        self.marks= int(self.marks + Pharmacy.add_bonus)
# a class method allows you to work with a class instead of instances
    @classmethod
    def set_bonus_marks(cls,bonusmarks):
        cls.add_bonus = bonusmarks
#create a class method for an alternative constructor to add the details of students given in string format
    @classmethod
    def from_string(cls, student_str):
        first, last, age, gender,course, marks = student_str.split('-')
        return cls(first,last,age,gender,course,marks)

student_a = Pharmacy('joe', 'thomas', 21, 'male', 'physiology', 500)
student_b = Pharmacy('alice', 'baile', 24, 'female', 'anatomy', 45)

#new data in string format that you will be needing to  add to your class
student_stra = 'faith-kobe-23-male-biology-46'
student_strb = 'josh-pope-25-female-chemistry-234'

# use the class method to transform the string to object by passing in the strings  into the alternative constructor print fullname in line45
new_studenta = Pharmacy.from_string(student_stra)

#line 27 allows you to call the class directly and insert the number of marks within the method class
Pharmacy.set_bonus_marks(100)

'''print(Pharmacy.add_bonus)
print(student_a.add_bonus)
print(student_b.add_bonus)'''
print(new_studenta.fullname())



