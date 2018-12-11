class Member:

    def __init__(self, full_name):
        self.full_name = full_name

    def introduce(self):
        print("Hi, my name is " + self.full_name +"!")


class Student(Member):

    def __init__(self, full_name, reason):
        super().__init__(full_name)
        self.reason = None

    def set_reason(self, reason):
        self.reason = reason


class Instructor(Member):

    def __init__(self, full_name, bio, skills):
        super().__init__(full_name)

    def set_bio(self, bio):
        self.bio = bio

    def set_skills(self, skills):
        self.skills = []


class Workshop:

    def __init__(self, date, subject, instructors, students):
        self.date = date

    def set_date(self, date):
        self.date = date

    def set_bio(self, subject):
        self.subject = subject

    def set_instructors(self, instructors):
        self.instructors = []

   def set_students(self, students):
        self.students = []

### Answer KEY ###
### ask about set .vs. not setting??? ###
class Workshop:
    def __init__(self, date, subject):
        self.date = date
        self.subject = subject
        self.participants = []
        self.instructors = []

    def add_participant(self, participant):
        if isinstance(participant, Instructor):
            self.instructors.append(participant)
        elif isinstance(participant, Student):
            self.participants.append(participant)
     def print_details(self):
        print("Workshop - {} - {}".format(self.date, self.subject))
        print("Students")
        for index, student in enumerate(self.participants):
            print("{}. {} - {}".format(index + 1, student.full_name, student.reason))
        print("Instructors")
        for index, instructor in enumerate(self.instructors):
            print("{}. {} - {} \n {}".format(index + 1, instructor.full_name,
                ', '.join(instructor.skills), instructor.bio))



