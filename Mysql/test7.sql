SELECT
    course_id,
    title
FROM
    course
WHERE
    LENGTH(title) > 15
    AND LOWER(title) LIKE '%sys%'
ORDER BY
    course_id ASC;

