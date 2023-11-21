SELECT
    dept_name
FROM
    instructor
GROUP BY
    dept_name
ORDER BY
    AVG(salary) DESC
LIMIT 1;

