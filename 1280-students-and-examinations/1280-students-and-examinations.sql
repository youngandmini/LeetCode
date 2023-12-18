# Write your MySQL query statement below


select base_table.student_id, base_table.student_name, base_table.subject_name, ifnull(join_table.attended_exams, 0) as attended_exams
from (select * from Students stu
cross join Subjects sub) base_table
left join (select e.student_id, e.subject_name, count(*) as attended_exams
from Students s join Examinations e where s.student_id = e.student_id
group by e.student_id, e.subject_name) join_table
on base_table.student_id = join_table.student_id and base_table.subject_name = join_table.subject_name
order by student_id, subject_name