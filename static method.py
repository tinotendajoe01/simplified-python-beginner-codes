'''from the previous blocks of class code if you have been following we noticed that
 general classes automatically takes the instance as the first arguement that is ''self'' variable
 and also that class methods automatically pass the class ''cls'' as the firt arguement. now static methods dont pass anything automatically,
 they dont pass the instance or the class ,they behave like regular functions'''

#TAKE FOR INSTANCE THAT WE WANT A SIMPLE FUNCTION THAT WILL TAKE IN ANY DATE AND RETURN WETHER OR NOT THAT IS A SCHOOL DAY

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
        self.marks = int(self.marks + Pharmacy.add_bonus)

    # a class method allows you to work with a class instead of instances
    @classmethod
    def set_bonus_marks(cls, bonusmarks):
        cls.add_bonus = bonusmarks


    @classmethod
    def from_string(cls, student_str):
        first, last, age, gender, course, marks = student_str.split('-')
        return cls(first, last, age, gender, course, marks)
#create the static method and since it doesnt take in any instances go a head a pass in the variable date in this case
# in python modules weekdays are represented by number 0 for monday so 5 and 6 in this case are for the weekends
    @staticmethod
    def  is_school_day(day):
         if day.weekday() == 5 or  day.weekday() == 6:
            return False

         return True


student_a = Pharmacy('joe', 'thomas', 21, 'male', 'physiology', 500)
student_b = Pharmacy('alice', 'baile', 24, 'female', 'anatomy', 45)

#import datetime module and create the pass in the current date
import datetime
current_date =datetime.date(2020, 2, 22)

print(Pharmacy.is_school_day(current_date))


