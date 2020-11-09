--Databases

-- ###Pages####
-- School Store + Purchase item from store + show purchased items (Blaine / Megan)
-------- SQL QUERIES: DISPLAY STORE, INSERT INTO Purchases, DISPLAY PURCHASES
-- Course Grades (Marshall / Connor)
------- DISPLAY + CALCULATE AVERAGES
-- User Profile / Update profile (Essie)
------ SQL QUERIES: DISPLAY TABLE, UPDATE
-- LOGIN functionality (Connor)
------ PYTHON LIST + COMPARE TO TABLE

--PAGE
-- python function that connects to the database and then displays info
-- SQL QUERY (view, update, delete, etc)

---MENU for ADMIN
-- User Profile
-- Update Profile
-- View grades of student
-- Go to School Store
-- 

-- MENU FOR EVERYONE ELSE
-- ####
-- User Profile
-- Update User Profile
-- View Grades
-- Go to School Store
-- View purchases
-- View Full Report


-- Functions file
-- Main File
-- Connection File




--Purchases Table (INSERT from user input with vscode)
CREATE TABLE purchases
(
purchase_id serial primary key,
user_id varchar(8) not null,
product_id varchar(8) not null,
purchase_date date not null,
discount decimal(4,2)
foreign key (user_id) references users (user_id) on delete cascade on update cascade,
foreign key (product_id) references products (product_id) on delete cascade on update cascade
)


--Create the Products Table
CREATE TABLE products
(
product_id serial primary key,
product_name text not null,
product_color text not null,
product_description text not null
)

-- Inserts items into the products table
INSERT INTO products (product_name, product_price, product_description) VALUES 
('College rule notebook', 4.99, 'Five Star College notebook 100 pages'),
('Oxford ruled index cards',  3.99, '100 pack wide ruled'),
('Pens', 2.99, 'Fine tip black 2 pack'),
('Colored Pencils', 1.99, '12 pack'),
('Notebook Paper', 2.99, '120 page pack wide rule'),
('Microsoft - Surface Studio 2', 3500, '28 Touch-Screen All-In-One Intel Core i7 16GB 1TB SSD' ),
('Microsoft - Surface Studio 2', 4500, '28 Touch-Screen All-In-One Intel Core i7 32GB 1TB SSD' ),
('Apple - 27" iMac Pro', 4100, 'iMac Pro with Retina 5K display 32GB Memory - 1TB SSD - Black' ),
('Apple - MacBook Pro - 16', 2100, 'Display with Touch Bar Intel Core i7 16GB Memory 512GB SSD'),
('Grapic Tee', 24.99, 'Uni-sexed XL'),
('Sweatshirt', 26.99, 'Uni-sexed XL'),
('Logo Socks', 5.99, 'Uni-sexed XL'),
('Grapic Tee', 24.99, 'Uni-sexed Large'),
('Sweatshirt', 26.99, 'Uni-sexed Large'),
('Logo Socks', 5.99, 'Uni-sexed Large'),
('Grapic Tee', 24.99, 'Uni-sexed Medium'),
('Sweatshirt', 26.99, 'Uni-sexed Medium'),
('Logo Socks', 5.99, 'Uni-sexed Medium'),
('Grapic Tee', 24.99, 'Uni-sexed Small'),
('Sweatshirt', 26.99, 'Uni-sexed Small'),
('Logo Socks', 5.99 , 'Uni-sexed Small')


-- Selects ALL from products Table
SELECT * FROM products

--Create users table
CREATE TABLE users
(
user_id serial primary key,
user_firstame text not null,
user_lastname text not null,
user_phone text not null,
user_email text not null,
user_password text not null,
user_role text not null, --Teacher, Student, Admin, etc
user_department text not null
)

-- Insert users into users table
INSERT INTO users (user_firstname, user_lastname, user_phone, user_email, user_password, user_role, user_department) VALUES
("Johnny", "AppleSeed", "444-444-1234", "johnny.appleseed@gmail.com", "passAdmin", "Principal", "Admin"),
("Emily", "Gold", "222-222-1234", "emily.gold@gmail.com", "passTeacher", "Teacher", "Staff"),
("Violet", "Waters", "123-123-1234", "violet.waters@gmail.com", "passTeacher", "Teacher", "Staff"),
("Trevor", "Stump", "111-111-1234", "trevor.stump@gmail.com", "passStudent", "Student", "Student"),
("Hannah", "Stump", "110-110-1234", "hannah.stump@gmail.com", "passStudent", "Student", "Student")

--Enrollment Table ()
CREATE TABLE enrollments
(
enrollment_id serial primary key,
user_id int not null,
course_id int not null,
enrollment_grade decimal(3,2)
foreign key (user_id) references users (user_id) on delete cascade on update cascade,
foreign key (class_id) references classes (class_id) on delete cascade on update cascade
)

--Class Table
CREATE TABLE courses
(
course_id serial primary key,
course_name text not null,
course_size int not null,
course_instructor text not null
)

INSERT INTO courses (course_name, course_size, course_instructor) VALUES
()

