create table if not exists noble_price_winner (
    id serial primary key,
    year int,
    winner text,
    name text,
    profession text
);

insert into noble_price_winner (year, winner, name, profession) values
(2020, 'Physics', 'Roger Penrose', 'Mathematical Physics'),
(2020, 'Physics', 'Reinhard Genzel', 'Astrophysics'),
(2020, 'Physics', 'Andrea Ghez', 'Astrophysics'),
(2020, 'Biology', 'Emmanuelle Charpentier', 'Biochemistry'),
(2020, 'Chemistry', 'Jennifer Doudna', 'Biochemistry'),
(2020, 'Medicine', 'Harvey J. Alter', 'Virology'),
(2020, 'Medicine', 'Michael Houghton', 'Virology'),
(2020, 'Medicine', 'Charles M. Rice', 'Virology');

select * from noble_price_winner;
where profession not like "P%";