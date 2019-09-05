class student:
    def __init__(self,name,age,phone):
        self.name=name
        self.age=age
        self.phone=phone

    def getdetails(self):
        print("Name is :-",self.name)
        print("age is :-",self.age)
        print("Phone number is :-",self.phone)
student1=student("mukund",33,15646517211)

print(student1.getdetails())