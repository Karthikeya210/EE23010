SELECT
    st.id ,
    st.name,
    st.dept_name,
    SUM(c.credits) as sum 
FROM
    student as st
JOIN
    takes ON st.id = takes.id
JOIN
    course as c ON takes.course_id = c.course_id
GROUP BY
    st.id,
    st.name,
    st.dept_name
ORDER BY
    sum DESC,
    st.name ASC
LIMIT 3;

