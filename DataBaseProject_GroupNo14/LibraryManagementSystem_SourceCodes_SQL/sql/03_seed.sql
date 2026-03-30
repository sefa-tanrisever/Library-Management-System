-- 03_seed_200_books.sql

BEGIN;

TRUNCATE loan, librarian, member, books, author, publisher, section, permission
RESTART IDENTITY CASCADE;



INSERT INTO permission (permission_name, description) VALUES
('member', 'Standard library member'),
('librarian', 'Library staff'),
('admin', 'System administrator');

INSERT INTO section (section_name) VALUES
('Biography'),
('Business'),
('Children'),
('Classics'),
('Computer Science'),
('Fantasy'),
('History'),
('Literature'),
('Mystery & Thriller'),
('Philosophy'),
('Politics'),
('Psychology'),
('Science'),
('Science Fiction'),
('Self-Help'),
('Young Adult');

INSERT INTO publisher (publisher_name, publisher_country) VALUES
('Ace Books', 'USA'),
('Addison-Wesley', 'USA'),
('Avery', 'USA'),
('Ballantine Books', 'USA'),
('Bantam Books', 'USA'),
('Basic Books', 'USA'),
('Beacon Press', 'USA'),
('Blackwell', 'United Kingdom'),
('Bloomsbury', 'United Kingdom'),
('Cambridge University Press', 'United Kingdom'),
('Crown Business', 'USA'),
('Crown Publishing Group', 'USA'),
('DAW Books', 'USA'),
('Del Rey', 'USA'),
('Dial Press', 'USA'),
('Doubleday', 'USA'),
('Dutton Books', 'USA'),
('Farrar, Straus and Giroux', 'USA'),
('Free Press', 'USA'),
('Gallimard', 'France'),
('Harper', 'USA'),
('Harper Business', 'USA'),
('HarperCollins', 'United Kingdom'),
('Harvard Business Review Press', 'USA'),
('Houghton Mifflin', 'USA'),
('Knopf Canada', 'Canada'),
('Little, Brown and Company', 'USA'),
('MIT Press', 'USA'),
('McClelland & Stewart', 'Canada'),
('McGraw-Hill', 'USA'),
('No Starch Press', 'USA'),
('Norstedts Förlag', 'Sweden'),
('O''Reilly Media', 'USA'),
('Oxford University Press', 'United Kingdom'),
('Pearson', 'United Kingdom'),
('Penguin Books', 'United Kingdom'),
('Penguin Classics', 'United Kingdom'),
('Picador', 'United Kingdom'),
('Pocket Books', 'USA'),
('Prentice Hall', 'USA'),
('Puffin Books', 'United Kingdom'),
('Random House', 'USA'),
('Riverhead Books', 'USA'),
('Schocken Books', 'USA'),
('Scholastic', 'USA'),
('Scribner', 'USA'),
('Simon & Schuster', 'USA'),
('Spiegel & Grau', 'USA'),
('Springer', 'Germany'),
('Tor Books', 'USA'),
('Viking Press', 'USA'),
('Vintage', 'USA'),
('W. W. Norton & Company', 'USA'),
('Wiley', 'USA');

INSERT INTO author (author_name, date_of_birth) VALUES
('Abraham Silberschatz', NULL),
('Adam Smith', '1723-06-16'),
('Agatha Christie', '1890-09-15'),
('Albert Camus', '1913-11-07'),
('Aldous Huxley', '1894-07-26'),
('Alexandre Dumas', '1802-07-24'),
('Andrew Hunt', NULL),
('Andrew S. Tanenbaum', '1944-03-16'),
('Andy Weir', '1972-06-16'),
('Anne Frank', '1929-06-12'),
('Antoine de Saint-Exupéry', '1900-06-29'),
('Aristotle', NULL),
('Arthur Conan Doyle', '1859-05-22'),
('Bram Stoker', '1847-11-08'),
('Brandon Sanderson', '1975-12-19'),
('Brian W. Kernighan', NULL),
('C. S. Lewis', '1898-11-29'),
('Carl Sagan', '1934-11-09'),
('Charles Dickens', '1812-02-07'),
('Charles Duhigg', NULL),
('Charlotte Brontë', '1816-04-21'),
('Christopher M. Bishop', NULL),
('Clayton M. Christensen', '1952-04-06'),
('Cormac McCarthy', '1933-07-20'),
('Dale Carnegie', '1888-11-24'),
('Dan Brown', '1964-06-22'),
('Daniel Kahneman', '1934-03-05'),
('Dante Alighieri', NULL),
('Dashiell Hammett', '1894-05-27'),
('David McCullough', '1933-07-07'),
('Don Norman', '1935-12-25'),
('E. B. White', '1899-07-11'),
('Edward Gibbon', '1737-05-08'),
('Emily Brontë', '1818-07-30'),
('Eric Freeman', NULL),
('Eric Matthes', NULL),
('Eric Ries', NULL),
('Erich Gamma', NULL),
('Ernest Cline', '1972-03-29'),
('Ernest Hemingway', '1899-07-21'),
('F. Scott Fitzgerald', '1896-09-24'),
('Frank Herbert', '1920-10-08'),
('Franz Kafka', '1883-07-03'),
('Friedrich Nietzsche', '1844-10-15'),
('Fyodor Dostoevsky', '1821-11-11'),
('Gabriel García Márquez', '1927-03-06'),
('George Orwell', '1903-06-25'),
('George R. R. Martin', '1948-09-20'),
('Gillian Flynn', '1971-02-24'),
('H. G. Wells', '1866-09-21'),
('Harold Abelson', '1947-04-26'),
('Harper Lee', '1926-04-28'),
('Herman Melville', '1819-08-01'),
('Homer', NULL),
('Howard Zinn', '1922-08-24'),
('Ian Goodfellow', NULL),
('Immanuel Kant', '1724-04-22'),
('Isaac Asimov', '1920-01-02'),
('J. D. Salinger', '1919-01-01'),
('J. K. Rowling', '1965-07-31'),
('J. R. R. Tolkien', '1892-01-03'),
('James Clear', NULL),
('Jane Austen', '1775-12-16'),
('Jared Diamond', '1937-09-10'),
('Jim Collins', NULL),
('John Green', '1977-08-24'),
('John Steinbeck', '1902-02-27'),
('Joseph Heller', '1923-05-01'),
('Joshua Bloch', NULL),
('Karl Marx', '1818-05-05'),
('Khaled Hosseini', '1965-03-04'),
('Kurt Vonnegut', '1922-11-11'),
('Leo Tolstoy', '1828-09-09'),
('Lois Lowry', '1937-03-20'),
('Luciano Ramalho', NULL),
('Marcus Aurelius', '0121-04-26'),
('Margaret Atwood', '1939-11-18'),
('Mark Lutz', NULL),
('Markus Zusak', '1975-06-23'),
('Martin Fowler', '1963-12-18'),
('Martin Heidegger', '1889-09-26'),
('Martin Kleppmann', NULL),
('Mary Shelley', '1797-08-30'),
('Michelle Obama', '1964-01-17'),
('Miguel de Cervantes', '1547-09-29'),
('Neal Stephenson', '1959-10-31'),
('Nelson Mandela', '1918-07-18'),
('Niccolò Machiavelli', '1469-05-03'),
('Orson Scott Card', '1951-08-24'),
('Oscar Wilde', '1854-10-16'),
('Patrick Rothfuss', '1973-06-06'),
('Paulo Coelho', '1947-08-24'),
('Peter Frankopan', NULL),
('Peter Thiel', '1967-10-11'),
('Philip K. Dick', '1928-12-16'),
('Plato', NULL),
('Ray Bradbury', '1920-08-22'),
('Raymond Chandler', '1888-07-23'),
('Richard Dawkins', '1941-03-26'),
('Roald Dahl', '1916-09-13'),
('Robert B. Cialdini', '1945-04-27'),
('Robert C. Martin', '1952-12-05'),
('Robert Louis Stevenson', '1850-11-13'),
('Siddhartha Mukherjee', NULL),
('Stephen Hawking', '1942-01-08'),
('Stephen King', '1947-09-21'),
('Stephen R. Covey', '1932-10-24'),
('Stieg Larsson', '1954-08-15'),
('Stuart Russell', NULL),
('Sun Tzu', NULL),
('Suzanne Collins', '1962-08-10'),
('Tana French', NULL),
('Thomas H. Cormen', NULL),
('Ursula K. Le Guin', '1929-10-21'),
('Victor Hugo', '1802-02-26'),
('Viktor E. Frankl', '1905-03-26'),
('Walter Isaacson', '1952-05-20'),
('William Gibson', '1948-03-17'),
('Yann Martel', '1963-06-25'),
('Yuval Noah Harari', '1976-02-24');

INSERT INTO books (title, author_id, section_id, publisher_id, language, book_status)
VALUES
(
  '1984',
  (SELECT author_id FROM author WHERE author_name='George Orwell' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Literature'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Books'),
  'English',
  'available'
),
(
  'Animal Farm',
  (SELECT author_id FROM author WHERE author_name='George Orwell' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Literature'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Books'),
  'English',
  'available'
),
(
  'Brave New World',
  (SELECT author_id FROM author WHERE author_name='Aldous Huxley' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Science Fiction'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='HarperCollins'),
  'English',
  'available'
),
(
  'Fahrenheit 451',
  (SELECT author_id FROM author WHERE author_name='Ray Bradbury' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Science Fiction'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Simon & Schuster'),
  'English',
  'available'
),
(
  'The Handmaid''s Tale',
  (SELECT author_id FROM author WHERE author_name='Margaret Atwood' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Science Fiction'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='McClelland & Stewart'),
  'English',
  'available'
),
(
  'The Road',
  (SELECT author_id FROM author WHERE author_name='Cormac McCarthy' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Literature'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Vintage'),
  'English',
  'available'
),
(
  'To Kill a Mockingbird',
  (SELECT author_id FROM author WHERE author_name='Harper Lee' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Literature'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='HarperCollins'),
  'English',
  'available'
),
(
  'The Great Gatsby',
  (SELECT author_id FROM author WHERE author_name='F. Scott Fitzgerald' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Literature'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Scribner'),
  'English',
  'available'
),
(
  'The Catcher in the Rye',
  (SELECT author_id FROM author WHERE author_name='J. D. Salinger' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Literature'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Little, Brown and Company'),
  'English',
  'available'
),
(
  'Of Mice and Men',
  (SELECT author_id FROM author WHERE author_name='John Steinbeck' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Literature'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Books'),
  'English',
  'available'
),
(
  'The Grapes of Wrath',
  (SELECT author_id FROM author WHERE author_name='John Steinbeck' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Literature'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Books'),
  'English',
  'available'
),
(
  'East of Eden',
  (SELECT author_id FROM author WHERE author_name='John Steinbeck' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Literature'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Books'),
  'English',
  'available'
),
(
  'Moby-Dick',
  (SELECT author_id FROM author WHERE author_name='Herman Melville' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Classics'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='HarperCollins'),
  'English',
  'available'
),
(
  'Pride and Prejudice',
  (SELECT author_id FROM author WHERE author_name='Jane Austen' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Classics'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Classics'),
  'English',
  'available'
),
(
  'Sense and Sensibility',
  (SELECT author_id FROM author WHERE author_name='Jane Austen' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Classics'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Classics'),
  'English',
  'available'
),
(
  'Emma',
  (SELECT author_id FROM author WHERE author_name='Jane Austen' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Classics'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Classics'),
  'English',
  'available'
),
(
  'Jane Eyre',
  (SELECT author_id FROM author WHERE author_name='Charlotte Brontë' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Classics'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Classics'),
  'English',
  'available'
),
(
  'Wuthering Heights',
  (SELECT author_id FROM author WHERE author_name='Emily Brontë' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Classics'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Classics'),
  'English',
  'available'
),
(
  'Great Expectations',
  (SELECT author_id FROM author WHERE author_name='Charles Dickens' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Classics'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Classics'),
  'English',
  'available'
),
(
  'A Tale of Two Cities',
  (SELECT author_id FROM author WHERE author_name='Charles Dickens' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Classics'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Classics'),
  'English',
  'available'
),
(
  'Oliver Twist',
  (SELECT author_id FROM author WHERE author_name='Charles Dickens' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Classics'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Classics'),
  'English',
  'available'
),
(
  'David Copperfield',
  (SELECT author_id FROM author WHERE author_name='Charles Dickens' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Classics'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Classics'),
  'English',
  'available'
),
(
  'Les Misérables',
  (SELECT author_id FROM author WHERE author_name='Victor Hugo' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Classics'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Oxford University Press'),
  'French',
  'available'
),
(
  'The Hunchback of Notre-Dame',
  (SELECT author_id FROM author WHERE author_name='Victor Hugo' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Classics'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Oxford University Press'),
  'French',
  'available'
),
(
  'The Count of Monte Cristo',
  (SELECT author_id FROM author WHERE author_name='Alexandre Dumas' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Classics'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Classics'),
  'French',
  'available'
),
(
  'The Three Musketeers',
  (SELECT author_id FROM author WHERE author_name='Alexandre Dumas' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Classics'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Classics'),
  'French',
  'available'
),
(
  'Crime and Punishment',
  (SELECT author_id FROM author WHERE author_name='Fyodor Dostoevsky' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Classics'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Vintage'),
  'Russian',
  'available'
),
(
  'The Brothers Karamazov',
  (SELECT author_id FROM author WHERE author_name='Fyodor Dostoevsky' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Classics'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Vintage'),
  'Russian',
  'available'
),
(
  'The Idiot',
  (SELECT author_id FROM author WHERE author_name='Fyodor Dostoevsky' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Classics'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Vintage'),
  'Russian',
  'available'
),
(
  'War and Peace',
  (SELECT author_id FROM author WHERE author_name='Leo Tolstoy' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Classics'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Classics'),
  'Russian',
  'available'
),
(
  'Anna Karenina',
  (SELECT author_id FROM author WHERE author_name='Leo Tolstoy' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Classics'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Classics'),
  'Russian',
  'available'
),
(
  'The Picture of Dorian Gray',
  (SELECT author_id FROM author WHERE author_name='Oscar Wilde' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Classics'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Classics'),
  'English',
  'available'
),
(
  'Dracula',
  (SELECT author_id FROM author WHERE author_name='Bram Stoker' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Classics'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Classics'),
  'English',
  'available'
),
(
  'Frankenstein',
  (SELECT author_id FROM author WHERE author_name='Mary Shelley' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Classics'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Classics'),
  'English',
  'available'
),
(
  'The Strange Case of Dr Jekyll and Mr Hyde',
  (SELECT author_id FROM author WHERE author_name='Robert Louis Stevenson' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Classics'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Classics'),
  'English',
  'available'
),
(
  'The War of the Worlds',
  (SELECT author_id FROM author WHERE author_name='H. G. Wells' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Science Fiction'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Classics'),
  'English',
  'available'
),
(
  'The Time Machine',
  (SELECT author_id FROM author WHERE author_name='H. G. Wells' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Science Fiction'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Classics'),
  'English',
  'available'
),
(
  'The Invisible Man',
  (SELECT author_id FROM author WHERE author_name='H. G. Wells' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Science Fiction'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Classics'),
  'English',
  'available'
),
(
  'The Odyssey',
  (SELECT author_id FROM author WHERE author_name='Homer' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Classics'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Oxford University Press'),
  'Greek',
  'available'
),
(
  'The Iliad',
  (SELECT author_id FROM author WHERE author_name='Homer' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Classics'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Oxford University Press'),
  'Greek',
  'available'
),
(
  'Don Quixote',
  (SELECT author_id FROM author WHERE author_name='Miguel de Cervantes' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Classics'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Classics'),
  'Spanish',
  'available'
),
(
  'The Divine Comedy',
  (SELECT author_id FROM author WHERE author_name='Dante Alighieri' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Classics'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Oxford University Press'),
  'Italian',
  'available'
),
(
  'The Stranger',
  (SELECT author_id FROM author WHERE author_name='Albert Camus' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Literature'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Vintage'),
  'French',
  'available'
),
(
  'The Plague',
  (SELECT author_id FROM author WHERE author_name='Albert Camus' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Literature'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Vintage'),
  'French',
  'available'
),
(
  'The Metamorphosis',
  (SELECT author_id FROM author WHERE author_name='Franz Kafka' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Literature'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Schocken Books'),
  'German',
  'available'
),
(
  'The Trial',
  (SELECT author_id FROM author WHERE author_name='Franz Kafka' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Literature'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Schocken Books'),
  'German',
  'available'
),
(
  'One Hundred Years of Solitude',
  (SELECT author_id FROM author WHERE author_name='Gabriel García Márquez' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Literature'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Books'),
  'Spanish',
  'available'
),
(
  'Love in the Time of Cholera',
  (SELECT author_id FROM author WHERE author_name='Gabriel García Márquez' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Literature'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Books'),
  'Spanish',
  'available'
),
(
  'The Old Man and the Sea',
  (SELECT author_id FROM author WHERE author_name='Ernest Hemingway' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Literature'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Scribner'),
  'English',
  'available'
),
(
  'For Whom the Bell Tolls',
  (SELECT author_id FROM author WHERE author_name='Ernest Hemingway' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Literature'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Scribner'),
  'English',
  'available'
),
(
  'The Sun Also Rises',
  (SELECT author_id FROM author WHERE author_name='Ernest Hemingway' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Literature'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Scribner'),
  'English',
  'available'
),
(
  'Slaughterhouse-Five',
  (SELECT author_id FROM author WHERE author_name='Kurt Vonnegut' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Science Fiction'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Dial Press'),
  'English',
  'available'
),
(
  'Cat''s Cradle',
  (SELECT author_id FROM author WHERE author_name='Kurt Vonnegut' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Science Fiction'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Dial Press'),
  'English',
  'available'
),
(
  'Catch-22',
  (SELECT author_id FROM author WHERE author_name='Joseph Heller' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Literature'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Simon & Schuster'),
  'English',
  'available'
),
(
  'The Lord of the Rings: The Fellowship of the Ring',
  (SELECT author_id FROM author WHERE author_name='J. R. R. Tolkien' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='HarperCollins'),
  'English',
  'available'
),
(
  'The Lord of the Rings: The Two Towers',
  (SELECT author_id FROM author WHERE author_name='J. R. R. Tolkien' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='HarperCollins'),
  'English',
  'available'
),
(
  'The Lord of the Rings: The Return of the King',
  (SELECT author_id FROM author WHERE author_name='J. R. R. Tolkien' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='HarperCollins'),
  'English',
  'available'
),
(
  'The Hobbit',
  (SELECT author_id FROM author WHERE author_name='J. R. R. Tolkien' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='HarperCollins'),
  'English',
  'available'
),
(
  'The Silmarillion',
  (SELECT author_id FROM author WHERE author_name='J. R. R. Tolkien' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='HarperCollins'),
  'English',
  'available'
),
(
  'Harry Potter and the Philosopher''s Stone',
  (SELECT author_id FROM author WHERE author_name='J. K. Rowling' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Bloomsbury'),
  'English',
  'available'
),
(
  'Harry Potter and the Chamber of Secrets',
  (SELECT author_id FROM author WHERE author_name='J. K. Rowling' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Bloomsbury'),
  'English',
  'available'
),
(
  'Harry Potter and the Prisoner of Azkaban',
  (SELECT author_id FROM author WHERE author_name='J. K. Rowling' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Bloomsbury'),
  'English',
  'available'
),
(
  'Harry Potter and the Goblet of Fire',
  (SELECT author_id FROM author WHERE author_name='J. K. Rowling' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Bloomsbury'),
  'English',
  'available'
),
(
  'Harry Potter and the Order of the Phoenix',
  (SELECT author_id FROM author WHERE author_name='J. K. Rowling' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Bloomsbury'),
  'English',
  'available'
),
(
  'Harry Potter and the Half-Blood Prince',
  (SELECT author_id FROM author WHERE author_name='J. K. Rowling' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Bloomsbury'),
  'English',
  'available'
),
(
  'Harry Potter and the Deathly Hallows',
  (SELECT author_id FROM author WHERE author_name='J. K. Rowling' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Bloomsbury'),
  'English',
  'available'
),
(
  'A Game of Thrones',
  (SELECT author_id FROM author WHERE author_name='George R. R. Martin' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Bantam Books'),
  'English',
  'available'
),
(
  'A Clash of Kings',
  (SELECT author_id FROM author WHERE author_name='George R. R. Martin' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Bantam Books'),
  'English',
  'available'
),
(
  'A Storm of Swords',
  (SELECT author_id FROM author WHERE author_name='George R. R. Martin' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Bantam Books'),
  'English',
  'available'
),
(
  'A Feast for Crows',
  (SELECT author_id FROM author WHERE author_name='George R. R. Martin' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Bantam Books'),
  'English',
  'available'
),
(
  'A Dance with Dragons',
  (SELECT author_id FROM author WHERE author_name='George R. R. Martin' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Bantam Books'),
  'English',
  'available'
),
(
  'The Name of the Wind',
  (SELECT author_id FROM author WHERE author_name='Patrick Rothfuss' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='DAW Books'),
  'English',
  'available'
),
(
  'The Wise Man''s Fear',
  (SELECT author_id FROM author WHERE author_name='Patrick Rothfuss' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='DAW Books'),
  'English',
  'available'
),
(
  'Mistborn: The Final Empire',
  (SELECT author_id FROM author WHERE author_name='Brandon Sanderson' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Tor Books'),
  'English',
  'available'
),
(
  'The Well of Ascension',
  (SELECT author_id FROM author WHERE author_name='Brandon Sanderson' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Tor Books'),
  'English',
  'available'
),
(
  'The Hero of Ages',
  (SELECT author_id FROM author WHERE author_name='Brandon Sanderson' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Tor Books'),
  'English',
  'available'
),
(
  'The Way of Kings',
  (SELECT author_id FROM author WHERE author_name='Brandon Sanderson' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Tor Books'),
  'English',
  'available'
),
(
  'Words of Radiance',
  (SELECT author_id FROM author WHERE author_name='Brandon Sanderson' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Tor Books'),
  'English',
  'available'
),
(
  'Oathbringer',
  (SELECT author_id FROM author WHERE author_name='Brandon Sanderson' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Tor Books'),
  'English',
  'available'
),
(
  'Rhythm of War',
  (SELECT author_id FROM author WHERE author_name='Brandon Sanderson' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Tor Books'),
  'English',
  'available'
),
(
  'Dune',
  (SELECT author_id FROM author WHERE author_name='Frank Herbert' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Science Fiction'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Ace Books'),
  'English',
  'available'
),
(
  'Dune Messiah',
  (SELECT author_id FROM author WHERE author_name='Frank Herbert' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Science Fiction'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Ace Books'),
  'English',
  'available'
),
(
  'Children of Dune',
  (SELECT author_id FROM author WHERE author_name='Frank Herbert' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Science Fiction'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Ace Books'),
  'English',
  'available'
),
(
  'Foundation',
  (SELECT author_id FROM author WHERE author_name='Isaac Asimov' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Science Fiction'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='HarperCollins'),
  'English',
  'available'
),
(
  'Foundation and Empire',
  (SELECT author_id FROM author WHERE author_name='Isaac Asimov' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Science Fiction'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='HarperCollins'),
  'English',
  'available'
),
(
  'Second Foundation',
  (SELECT author_id FROM author WHERE author_name='Isaac Asimov' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Science Fiction'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='HarperCollins'),
  'English',
  'available'
),
(
  'I, Robot',
  (SELECT author_id FROM author WHERE author_name='Isaac Asimov' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Science Fiction'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Bantam Books'),
  'English',
  'available'
),
(
  'Do Androids Dream of Electric Sheep?',
  (SELECT author_id FROM author WHERE author_name='Philip K. Dick' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Science Fiction'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Del Rey'),
  'English',
  'available'
),
(
  'Ubik',
  (SELECT author_id FROM author WHERE author_name='Philip K. Dick' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Science Fiction'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Vintage'),
  'English',
  'available'
),
(
  'Neuromancer',
  (SELECT author_id FROM author WHERE author_name='William Gibson' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Science Fiction'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Ace Books'),
  'English',
  'available'
),
(
  'Snow Crash',
  (SELECT author_id FROM author WHERE author_name='Neal Stephenson' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Science Fiction'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Bantam Books'),
  'English',
  'available'
),
(
  'Ender''s Game',
  (SELECT author_id FROM author WHERE author_name='Orson Scott Card' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Science Fiction'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Tor Books'),
  'English',
  'available'
),
(
  'Speaker for the Dead',
  (SELECT author_id FROM author WHERE author_name='Orson Scott Card' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Science Fiction'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Tor Books'),
  'English',
  'available'
),
(
  'The Left Hand of Darkness',
  (SELECT author_id FROM author WHERE author_name='Ursula K. Le Guin' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Science Fiction'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Ace Books'),
  'English',
  'available'
),
(
  'The Dispossessed',
  (SELECT author_id FROM author WHERE author_name='Ursula K. Le Guin' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Science Fiction'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='HarperCollins'),
  'English',
  'available'
),
(
  'The Martian',
  (SELECT author_id FROM author WHERE author_name='Andy Weir' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Science Fiction'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Crown Publishing Group'),
  'English',
  'available'
),
(
  'Project Hail Mary',
  (SELECT author_id FROM author WHERE author_name='Andy Weir' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Science Fiction'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Ballantine Books'),
  'English',
  'available'
),
(
  'Ready Player One',
  (SELECT author_id FROM author WHERE author_name='Ernest Cline' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Science Fiction'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Crown Publishing Group'),
  'English',
  'available'
),
(
  'The Hunger Games',
  (SELECT author_id FROM author WHERE author_name='Suzanne Collins' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Young Adult'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Scholastic'),
  'English',
  'available'
),
(
  'Catching Fire',
  (SELECT author_id FROM author WHERE author_name='Suzanne Collins' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Young Adult'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Scholastic'),
  'English',
  'available'
),
(
  'Mockingjay',
  (SELECT author_id FROM author WHERE author_name='Suzanne Collins' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Young Adult'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Scholastic'),
  'English',
  'available'
),
(
  'The Fault in Our Stars',
  (SELECT author_id FROM author WHERE author_name='John Green' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Young Adult'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Dutton Books'),
  'English',
  'available'
),
(
  'The Book Thief',
  (SELECT author_id FROM author WHERE author_name='Markus Zusak' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Literature'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Picador'),
  'English',
  'available'
),
(
  'The Alchemist',
  (SELECT author_id FROM author WHERE author_name='Paulo Coelho' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Literature'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='HarperCollins'),
  'Portuguese',
  'available'
),
(
  'The Kite Runner',
  (SELECT author_id FROM author WHERE author_name='Khaled Hosseini' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Literature'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Riverhead Books'),
  'English',
  'available'
),
(
  'A Thousand Splendid Suns',
  (SELECT author_id FROM author WHERE author_name='Khaled Hosseini' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Literature'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Riverhead Books'),
  'English',
  'available'
),
(
  'Life of Pi',
  (SELECT author_id FROM author WHERE author_name='Yann Martel' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Literature'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Knopf Canada'),
  'English',
  'available'
),
(
  'The Girl with the Dragon Tattoo',
  (SELECT author_id FROM author WHERE author_name='Stieg Larsson' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Mystery & Thriller'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Norstedts Förlag'),
  'Swedish',
  'available'
),
(
  'Gone Girl',
  (SELECT author_id FROM author WHERE author_name='Gillian Flynn' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Mystery & Thriller'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Crown Publishing Group'),
  'English',
  'available'
),
(
  'The Da Vinci Code',
  (SELECT author_id FROM author WHERE author_name='Dan Brown' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Mystery & Thriller'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Doubleday'),
  'English',
  'available'
),
(
  'Angels & Demons',
  (SELECT author_id FROM author WHERE author_name='Dan Brown' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Mystery & Thriller'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Pocket Books'),
  'English',
  'available'
),
(
  'The Lost Symbol',
  (SELECT author_id FROM author WHERE author_name='Dan Brown' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Mystery & Thriller'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Doubleday'),
  'English',
  'available'
),
(
  'In the Woods',
  (SELECT author_id FROM author WHERE author_name='Tana French' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Mystery & Thriller'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Viking Press'),
  'English',
  'available'
),
(
  'The Big Sleep',
  (SELECT author_id FROM author WHERE author_name='Raymond Chandler' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Mystery & Thriller'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Vintage'),
  'English',
  'available'
),
(
  'The Maltese Falcon',
  (SELECT author_id FROM author WHERE author_name='Dashiell Hammett' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Mystery & Thriller'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Vintage'),
  'English',
  'available'
),
(
  'The Hound of the Baskervilles',
  (SELECT author_id FROM author WHERE author_name='Arthur Conan Doyle' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Mystery & Thriller'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Classics'),
  'English',
  'available'
),
(
  'A Study in Scarlet',
  (SELECT author_id FROM author WHERE author_name='Arthur Conan Doyle' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Mystery & Thriller'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Classics'),
  'English',
  'available'
),
(
  'Murder on the Orient Express',
  (SELECT author_id FROM author WHERE author_name='Agatha Christie' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Mystery & Thriller'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='HarperCollins'),
  'English',
  'available'
),
(
  'And Then There Were None',
  (SELECT author_id FROM author WHERE author_name='Agatha Christie' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Mystery & Thriller'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='HarperCollins'),
  'English',
  'available'
),
(
  'The Murder of Roger Ackroyd',
  (SELECT author_id FROM author WHERE author_name='Agatha Christie' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Mystery & Thriller'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='HarperCollins'),
  'English',
  'available'
),
(
  'The ABC Murders',
  (SELECT author_id FROM author WHERE author_name='Agatha Christie' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Mystery & Thriller'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='HarperCollins'),
  'English',
  'available'
),
(
  'The Mysterious Affair at Styles',
  (SELECT author_id FROM author WHERE author_name='Agatha Christie' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Mystery & Thriller'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='HarperCollins'),
  'English',
  'available'
),
(
  'The Shining',
  (SELECT author_id FROM author WHERE author_name='Stephen King' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Mystery & Thriller'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Scribner'),
  'English',
  'available'
),
(
  'It',
  (SELECT author_id FROM author WHERE author_name='Stephen King' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Mystery & Thriller'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Scribner'),
  'English',
  'available'
),
(
  'Misery',
  (SELECT author_id FROM author WHERE author_name='Stephen King' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Mystery & Thriller'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Scribner'),
  'English',
  'available'
),
(
  'Carrie',
  (SELECT author_id FROM author WHERE author_name='Stephen King' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Mystery & Thriller'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Doubleday'),
  'English',
  'available'
),
(
  'The Outsider',
  (SELECT author_id FROM author WHERE author_name='Stephen King' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Mystery & Thriller'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Scribner'),
  'English',
  'available'
),
(
  'The Stand',
  (SELECT author_id FROM author WHERE author_name='Stephen King' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Science Fiction'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Doubleday'),
  'English',
  'available'
),
(
  'The Giver',
  (SELECT author_id FROM author WHERE author_name='Lois Lowry' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Young Adult'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Houghton Mifflin'),
  'English',
  'available'
),
(
  'The Chronicles of Narnia: The Lion, the Witch and the Wardrobe',
  (SELECT author_id FROM author WHERE author_name='C. S. Lewis' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='HarperCollins'),
  'English',
  'available'
),
(
  'The Chronicles of Narnia: Prince Caspian',
  (SELECT author_id FROM author WHERE author_name='C. S. Lewis' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='HarperCollins'),
  'English',
  'available'
),
(
  'The Chronicles of Narnia: The Voyage of the Dawn Treader',
  (SELECT author_id FROM author WHERE author_name='C. S. Lewis' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='HarperCollins'),
  'English',
  'available'
),
(
  'The Chronicles of Narnia: The Silver Chair',
  (SELECT author_id FROM author WHERE author_name='C. S. Lewis' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='HarperCollins'),
  'English',
  'available'
),
(
  'The Chronicles of Narnia: The Horse and His Boy',
  (SELECT author_id FROM author WHERE author_name='C. S. Lewis' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='HarperCollins'),
  'English',
  'available'
),
(
  'The Chronicles of Narnia: The Magician''s Nephew',
  (SELECT author_id FROM author WHERE author_name='C. S. Lewis' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='HarperCollins'),
  'English',
  'available'
),
(
  'The Chronicles of Narnia: The Last Battle',
  (SELECT author_id FROM author WHERE author_name='C. S. Lewis' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Fantasy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='HarperCollins'),
  'English',
  'available'
),
(
  'The Little Prince',
  (SELECT author_id FROM author WHERE author_name='Antoine de Saint-Exupéry' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Children'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Gallimard'),
  'French',
  'available'
),
(
  'Charlotte''s Web',
  (SELECT author_id FROM author WHERE author_name='E. B. White' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Children'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='HarperCollins'),
  'English',
  'available'
),
(
  'Matilda',
  (SELECT author_id FROM author WHERE author_name='Roald Dahl' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Children'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Puffin Books'),
  'English',
  'available'
),
(
  'Charlie and the Chocolate Factory',
  (SELECT author_id FROM author WHERE author_name='Roald Dahl' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Children'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Puffin Books'),
  'English',
  'available'
),
(
  'The BFG',
  (SELECT author_id FROM author WHERE author_name='Roald Dahl' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Children'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Puffin Books'),
  'English',
  'available'
),
(
  'A Brief History of Time',
  (SELECT author_id FROM author WHERE author_name='Stephen Hawking' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Science'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Bantam Books'),
  'English',
  'available'
),
(
  'Cosmos',
  (SELECT author_id FROM author WHERE author_name='Carl Sagan' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Science'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Random House'),
  'English',
  'available'
),
(
  'The Selfish Gene',
  (SELECT author_id FROM author WHERE author_name='Richard Dawkins' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Science'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Oxford University Press'),
  'English',
  'available'
),
(
  'The Gene: An Intimate History',
  (SELECT author_id FROM author WHERE author_name='Siddhartha Mukherjee' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Science'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Scribner'),
  'English',
  'available'
),
(
  'Sapiens: A Brief History of Humankind',
  (SELECT author_id FROM author WHERE author_name='Yuval Noah Harari' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='History'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Harper'),
  'English',
  'available'
),
(
  'Homo Deus',
  (SELECT author_id FROM author WHERE author_name='Yuval Noah Harari' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='History'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Harper'),
  'English',
  'available'
),
(
  '21 Lessons for the 21st Century',
  (SELECT author_id FROM author WHERE author_name='Yuval Noah Harari' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='History'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Spiegel & Grau'),
  'English',
  'available'
),
(
  'Guns, Germs, and Steel',
  (SELECT author_id FROM author WHERE author_name='Jared Diamond' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='History'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='W. W. Norton & Company'),
  'English',
  'available'
),
(
  'The Silk Roads',
  (SELECT author_id FROM author WHERE author_name='Peter Frankopan' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='History'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Bloomsbury'),
  'English',
  'available'
),
(
  'A People''s History of the United States',
  (SELECT author_id FROM author WHERE author_name='Howard Zinn' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='History'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='HarperCollins'),
  'English',
  'available'
),
(
  'The History of the Decline and Fall of the Roman Empire',
  (SELECT author_id FROM author WHERE author_name='Edward Gibbon' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='History'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Classics'),
  'English',
  'available'
),
(
  'The Diary of a Young Girl',
  (SELECT author_id FROM author WHERE author_name='Anne Frank' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Biography'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Books'),
  'English',
  'available'
),
(
  'Long Walk to Freedom',
  (SELECT author_id FROM author WHERE author_name='Nelson Mandela' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Biography'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Little, Brown and Company'),
  'English',
  'available'
),
(
  'Steve Jobs',
  (SELECT author_id FROM author WHERE author_name='Walter Isaacson' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Biography'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Simon & Schuster'),
  'English',
  'available'
),
(
  'Einstein: His Life and Universe',
  (SELECT author_id FROM author WHERE author_name='Walter Isaacson' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Biography'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Simon & Schuster'),
  'English',
  'available'
),
(
  'Becoming',
  (SELECT author_id FROM author WHERE author_name='Michelle Obama' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Biography'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Crown Publishing Group'),
  'English',
  'available'
),
(
  'The Wright Brothers',
  (SELECT author_id FROM author WHERE author_name='David McCullough' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Biography'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Simon & Schuster'),
  'English',
  'available'
),
(
  'Thinking, Fast and Slow',
  (SELECT author_id FROM author WHERE author_name='Daniel Kahneman' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Psychology'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Farrar, Straus and Giroux'),
  'English',
  'available'
),
(
  'Man''s Search for Meaning',
  (SELECT author_id FROM author WHERE author_name='Viktor E. Frankl' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Psychology'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Beacon Press'),
  'English',
  'available'
),
(
  'Influence: The Psychology of Persuasion',
  (SELECT author_id FROM author WHERE author_name='Robert B. Cialdini' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Psychology'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Harper Business'),
  'English',
  'available'
),
(
  'The Power of Habit',
  (SELECT author_id FROM author WHERE author_name='Charles Duhigg' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Psychology'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Random House'),
  'English',
  'available'
),
(
  'Atomic Habits',
  (SELECT author_id FROM author WHERE author_name='James Clear' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Self-Help'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Avery'),
  'English',
  'available'
),
(
  'The 7 Habits of Highly Effective People',
  (SELECT author_id FROM author WHERE author_name='Stephen R. Covey' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Self-Help'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Free Press'),
  'English',
  'available'
),
(
  'How to Win Friends and Influence People',
  (SELECT author_id FROM author WHERE author_name='Dale Carnegie' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Self-Help'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Simon & Schuster'),
  'English',
  'available'
),
(
  'Meditations',
  (SELECT author_id FROM author WHERE author_name='Marcus Aurelius' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Philosophy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Classics'),
  'Greek',
  'available'
),
(
  'The Republic',
  (SELECT author_id FROM author WHERE author_name='Plato' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Philosophy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Oxford University Press'),
  'Greek',
  'available'
),
(
  'Nicomachean Ethics',
  (SELECT author_id FROM author WHERE author_name='Aristotle' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Philosophy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Oxford University Press'),
  'Greek',
  'available'
),
(
  'Beyond Good and Evil',
  (SELECT author_id FROM author WHERE author_name='Friedrich Nietzsche' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Philosophy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Classics'),
  'German',
  'available'
),
(
  'Thus Spoke Zarathustra',
  (SELECT author_id FROM author WHERE author_name='Friedrich Nietzsche' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Philosophy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Classics'),
  'German',
  'available'
),
(
  'Critique of Pure Reason',
  (SELECT author_id FROM author WHERE author_name='Immanuel Kant' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Philosophy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Cambridge University Press'),
  'German',
  'available'
),
(
  'Being and Time',
  (SELECT author_id FROM author WHERE author_name='Martin Heidegger' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Philosophy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Blackwell'),
  'German',
  'available'
),
(
  'The Prince',
  (SELECT author_id FROM author WHERE author_name='Niccolò Machiavelli' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Philosophy'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Classics'),
  'Italian',
  'available'
),
(
  'The Art of War',
  (SELECT author_id FROM author WHERE author_name='Sun Tzu' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='History'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Oxford University Press'),
  'Chinese',
  'available'
),
(
  'The Communist Manifesto',
  (SELECT author_id FROM author WHERE author_name='Karl Marx' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Politics'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Penguin Classics'),
  'German',
  'available'
),
(
  'The Wealth of Nations',
  (SELECT author_id FROM author WHERE author_name='Adam Smith' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Business'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Oxford University Press'),
  'English',
  'available'
),
(
  'The Lean Startup',
  (SELECT author_id FROM author WHERE author_name='Eric Ries' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Business'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Crown Business'),
  'English',
  'available'
),
(
  'Good to Great',
  (SELECT author_id FROM author WHERE author_name='Jim Collins' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Business'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Harper Business'),
  'English',
  'available'
),
(
  'Zero to One',
  (SELECT author_id FROM author WHERE author_name='Peter Thiel' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Business'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Crown Business'),
  'English',
  'available'
),
(
  'The Innovator''s Dilemma',
  (SELECT author_id FROM author WHERE author_name='Clayton M. Christensen' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Business'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Harvard Business Review Press'),
  'English',
  'available'
),
(
  'The Design of Everyday Things',
  (SELECT author_id FROM author WHERE author_name='Don Norman' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Computer Science'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Basic Books'),
  'English',
  'available'
),
(
  'Clean Code',
  (SELECT author_id FROM author WHERE author_name='Robert C. Martin' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Computer Science'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Prentice Hall'),
  'English',
  'available'
),
(
  'The Pragmatic Programmer',
  (SELECT author_id FROM author WHERE author_name='Andrew Hunt' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Computer Science'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Addison-Wesley'),
  'English',
  'available'
),
(
  'Introduction to Algorithms',
  (SELECT author_id FROM author WHERE author_name='Thomas H. Cormen' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Computer Science'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='MIT Press'),
  'English',
  'available'
),
(
  'Design Patterns: Elements of Reusable Object-Oriented Software',
  (SELECT author_id FROM author WHERE author_name='Erich Gamma' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Computer Science'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Addison-Wesley'),
  'English',
  'available'
),
(
  'Artificial Intelligence: A Modern Approach',
  (SELECT author_id FROM author WHERE author_name='Stuart Russell' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Computer Science'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Pearson'),
  'English',
  'available'
),
(
  'Deep Learning',
  (SELECT author_id FROM author WHERE author_name='Ian Goodfellow' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Computer Science'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='MIT Press'),
  'English',
  'available'
),
(
  'Pattern Recognition and Machine Learning',
  (SELECT author_id FROM author WHERE author_name='Christopher M. Bishop' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Computer Science'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Springer'),
  'English',
  'available'
),
(
  'The C Programming Language',
  (SELECT author_id FROM author WHERE author_name='Brian W. Kernighan' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Computer Science'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Prentice Hall'),
  'English',
  'available'
),
(
  'Structure and Interpretation of Computer Programs',
  (SELECT author_id FROM author WHERE author_name='Harold Abelson' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Computer Science'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='MIT Press'),
  'English',
  'available'
),
(
  'Operating System Concepts',
  (SELECT author_id FROM author WHERE author_name='Abraham Silberschatz' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Computer Science'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Wiley'),
  'English',
  'available'
),
(
  'Computer Networks',
  (SELECT author_id FROM author WHERE author_name='Andrew S. Tanenbaum' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Computer Science'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Pearson'),
  'English',
  'available'
),
(
  'Database System Concepts',
  (SELECT author_id FROM author WHERE author_name='Abraham Silberschatz' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Computer Science'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='McGraw-Hill'),
  'English',
  'available'
),
(
  'Designing Data-Intensive Applications',
  (SELECT author_id FROM author WHERE author_name='Martin Kleppmann' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Computer Science'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='O''Reilly Media'),
  'English',
  'available'
),
(
  'Python Crash Course',
  (SELECT author_id FROM author WHERE author_name='Eric Matthes' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Computer Science'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='No Starch Press'),
  'English',
  'available'
),
(
  'Fluent Python',
  (SELECT author_id FROM author WHERE author_name='Luciano Ramalho' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Computer Science'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='O''Reilly Media'),
  'English',
  'available'
),
(
  'Learning Python',
  (SELECT author_id FROM author WHERE author_name='Mark Lutz' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Computer Science'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='O''Reilly Media'),
  'English',
  'available'
),
(
  'Effective Java',
  (SELECT author_id FROM author WHERE author_name='Joshua Bloch' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Computer Science'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Addison-Wesley'),
  'English',
  'available'
),
(
  'Refactoring',
  (SELECT author_id FROM author WHERE author_name='Martin Fowler' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Computer Science'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='Addison-Wesley'),
  'English',
  'available'
),
(
  'Head First Design Patterns',
  (SELECT author_id FROM author WHERE author_name='Eric Freeman' LIMIT 1),
  (SELECT section_id FROM section WHERE section_name='Computer Science'),
  (SELECT publisher_id FROM publisher WHERE publisher_name='O''Reilly Media'),
  'English',
  'available'
);

INSERT INTO member (first_name, last_name, phone_number, email, password, permission_id)
VALUES
('Ali', 'Yılmaz', '0555-111-2233', 'ali@example.com', '1234',
 (SELECT permission_id FROM permission WHERE permission_name='member')
),
('Ayşe', 'Demir', '0555-333-4455', 'ayse@example.com', '1234',
 (SELECT permission_id FROM permission WHERE permission_name='member')
),
('Mehmet', 'Kaya',   '0555-111-3344', 'mehmet.kaya@example.com',   '1234',
 (SELECT permission_id FROM permission WHERE permission_name='member')
),
('Zeynep', 'Şahin',  '0555-111-5566', 'zeynep.sahin@example.com',  '1234',
 (SELECT permission_id FROM permission WHERE permission_name='member')
),
('Eren', 'Koç',      '0555-222-1122', 'eren.koc@example.com',      '1234',
 (SELECT permission_id FROM permission WHERE permission_name='member')
),
('Elif', 'Acar',     '0555-222-3344', 'elif.acar@example.com',     '1234',
 (SELECT permission_id FROM permission WHERE permission_name='member')
),
('Mert', 'Yıldız',   '0555-222-5566', 'mert.yildiz@example.com',   '1234',
 (SELECT permission_id FROM permission WHERE permission_name='member')
),
('Buse', 'Çelik',    '0555-333-1122', 'buse.celik@example.com',    '1234',
 (SELECT permission_id FROM permission WHERE permission_name='member')
),
('Can', 'Arslan',    '0555-333-3344', 'can.arslan@example.com',    '1234',
 (SELECT permission_id FROM permission WHERE permission_name='member')
),
('Selin', 'Öztürk',  '0555-333-5566', 'selin.ozturk@example.com',  '1234',
 (SELECT permission_id FROM permission WHERE permission_name='member')
);

INSERT INTO librarian (name, phone_number, email, password, permission_id)
VALUES
('Library Staff 1', '0555-000-0000', 'staff1@library.com', '1234',
 (SELECT permission_id FROM permission WHERE permission_name='librarian')
);

INSERT INTO loan (member_id, book_id, borrow_date, due_date, return_date, status)
VALUES
(
  (SELECT member_id FROM member WHERE email='ali@example.com'),
  (SELECT book_id FROM books WHERE title='1984'),
  CURRENT_DATE - 10,
  CURRENT_DATE - 3,
  NULL,
  'borrowed'
);

COMMIT;