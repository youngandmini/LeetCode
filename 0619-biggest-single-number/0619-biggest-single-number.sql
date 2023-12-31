# Write your MySQL query statement below


# select
#     if(
#         count(
#             select n1.num
#             from MyNumbers as n1
#             group by n1.num
#             having count(n1.num) <= 1
#         ) = 0, 
#        null,
#        (select *
#         from MyNumbers
#         group by num
#         having count(num) <= 1
#         order by num desc
#         limit 1)
#     ) as num
# from dual;


select max(a.num) as num
from
(select * from MyNumbers
group by num
having count(num) <= 1) as a
