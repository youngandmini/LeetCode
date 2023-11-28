# Write your MySQL query statement below

select s.product_id, j.first_year, s.quantity, s.price
from Sales s
join
    (select ss.product_id, min(ss.year) as first_year
    from Sales ss
    group by ss.product_id) as j
on s.product_id = j.product_id and s.year = j.first_year