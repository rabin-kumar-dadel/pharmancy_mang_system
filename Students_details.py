class students:
    def __init__(self,name,department):
        self.name = name
        self.department = department

    def showData(self):
        print(f'name of the teacher is {self.name} department of the teacher is {self.department}')


    def user_input(self,name,dept):
        self.name = name
        self.dept = dept




        




name = str(input("enter your name"))
depart = str(input("enter your department"))
Teach = students(name,depart)
Teach.user_input(name,depart)
Teach.showData()