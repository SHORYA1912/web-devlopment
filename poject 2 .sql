CREATE TABLE IF NOT  EXISTS  TABLE_IDK (
  'SNO' INTEGER NOT NULL,
  'ID' INTEGER PRIMARY KEY AUTOINCREMENT,
  'NAME' TEXT NOT NULL,
  'AGE' INTEGER NOT NULL,
  'MARKS' INTEGER NOT NULL,
  'ADDRESS' TEXT NOT NULL
);

INSERT INTO TABLE_IDK (SNO, ID, NAME, AGE, MARKS, ADDRESS) VALUES 
(1, 1, 'Alice', 20, 85, 'NEW YORK'),
(2, 2, 'Bob', 22, 90, 'LOS ANGELES'),
(3, 3, 'Charlie', 19, 78, 'INDIA'),
(4, 4, 'David', 21, 92, 'HOUSTON'),
(5, 5, 'Eve', 20, 88, 'PHOENIX'),
(6, 6, 'Frank', 23, 80, 'PHILADELPHIA'),
(7, 7, 'Grace', 19, 95, 'SAN ANTONIO'),
(8, 8, 'Heidi', 22, 82, 'INDIA'),
(9, 9, 'Ivan', 20, 89, 'DALLAS'),
(10, 10, 'Judy', 21, 91, 'SAN JOSE'),
(11, 11, 'Karl', 19, 77, 'NEW YORK'),
(12, 12, 'Leo', 22, 84, 'JACKSONVILLE'),
(13, 13, 'Mallory', 20, 90, 'FORT WORTH'),
(14, 14, 'Nina', 21, 87, 'INDIA'),
(15, 15, 'Oscar', 23, 79, 'CHARLOTTE'),
(16, 16, 'Peggy', 19, 94, 'NEW YORK'),
(17, 17, 'Quentin', 22, 81, 'INDIANAPOLIS'),
(18, 18, 'Ruth', 20, 88, 'SEATTLE'),
(19, 19, 'Steve', 21, 93, 'INDIA'),
(20, 20, 'Trudy', 23, 80, 'NEW YORK'),
(21, 21, 'Uma', 19, 85, 'INDIA'),
(22, 22, 'Victor', 22, 90, 'DENVER'),
(23, 23, 'Wendy', 20, 78, 'INDIA'),
(24, 24, 'Xavier', 21, 92, 'BOSTON'),
(25, 25, 'Yvonne', 20, 88, 'INDIA'),
(26, 26, 'Zack', 23, 80, 'NEW YORK')
(27, 27, 'Amy', 19, 95, 'INDIA'),
(28, 28, 'Brian', 22, 82, 'INDIANAPOLIS'),
(29, 29, 'Cathy', 20, 89, 'DALLAS'),
(30, 30, 'Dan', 21, 91, 'SAN JOSE'),
(31, 31, 'Ellen', 19, 77, 'NEW YORK'),
(32, 32, 'Fred', 22, 84, 'JACKSONVILLE'),
(33, 33, 'Gina', 20, 90, 'FORT WORTH'),
(34, 34, 'Hank', 21, 87, 'INDIA'),
(35, 35, 'Ivy', 23, 79, 'CHARLOTTE'),
(36, 36, 'Jack', 19, 94, 'NEW YORK'),
(37, 37, 'Karen', 22, 81, 'INDIANAPOLIS'),
(38, 38, 'Leo', 20, 88, 'SEATTLE'),
(39, 39, 'Mona', 21, 93, 'INDIA'),
(40, 40, 'Nate', 23, 80,'NEW YORK')
(41, 41, 'Olivia', 19, 85, 'INDIA'),
(42, 42, 'Paul', 22, 90, 'DENVER'),
(43, 43, 'Quincy', 20, 78, 'INDIA'),
(44, 44, 'Rachel', 21, 92, 'BOSTON'),
(45, 45, 'Sam', 20, 88, 'INDIA'),
(46, 46, 'Tina', 23, 80, 'NEW YORK'),
(47, 47, 'Ursula', 19, 95, 'INDIA'),
(48, 48, 'Vince', 22, 82, 'INDIANAPOLIS'),
(49, 49, 'Walt', 20, 89, 'DALLAS'),
(50, 50, 'Xena', 21, 91,'SAN JOSE');

SELECT * FROM TABLE_IDK;
SELECT NAME, AGE FROM TABLE_IDK WHERE MARKS > 90;
SELECT NAME, ADDRESS FROM TABLE_IDK WHERE AGE < 20;
SELECT NAME, MARKS FROM TABLE_IDK WHERE ADDRESS = 'INDIA';
SELECT NAME, AGE FROM TABLE_IDK WHERE NAME LIKE 'A%';
SELECT NAME, AGE FROM TABLE_IDK WHERE NAME LIKE '%a';
SELECT NAME, AGE FROM TABLE_IDK WHERE NAME LIKE '%a%';
SELECT NAME, AGE FROM TABLE_IDK WHERE NAME LIKE '_a%';

