#GPA Calculator
Grades = {'A': 4.0, 'A-': 3.7, 'B+':3.3, 'B':3.0, 'B-': 2.7,'C+': 2.3,  'C':2.0, 'C-': 1.7, 'D+': 1.3, 'D':1.0}
number_of_classes = int(input('How many classes do you have'))


Classes = []
for i in range(0,number_of_classes):

    Classe = input('What did you get in this class?')
    Classes.append(Classe)

print(Classes)

Values = 0
for i in Classes:
   if i in Grades:
       Values += Grades[i]
print(Values)

Gpa = Values / number_of_classes
print(Gpa)
