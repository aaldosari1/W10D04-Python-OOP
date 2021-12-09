# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 11:26:12 2021

@author: kaa
""" 
class Universty_personnel:
    def __init__(self, person_id,name, university_id, university_email):
        self.person_id=person_id
        self.name=name
        self.university_id=university_id
        self.university_email=university_email
        
    
    def set_ids(self, ids):
        person_id, university_id = ids.split(" ")
        self.person_id = person_id
        self.university_id = university_id
      
    def set_email_and_name(self, name_email):
        name, university_email = name_email.split(" ")
        self.name = name
        self.university_email = university_email
        
        
    def get_personnel_info(self):
        return f"Personnel Information: Id: {self.person_id}, name: {self.name}, university Id: {self.university_id},  University email: {self.university_email}"
        
        
personnel_1 = Universty_personnel("192", "Saeed", "20000","Saeed@gmail.com")

personnel_1.set_ids("200 30000")
personnel_1.set_email_and_name("Faisal Faisal@gmail.com")

print(personnel_1.get_personnel_info())




class Teacher(Universty_personnel):
    def __init__(self,person_id,name,university_id,university_email ,specialization, salary_per_hour,teaching_hours):
        super().__init__(person_id,name,university_id,university_email)
        self.specialization = specialization
        self.salary_per_hour = salary_per_hour
        self.teaching_hours = teaching_hours
        
    def set_specialization(self,specialization):
        self.specialization=specialization
    def set_salary(self,salary_per_hour):
        self.salary_per_hour=salary_per_hour
    def set_teaching_hours(self, teaching_hours):    
        self.teaching_hours=teaching_hours
    def get_specialization(self):
        return self.specialization
    def get_salary(self):
        return self.salary_per_hour
    def get_teaching_hours(self):
        return self.teaching_hours
    def calculate_salary(self):
        return f"total salary :{self.get_salary() * self.teaching_hours}"  
    def get_personnel_info(self):
        return f"Personnel Information: Id: {self.person_id}, name: {self.name}, university Id: {self.university_id},  University email: {self.university_email}, specialization:{self.specialization}, salary per hour: {self.salary_per_hour}, number of teaching hours: {self.teaching_hours} "
        
        
teacher_1 = Teacher("38576", "Saeed", "20000","Saeed@gmail.com", "History", 9000,22)
teacher_1.set_ids("8356 89956")
teacher_1.set_email_and_name("Faisal Faisal@hotmail.com")
teacher_1.set_specialization("Geography")
teacher_1.set_salary(10000)
teacher_1.set_teaching_hours(20)
print(teacher_1.get_personnel_info())  
print(teacher_1.calculate_salary())


class Student(Universty_personnel):
    def __init__(self,person_id,name,university_id,university_email , level, number_of_points,credit):
        super().__init__(person_id,name,university_id,university_email)
        self.level=level
        self.number_of_points=number_of_points
        self.credit=credit
        
    def set_level(self,level):
        self.level=level
    def set_number_of_points(self,number_of_points):
        self.number_of_points=number_of_points
    def set_credit(self, credit):    
        self.credit=credit
    def get_level(self):
        return self.level
    def get_number_of_points(self):
        return self.number_of_points
    def get_credit(self):
        return self.credit
    def calculate_gpa(self):
        return f" student GPA :{self.get_credit() * self.get_number_of_points()}"
    def get_personnel_info(self):
        return f"Personnel Information: Id: {self.person_id}, name: {self.name}, university Id: {self.university_id},  University email: {self.university_email}, level:{self.level}, number of points: {self.number_of_points}, credit: {self.credit}"

Student_1 = Student("3442", "fofo", "1212","fofo@gmail.com", "6th", 60, 4 )

Student_1.set_ids("10201 47213")
personnel_1.set_email_and_name("Khalid Khalid@gmail.com")
Student_1.set_level("4th")
Student_1.set_number_of_points(50)
Student_1.set_credit(2)

print(Student_1.get_personnel_info()) 
print(Student_1.calculate_gpa())


        
        
        
        
        
        
        
        
        