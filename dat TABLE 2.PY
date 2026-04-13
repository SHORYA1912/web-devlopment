import matplotlib.pyplot as plt

student_names= ["ALICE","BOB","CHARLIE","DAVID","EMILY", "AJAY", "FIONA", "GEORGE", "HENRY", "ISABELLA", "JACK", "KAREN", "LEO", "MIA", "NATHAN", "OLIVIA", "PETER", "QUINN", "RACHEL", "SAMUEL"]
students_attendance=[95,80,85,90,92,21,91,87,93,19,94,22,45,91,25,92,89,90,87,91]

attendance_perc = []
for attendance in students_attendance:
    res = (attendance / 100) * 100
    attendance_perc.append(res)
    print(attendance_perc)

def attendance_line_charts():
    plt.plot(student_names, attendance_perc)
    plt.xlabel("Student Names")
    plt.ylabel("Percentage Attendance")
    plt.title("Student Attendance")
    plt.show()

attendance_line_charts()

def attendance_bar_charts():
    plt.bar(student_names, attendance_perc)
    plt.xlabel("Student Names")
    plt.ylabel("Percentage Attendance")
    plt.title("Student Attendance")
    plt.show()

attendance_bar_charts()

