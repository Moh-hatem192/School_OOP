import csv
class Teacher:
    SCHOOL = 'OMAREYAH'
    def __init__(self, name, position, phone, email, hours_worked, hourly_rate, job_type='full_time',from_file =False):
        self.name = name
        self.position = position
        self.phone = phone
        self.email = email
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        self.job_type = job_type
        if not from_file:
            All_teachers.add_teacher(self)
    
    def __str__(self):
        return f'{self.name} works as a {self.job_type} {self.position} '    

    def __repr__(self):
        return f'Teacher: (name = {self.name}, job = {self.position}, email = {self.email}'

    def calculate_gross_salary(self):
        gross_salary = self.hours_worked * self.hourly_rate
        return gross_salary
    
    def calculate_net_salary(self):
        gross_salary = self.calculate_gross_salary()
        net_salary = Finance.calculate_net_salary(gross_salary)
        return net_salary
    

class Manager(Teacher):
    pass

class Teachers_file_handler:
    @classmethod
    def create_instances(cls, file):
        with open(file) as f:
            reader = csv.DictReader(f)
            for teacher in reader:
                teacher = Teacher(
                    teacher.get('name'),
                    teacher.get('position'),
                    teacher.get('phone'),
                    teacher.get('email'),
                    float(teacher.get('hours_worked')),
                    float(teacher.get('hourly_rate')),
                    teacher.get('job_type'),
                    True
                )
                All_teachers.add_teacher(teacher)

class All_teachers:
    __Teachers = []    
    @classmethod
    def add_teacher(cls, teacher):
        cls.__Teachers.append(teacher)

    @classmethod
    def show_teachers(cls):
        return cls.__Teachers

class Finance:
    INSURANCE = 100
    HIGH_RATE = 0.18
    LOW_RATE = 0.4
    FIXED_AMOUNT = 1400
    RETIRMENT_COST = 15 
    
    @staticmethod
    def calculate_tax(salary):
        if salary >= Finance.FIXED_AMOUNT:
            tax = Finance.HIGH_RATE * salary
            return tax
        tax = salary * Finance.LOW_RATE
        return tax
    
    @staticmethod
    def calculate_net_salary(salary):
        All_deductions = Finance.RETIRMENT_COST + Finance.INSURANCE + Finance.calculate_tax(salary)
        net_salary = salary - All_deductions
        return net_salary    

osama = Teacher('osama', 'chemistry teacher', '099', 'mohf', 100, 13)
print(osama.calculate_gross_salary())
print(osama.calculate_net_salary())