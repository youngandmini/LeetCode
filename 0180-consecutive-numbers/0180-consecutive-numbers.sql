# Write your MySQL query statement below

select distinct l1.num as ConsecutiveNums
from Logs l1
join Logs l2 on l1.id = l2.id-1 and l1.num = l2.num
join Logs l3 on l2.id = l3.id-1 and l2.num = l3.num