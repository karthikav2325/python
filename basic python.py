students =int(input("enter no of students upto 3:"))

for i in range(students):
    print("\nStudents",i+1)
    name = input("enter name:")
    mark1 = int(input("enter mark 1:"))
    mark2 = int(input("enter mark 2:"))
    mark3 = int(input("enter mark 3:"))

    total = mark1 + mark2 + mark3
    average = total / 3

    print("total marks:",total)
    print("average marks:",average)

    if mark1 >=50 and mark2 >=50 and mark3 >=50:
        result = "pass"
        print("result: pass")
    else:
        result = "fail"
        print("result: fail")

    if average >=90:
        grade ="A"
        print("grade:A")
    elif average >=80:
        grade = "B"
        print("garde:B")
    elif average >=70:
        grade = "C"
        print("grade:C")
    elif average >=60:
        grade = "D"
        print("grade:D")
    else:
        grade = "F"
        print("grade:F")

    print("-----------Report card----------")
    print("Name:",name)
    print("Total marks:",total)
    print("Average marks:",average)
    print("Result:",result)
    print("Grade:",grade)