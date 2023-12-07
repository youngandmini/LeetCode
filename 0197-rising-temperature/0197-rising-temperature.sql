# Write your MySQL query statement below

select basetable.id
from Weather basetable
join Weather jointable
on datediff(basetable.recordDate, jointable.recordDate) = 1
where basetable.temperature > jointable.temperature