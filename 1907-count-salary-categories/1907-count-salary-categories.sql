# Write your MySQL query statement below


select t1.category, ifnull(t2.accounts_count, 0) as accounts_count
from
((select "Low Salary" as category
from dual)
union
(select "Average Salary" as category
from dual)
union
(select "High Salary" as category
from dual)) as t1
left join
(select
case
when income < 20000 then 'Low Salary'
when income > 50000 then 'High Salary'
else 'Average Salary'
end as category, count(*) as accounts_count
from Accounts
group by category) as t2
on t1.category = t2.category