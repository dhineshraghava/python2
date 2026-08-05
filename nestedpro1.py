marks=int(input())
Attendance=int(input())
project_completion=bool(input())
if marks>=60 and Attendance>=75:
    if project_completion =="True":
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")