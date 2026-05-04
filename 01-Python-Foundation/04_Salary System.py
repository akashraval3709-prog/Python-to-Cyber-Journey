class Employee:
    def salary(self):
        print("Employee salary calculation\n")


class FullTimeEmployee(Employee):
    def salary(self):
        super().salary()
        self.amount = 30000
        print(f"Full Time Salary: ₹{self.amount}")


class PartTimeEmployee(Employee):
    def salary(self, hr=8):
        self.rate = 500
        print(f"Part Time Salary: ₹{self.rate * hr}")


class Intern(Employee):
    def salary(self):
        self.amount = 8000
        print(f"Intern Salary: ₹{self.amount}")


s = [FullTimeEmployee(), PartTimeEmployee(), Intern()]

for i in s:
    i.salary()
