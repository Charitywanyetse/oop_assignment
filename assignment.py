
# Qustion
class cohort:
    name = "charity"
    description = "cohort 4 "
    start_date = "20th august 2024"
    end_date = "2026"
    num_of_students = 25

# within the cohort class ,
# add a constractor for the cohort class.(read about constractors and object/instances)

def _init_(self,name,description,start_date,end_date,num_of_students):
    self.name = name
    self.description = description
    self.start_date = start_date
    self.end_date = end_date
    self.num_of_students = num_of_students


# add a method to the class that prints the cohort name and the total number of students.

def print_cohort_info(self):
    print(f"cohort name: {self.name}")
    print(f"total students: {self.num_of_students}")


# create a new instance/object of the cohort class

cohort_4 = cohort("charity","cohort 4","20th august 2024","2026",25)

cohort_4.print_cohort_info()