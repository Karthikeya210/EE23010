SELECT
    c.course_id,
    c.title,
    c.dept_name,
    i.name,
    COUNT(takes.id),
    s.sec_id,
    s.semester,
    s.year,
    s.time_slot_id
FROM
    course as c
NATURAL JOIN 
    teaches as t
JOIN
    instructor as i ON i.id = t.id
JOIN
    section as s ON t.course_id = s.course_id AND t.sec_id = s.sec_id
JOIN
    takes ON s.course_id = takes.course_id AND s.sec_id = takes.sec_id
WHERE
    c.course_id = '362'
GROUP BY
    c.course_id,
    c.title,
    c.dept_name,
    i.name,
    s.sec_id,
    s.semester,
    s.year,
    s.time_slot_id
ORDER BY
    s.year DESC;


