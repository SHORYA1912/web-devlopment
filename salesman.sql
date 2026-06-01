create table salesman (
    salesman_id int primary key,
    name text,
    city text,
    commission text
)insert into salesman( salesman_id, name, city, commission) values
(5001, 'James Hoog', 'New York', '0.15'),
(5002, 'Nail Knite', 'Paris', '0.12'),
(5003, 'Pit Alex', 'London', '0.10'),
(5004, 'Mc Lyon', 'Paris', '0.14'),
(5005, 'Paul Adam', 'Rome', '0.10'),
(5006, 'Allen Adam', 'Rome', '0.11'),
(5007, 'James Adam', 'Rome', '0.16'),
(5008, 'James Adam', 'Rome', '0.11'),
(5009, 'James Adam', 'Rome', '0.15'),
(5010, 'James Adam', 'Rome', '0.11');

create table if not exists customers (
    cust_id int primary key,
    cust_name text,
    city text,
    grade text,
    salesman_id text,
);

insert into customers (cust_id, cust_name, city, grade, salesman_id) values
(3002, 'Alfreds Futterkiste', 'Berlin', '1', 5001),
(3003, 'Ana Trujillo Emparedados y helados', 'Mexico D.F.', '2', 5002),
(3004, 'Antonio Moreno Taquería', 'Mexico D.F.', '3', 5003),
(3005, 'Around the Horn', 'London', '4', 5004),
(3006, 'Berglunds snabbköp', 'Luleå', '5', 5005),
(3007, 'Blauer See Delikatessen', 'Mannheim', '6', 5006),
(3008, 'Blondel père et fils', 'Strasbourg', '7', 5007),
(3009, 'Bólido Comidas preparadas', 'Madrid', '8', 5008),
(3010, 'Bon app''', 'Marseille', '9', 5009);

create table if not exists orders (
    ord_no int primary key,
    purch_amt text,
    ord_date text,
    cust_id text,
    salesman_id text
);

insert into orders (ord_no, purch_amt, ord_date, cust_id, salesman_id) values
(70001, '150.5', '2012-10-05', 3005, 5003),
(70009, '270.65', '2012-09-10', 3001, 5001),
(70002, '65.26', '2012-10-06', 3002, 5002),
(70004, '110.5', '2012-08-17', 3003, 5003),
(70007, '948.5', '2012-09-10', 3004, 5004),
(70005, '2400.6', '2012-09-11', 3005, 5005),
(70008, '5760', '2012-09-12', 3006, 5006),
(70010, '1983.43', '2012-09-13', 3007, 5007),
(70003, '2480.4', '2012-09-14', 3008, 5008),
(70011, '250.45', '2012-09-15', 3009, 5009);


select customers.cust_name, salesman.name , salesman.city
from customers
join salesman on customers.city = salesman.city

select customer.custname, salesman.name
from customers
join salesman on customers.salesman_id = salesman.salesman_id

select order.ord_no, customers.cust_name, salesman.name
from orders
join customers on orders.cust_id = customers.cust_id
join salesman on orders.salesman_id = salesman.salesman_id
where customers.city <> salesman.city 

from orders
join customers on orders.cust_id = customers.cust_id

select customers.cust_name as "customer name", customer.customers.city as "customer city", salesman.name as "salesman name", salesman.city as "salesman city"
from orders
join salesman on orders.salesman_id = salesman.salesman_id
join customers on orders.cust_id = customers.cust_id
where customers.grade is not null;

select customers.cust_name as "customer name"
from orders,customers city as "city"
where orders.cust_id = customers.cust_id
salesman.name as "salesman name"
from orders, salesman
join salesman on orders.salesman_id = salesman.salesman_id
where customers.city = salesman.city

select orders.ord_no ,customers.cust_name, salesman.comission
from orders
join customers on orders.cust_id = customers.cust_id
join salesman on orders.salesman_id = salesman.salesman_id,
where customers.grade = '1' and salesman.comission > 0.12
