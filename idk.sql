create table if not exists students (
    student_id integer primary key,
    student_name text not null,
    marks integer,
    grade text,
    standard text
);

insert into students (student_id, student_name, marks, grade, standard) values
(1, 'Alice', 85, 'A', '10th'),
(2, 'Bob', 78, 'B', '10th'),
(3, 'Charlie', 92, 'A+', '10th'),
(4, 'David', 65, 'C', '10th'),
(5, 'Eve', 88, 'A', '10th');

select student_name, marks, grade
from students
where marks >= 80
order by marks desc;
select standard, avg(marks) as average_marks
from students
group by standard;
select grade, count(*) as total_students
from students
group by grade;
select student_name, marks
from students
where grade = 'A'
order by marks desc;
select student_name, grade
from students
where standard = '10th'
order by grade;
