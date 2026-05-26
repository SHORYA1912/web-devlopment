create table if not exists departments (
    id int primary key ,
    name text,
    department id text,
    manager id text,
    salary real
);

insert into departments (id, name, department id, manager id, salary) values
(1, 'John Doe', 'HR', 'Jane Smith', 50000),
(2, 'Alice Johnson', 'IT', 'Bob Brown', 60000),
(3, 'Michael Lee', 'Finance', 'Sara Davis', 55000),
(4, 'Emily Wilson', 'Marketing', 'Tom Clark', 45000),
(5, 'David Kim', 'Sales', 'Lisa White', 48000);

select department id as department code, count(*) as "total employees"
from departments
group by department id;


select department id, sum(salary) as "total salary"
from departments;
group by department id;

select department id, avg(salary) as "average salary"
from departments;   
group by department id;

select department id as department code, count(*) as "total employees";
from departments;
(sum(salary) as "total salary"
from departments;
group by department id;

SELECT DEPARTMENT ID, AS DEPARTMENT CODE,
AVG(SALARY) AS "AVERAGE SALARY"
SUM(SALARY) AS "TOTAL SALARY"
COUNT(*) AS "TOTAL EMPLOYEES"
 WHERE DEPARTMENT ID = 'IT'
WHERE ID = 2 
FROM DEPARTMENTS
GROUP BY DEPARTMENT ID;




