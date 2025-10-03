
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calBonus(self):
        pass            

class Manager(Employee):
    def calBonus(self):
        return self.salary * 0.20

    def hire(self):
        print(self.name," is hiring someone.")

class Developer(Employee):
    def calBonus(self):
        return self.salary * 0.10

    def writeCode(self):
        print(self.name," is writing code.")

class SeniorManager(Manager):
    def calBonus(self):
        return self.salary * 0.30   
    

mgr = Manager("Laiba", 80000)
dev = Developer("Arshia", 60000)
smgr = SeniorManager("Javed", 120000)
print("Manager Bonus:", mgr.calBonus())
print("Developer Bonus:", dev.calBonus())
print("Senior Manager Bonus:", smgr.calBonus())
mgr.hire()
dev.writeCode()

