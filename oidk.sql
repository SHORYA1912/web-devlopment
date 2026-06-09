drop table if exists bookstore;
CREATE table if not exists bookstore(
    title TEXT,
    author TEXT,
    genre TEXT,
    price_range TEXT,
    condition TEXT,
    review REAL
);

insert into bookstore (title, author, genre, price_range, condition, review) values 
('The Silent Patient', 'Alex Michaelides', 'Thriller', '$$', 'New', 4),
('Where the Crawdads Sing', 'Delia Owens', 'Fiction', '$$$', 'Good', 5),
('Educated', 'Tara Westover', 'Memoir', '$', 'Good', 5),
('The Hobbit', 'J.R.R. Tolkien', 'Fantasy', '$$', 'New', 5),
('Becoming', 'Michelle Obama', 'Memoir', '$$$', 'Good', 5),
('Dune', 'Frank Herbert', 'Science Fiction', '$$', 'New', 4),
('The Great Gatsby', 'F. Scott Fitzgerald', 'Classic', '$$$', 'Fair', 4),
('The Road', 'Cormac McCarthy', 'Dystopian', '$$', '', 4),
('Sapiens', 'Yuval Noah Harari', 'Nonfiction', '$$$', 'New', 5),
('The Night Circus', 'Erin Morgenstern', 'Fantasy', '$$', 'Good', 4);

select distinct author 
from bookstore;

select distinct genre
from bookstore;

select * from bookstore
where genre = 'Fantasy';

select * from bookstore
where review >= 4 ;

select * from bookstore
where genre = 'Fantasy' and price_range = '$$' and condition = 'New';

select * from bookstore
where price_range = '$$$';

select * from bookstore
where title like '%the%';

select * from bookstore
where author in ('Alex Michaelides', 'Delia Owens', 'J.R.R. Tolkien');

select * from bookstore
where condition ='' or condition is NULL;

select * from bookstore
order by review desc;