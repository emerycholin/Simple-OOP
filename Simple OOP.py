class team:
    
    salary_raise = 1.05
    
    def __init__(self, city, name, salary):
        self.city = city
        self.name = name
        self.salary = salary
        
    def fullname(self):
        return '{} {}'.format(self.city, self.name)
    
    def apply_raise(self):
        self.salary = int(self.salary * self.salary_raise)
    
t1 = team('Calgary', 'Flames', 80000000)
t2 = team('Arizona', 'Coyotes', 80000000)
t3= team('Florida', 'Panthers', 80000000)

t1.salary_raise = 1.06

t1.apply_raise()
t2.apply_raise()

print(t1.salary)
print(t2.salary)


print(t3.fullname())

print(t1.__dict__)
