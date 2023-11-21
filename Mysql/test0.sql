SELECT i.name, i.id, COUNT(DISTINCT course_id)  as n
FROM teaches as t
JOIN instructor as i ON t.id = i.id
GROUP BY i.id
ORDER BY n DESC
LIMIT 3;


SELECT i.name,i.id, COUNT(DISTINCT t.course_id) as n
FROM teaches as t
JOIN instructor as i ON t.id = i.id
WHERE i.dept_name = 'Statistics'
GROUP BY i.id
ORDER BY n DESC
LIMIT 3;
