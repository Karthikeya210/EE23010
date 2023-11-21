SELECT
    id,
    name,
    dept_name
FROM
    instructor
WHERE
    id NOT IN (
        SELECT
            id
        FROM
            teaches as t
        JOIN
            section as s ON t.course_id = s.course_id AND t.sec_id = s.sec_id AND s.year = 2003
        GROUP BY
            id
        HAVING
            COUNT(DISTINCT s.course_id) > 1
    )
ORDER BY
    id;

