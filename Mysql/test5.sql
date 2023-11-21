SELECT
    course_id,
    title
FROM
    course
WHERE
    course_id NOT IN (
        SELECT DISTINCT course_id
        FROM section
        WHERE year IN (2003, 2004)
    )
ORDER BY
    course_id ASC;

