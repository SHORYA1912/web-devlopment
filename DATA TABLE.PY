import matplotlib.pyplot as plt
 
student_names= ["ALICE","BOB","CHARLIE","DAVID","EMILY", "AJAY"]
students_scores=[99,25,78,65,88,92]

mark_perc = []
for score in students_scores:
    res = (score / 100) * 100
    mark_perc.append(res)

print(mark_perc)

def marks_line_charts():
    plt.plot(student_names, mark_perc)
    plt.xlabel("Student Names")
    plt.ylabel("Percentage Marks")
    plt.title("Student Performance")
    plt.show()

marks_line_charts()

def marks_bar_charts():
    plt.bar(student_names, mark_perc)
    plt.xlabel("Student Names")
    plt.ylabel("Percentage Marks")
    plt.title("Student Performance")
    plt.show()

marks_bar_charts()