
create table authors (
    author_id integer primary key,
    name text,
    city text,
    royalty_rate real
);

insert into authors(author_id, name, city, royalty_rate) values
(1, 'James Hoog', 'New York', 0.15),
(2, 'Nail Knite', 'Paris', 0.12),
(3, 'Pit Alex', 'London', 0.10),
(4, 'Mc Lyon', 'Paris', 0.14),
(5, 'Paul Adam', 'Rome', 0.10),
(6, 'Allen Adam', 'Rome', 0.11),
(7, 'James Adam', 'Rome', 0.16),
(8, 'Alex Smith', 'Rome', 0.11),
(9, 'Maria Ruiz', 'Rome', 0.15),
(10, 'Liu Wong', 'Rome', 0.11);

create table if not exists members (
    member_id integer primary key,
    full_name text,
    city text,
    membership_level text,
    favorite_author_id integer
);

insert into members (member_id, full_name, city, membership_level, favorite_author_id) values
(1001, 'Alfreds Futterkiste', 'Berlin', 'A', 1),
(1002, 'Ana Trujillo', 'Mexico D.F.', 'B', 2),
(1003, 'Antonio Moreno', 'Mexico D.F.', 'C', 3),
(1004, 'Around the Horn', 'London', 'D', 4),
(1005, 'Berglunds snabbköp', 'Luleå', 'E', 5),
(1006, 'Blauer See', 'Mannheim', 'F', 6),
(1007, 'Blondel père', 'Strasbourg', 'G', 7),
(1008, 'Bólido Comidas', 'Madrid', 'H', 8),
(1009, 'Bon app''', 'Marseille', 'I', 9);

create table if not exists loans (
    loan_id integer primary key,
    book_title text,
    loan_date text,
    member_id integer,
    author_id integer
);

insert into loans (loan_id, book_title, loan_date, member_id, author_id) values
(9001, 'Database Design', '2023-10-05', 1004, 3),
(9002, 'SQL Fundamentals', '2023-09-10', 1001, 1),
(9003, 'Advanced SQL', '2023-10-06', 1002, 2),
(9004, 'Learning SQLite', '2023-08-17', 1003, 3),
(9005, 'Practical Databases', '2023-09-10', 1004, 4),
(9006, 'Data Modeling', '2023-09-11', 1005, 5),
(9007, 'Design Patterns', '2023-09-12', 1006, 6),
(9008, 'Modern SQL', '2023-09-13', 1007, 7),
(9009, 'SQL in Practice', '2023-09-14', 1008, 8),
(9010, 'Intro to Databases', '2023-09-15', 1009, 9);


-- Example queries adapted to library schema
select m.full_name as member_name, a.name as author_name, a.city
from members m
join authors a on m.city = a.city;

select m.full_name, a.name
from members m
join authors a on m.favorite_author_id = a.author_id;

select l.loan_id, m.full_name, a.name
from loans l
join members m on l.member_id = m.member_id
join authors a on l.author_id = a.author_id
where m.city <> a.city;

select m.full_name as "member name", m.city as "member city", a.name as "author name", a.city as "author city"
from loans l
join authors a on l.author_id = a.author_id
join members m on l.member_id = m.member_id
where m.membership_level is not null;

select l.loan_id, m.full_name, a.royalty_rate
from loans l
join members m on l.member_id = m.member_id
join authors a on l.author_id = a.author_id
where m.membership_level = 'A' and a.royalty_rate > 0.12;
