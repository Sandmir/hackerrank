__author__ = 'Senyutina'


class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self,firstName, lastName, idNumber,scores):
        '''
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        '''
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores
    def calculate(self):
        sum_sc = sum(scores)/numScores
        if 90 <= sum_sc <= 100:
           return 'O'
        elif 80 <= sum_sc < 90:
           return 'E'
        elif 70 <= sum_sc < 80:
           return 'A'
        elif 55 <= sum_sc < 70:
           return 'P'
        elif 40 <= sum_sc < 55:
           return 'D'
        elif  sum_sc < 40:
           return 'T'


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())