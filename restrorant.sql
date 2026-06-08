drop table if exists restaurant;
CREATE table if not exists restaurant(
    name TEXT, 
    neighborhood TEXT,
    cuisine TEXT,
    price TEXT,
    health TEXT,
    review REAL
);

insert into restaurant (name, neighborhood, cuisine, price, health, review) values 
('Pizza Place', 'Downtown', 'Italian', '$$', 'A', 4),
('Sushi Spot', 'Uptown', 'Japanese', '$$$', 'B', 5),
('Burger Joint', 'Midtown', 'American', '$', 'B', 3),
('Taco Stand', 'Downtown', 'Mexican', '$', 'A', 4),
('Pasta House', 'Uptown', 'Italian', '$$', 'A', 5),
('Curry Corner', 'Midtown', 'Indian', '$$', 'B', 4),
('BBQ Pit', 'Downtown', 'American', '$$$', 'C', 3),
('Vegan Cafe', 'Uptown', 'Vegan', '$$', 'A', 5),
('Seafood Shack', 'Midtown', 'Seafood', '$$$', 'B', 4),
('Dumpling Den', 'Downtown', 'Chinese', '$$', 'A', 5);

select distinct neighborhood 
from restaurant;

select distinct cuisine
from restaurant;

select * from restaurant
where cuisine = 'Chinese';

select * from restaurant
where review >= 4 ;

select * from restaurant
where cuisine = 'Chinese' and price = '$$' and health = 'A';

select * from restaurant
where price = '$$$';

select * from restaurant
where name like '%candy%';

select * from restaurant
where neighborhood in ('Downtown', 'Uptown', 'Midtown');

select * from restaurant
where health ='' or health is NULL;

select * from restaurant
order by review desc;