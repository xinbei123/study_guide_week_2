"""Solutions for part 3."""

from practice_part2 import Exam, Student, Question


class StudentExam(object):
    """An exam belonging to a particular student. Contains student's score."""

    def __init__(self, student, exam):
        self.student = student
        self.exam = exam
        self.score = None

    def take_test(self):
        """Administer exam to student and record score."""

        self.score = self.exam.administer()

        print("Your score is {:.2f} percent.".format(self.score))


def example():
    """Show usage of exam, questions, and student."""

    exam = Exam('midterm')

    parent_q = Question(
        'What is the parent class for a non-inheriting Python class?',
        'object')
    exam.add_question(parent_q)

    init_q = Question(
        'Which special method determines how to initialize instances?',
        '__init__')
    exam.add_question(init_q)

    opinionated_q = Question(
        'What is the greatest programming language ever?',
        'Python')  # note from Joel: actual answer: LISP
    exam.add_question(opinionated_q)

    student = Student(
        'Jasmine',
        'Debugger',
        '1010 Computer Street')

    jasmine_midterm = StudentExam(student, exam)

    jasmine_midterm.take_test()
