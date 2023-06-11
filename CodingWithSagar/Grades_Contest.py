#Taking Number of Questions as input from user
no_of_question=int(input("Please enter no of questions in exam="))
#Taking No of correct responses from User
no_of_correct_question=int(input("Please enter no of correct responses="))
#Taking marks of each question
no_of_question_mark=int(input("Please enter marks of each question="))
#Calculating Total marks earned
total_marks=no_of_question*no_of_question_mark
#Printing Total marks
print(f"Total no of marks of exam is {total_marks}")
#Total Marks eaerned after correct response
total_marks_of_correct_question=no_of_correct_question*no_of_question_mark
#Printing total marks
print(f"Total Marks Earned are={total_marks_of_correct_question}")
#Calcluating percentage
percentage=total_marks_of_correct_question/total_marks*100
#Printing Percentage
print(f"Percentage of total marks earned is={percentage}")
#Calculating Grades
if(percentage>=91 and percentage<=100):
    print(f"Your Final Grade is A")
elif(percentage>=81 and percentage<=90):
    print("Your Final Grade is B")
elif(percentage>=71 and percentage<=80):
    print("Your Final Grade is C")
elif(percentage>=61 and percentage<=70):
    print("Your Final Grade is D")
else:
    print("Your Final Grade is F")