SELECT
    course.course_id,
    course.title,
    instructor.name AS instructor,
    MIN(section.year) AS first_offered_year
FROM
    course
JOIN
    teaches ON course.course_id = teaches.course_id
JOIN
    instructor ON teaches.id = instructor.id
LEFT JOIN
    section ON course.course_id = section.course_id
GROUP BY
    course.course_id,
    course.title,
    instructor.name
HAVING
    MIN(section.year) = (
        SELECT
            MAX(first_offered_year)
        FROM
            (
                SELECT
                    course.course_id,
                    MIN(section.year) AS first_offered_year
                FROM
                    course
                LEFT JOIN
                    section ON course.course_id = section.course_id
                GROUP BY
                    course.course_id
            ) AS first_offerings
    )
ORDER BY
    course.course_id;

