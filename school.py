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
                    teacher.get('hours_worked'),
                    teacher.get('hourly_rate'),
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
