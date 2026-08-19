def get_marks():
    marks={}
    user= int(input("Enter a total subject: "))

    for i in range(user):
        subject_name=input("Subject Name: ")
        subject_mark=int(input("Enter a marks: "))
        marks[subject_name]=subject_mark
    return marks


def calculate_average(marks):
    total=sum(marks.values())
    average=total/len(marks)

    return average

def get_grade(average):
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade ="D"
    else:
        grade = "Fail"

    return grade 

    
def show_result(marks, average, grade):
    print("Total Marks: ", marks)
    print("Average : ", average)
    print("Grade: ", grade)

marks=get_marks()
average=calculate_average(marks)
grade= get_grade(average)
show_result(marks, average, grade)
