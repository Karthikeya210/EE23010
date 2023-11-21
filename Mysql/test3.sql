SELECT
    COUNT(takes.id) 
FROM
    takes
JOIN
    section as s ON takes.course_id = s.course_id AND takes.sec_id = s.sec_id
JOIN
    student as st ON takes.id = st.id
JOIN
    course as c ON s.course_id = c.course_id
WHERE
    takes.course_id = '319'
    AND s.year = 2003
    AND st.dept_name <> c.dept_name;

