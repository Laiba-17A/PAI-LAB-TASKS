
class student:
    def __init__(self,name,id):
        self.name = name
        self.id = id

        
    def display(self):
        print("Name:",self.name)
        print("ID:",self.id)
        

class marks(student):
    def __init__(self,name,id,pai_marks,la_marks,coal_marks):
        super().__init__(name,id)
        self.pai_marks = pai_marks
        self.la_marks = la_marks
        self.coal_marks = coal_marks

    def display(self):
        super().display()
        print("PAI Marks:",self.pai_marks)
        print("LA Marks:",self.la_marks)
        print("COAL Marks:",self.coal_marks)

class result(marks):
    def __init__(self,name,id,pai_marks,la_marks,coal_marks):
        super().__init__(name,id,pai_marks,la_marks,coal_marks)

    def display(self):
        super().display()
        total = self.pai_marks + self.la_marks + self.coal_marks
        avg = total / 3
        print("Total Marks:",total)
        print("Average Marks:",avg)

r = result("laiba",14,85,90,80)
r.display()
        
