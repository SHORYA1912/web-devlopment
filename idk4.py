import matplotlib.pyplot as plt


def question1():
    days = [1, 2, 3, 4, 5, 6, 7]
    temperature = [30, 32, 31, 29, 30, 28, 27]
    plt.figure(figsize=(6, 4))
    plt.plot(days, temperature, marker='o', linestyle='-', color='tab:red')
    plt.title('Days vs Temperature')
    plt.xlabel('Day')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)


def question2():
    students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan']
    marks = [85, 92, 78, 88, 90]
    plt.figure(figsize=(6, 4))
    plt.bar(students, marks, color='skyblue')
    plt.title('Students and Marks')
    plt.xlabel('Student')
    plt.ylabel('Marks')


def question3():
    subjects = ['Math', 'Science', 'English', 'History', 'Art']
    favorites = [25, 30, 15, 18, 12]
    plt.figure(figsize=(6, 6))
    plt.pie(favorites, labels=subjects, autopct='%1.1f%%', startangle=140)
    plt.title('Favourite Subjects')


def question4():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
    values = [40, 45, 38, 50, 47]
    plt.figure(figsize=(6, 4))
    plt.plot(months, values, marker='s', linestyle='--', color='tab:green')
    plt.title('Monthly Values with Labels')
    plt.xlabel('Month')
    plt.ylabel('Value')


def question5():
    students = ['A', 'B', 'C', 'D', 'E']
    math_marks = [90, 80, 85, 95, 88]
    science_marks = [85, 82, 88, 92, 91]
    plt.figure(figsize=(6, 4))
    plt.plot(students, math_marks, marker='o', linestyle='-', label='Math')
    plt.plot(students, science_marks, marker='s', linestyle='-.', label='Science')
    plt.title('Math and Science Marks')
    plt.xlabel('Student')
    plt.ylabel('Marks')
    plt.legend()


def question6():
    students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan']
    attendance = [95, 88, 92, 85, 90]
    plt.figure(figsize=(6, 4))
    plt.bar(students, attendance, color='mediumseagreen')
    plt.title('Attendance Percentages')
    plt.xlabel('Student')
    plt.ylabel('Attendance (%)')
    plt.ylim(0, 100)


def question7():
    categories = ['Food', 'Travel', 'Shopping']
    expenses = [250, 150, 200]
    plt.figure(figsize=(6, 4))
    plt.bar(categories, expenses, color=['tomato', 'gold', 'skyblue'])
    plt.title('Monthly Expense Chart')
    plt.xlabel('Expense Type')
    plt.ylabel('Amount ($)')


def question8():
    students = ['A', 'B', 'C', 'D']
    marks = [88, 92, 79, 85]
    attendance = [95, 90, 85, 88]
    grades = [30, 40, 20, 10]
    labels = ['A', 'B', 'C', 'D']

    plt.figure(figsize=(12, 8))
    plt.subplot(2, 2, 1)
    plt.bar(students, marks, color='cornflowerblue')
    plt.title('Marks')
    plt.xlabel('Student')
    plt.ylabel('Marks')

    plt.subplot(2, 2, 2)
    plt.plot(students, attendance, marker='o', color='orange')
    plt.title('Attendance')
    plt.xlabel('Student')
    plt.ylabel('Attendance (%)')
    plt.ylim(0, 100)

    plt.subplot(2, 2, 3)
    plt.pie(grades, labels=labels, autopct='%1.0f%%', startangle=90)
    plt.title('Grades Distribution')

    plt.tight_layout()


def question9():
    x = [1, 2, 3, 4, 5]
    y = [10, 14, 12, 16, 18]
    plt.figure(figsize=(8, 4))
    plt.plot(x, y, linestyle='--', marker='D', color='purple')
    plt.title('Customized Graph')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.grid(True)


def question10():
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    temps = [22, 24, 21, 23, 25, 26, 24]
    rainfall = [5, 10, 3, 8, 6, 12, 7]
    humidity = [70, 65, 72, 68, 66, 63, 69]

    plt.figure(figsize=(10, 6))
    plt.plot(days, temps, marker='o', label='Temperature (°C)')
    plt.bar(days, rainfall, alpha=0.4, label='Rainfall (mm)', color='royalblue')
    plt.plot(days, humidity, marker='s', linestyle='--', label='Humidity (%)', color='green')
    plt.title('Weekly Weather Data Visualization')
    plt.xlabel('Day')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)


if __name__ == '__main__':
    question1()
    question2()
    question3()
    question4()
    question5()
    question6()
    question7()
    question8()
    question9()
    question10()
    plt.show()
