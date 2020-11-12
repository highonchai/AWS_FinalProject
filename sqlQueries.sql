-- Query for Enrollments Table
SELECT e.enrollment_id as 'Enrollment ID', 
CONCAT(u.user_firstname, ' ', u.user_lastname) as 'Student Name', 
e.user_id as 'Student ID', 
c.course_name as 'Course Name', 
c.course_id as 'Course ID',
e.enrollment_grade as 'Student Grade'
FROM enrollments e
LEFT JOIN users u on u.user_id = e.user_id
LEFT JOIN courses c on c.course_id = e.course_id
ORDER BY u.user_lastname, u.user_firstname

select * from users