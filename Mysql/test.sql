SELECT
    i.dept_name ,
    t.course_id,
    c.title ,
    s.sec_id ,
    s.semester,
    s.year,
    COUNT(takes.id) 
FROM
    instructor as i
NATURAL JOIN
    teaches as t
JOIN
    course as c ON t.course_id = c.course_id
JOIN
    section as s ON t.course_id = s.course_id AND t.sec_id = s.sec_id
JOIN
    takes ON s.course_id = takes.course_id AND s.sec_id = takes.sec_id
WHERE
    i.salary = (SELECT MAX(salary) FROM instructor)
GROUP BY
    i.dept_name,
    t.course_id,
    c.title,
    s.sec_id,
    s.semester,
    s.year
ORDER BY
    t.course_id ASC,
    s.year ASC,
    s.semester ASC;

