# Write your MySQL query statement below


select p0.product_id, ifnull(new_price, 10) as price 
from (select distinct product_id
from Products) p0
left join 

(select p1.product_id, p1.change_date, p1.new_price
from Products p1
join
(select product_id, max(change_date) as change_date
from Products
where change_date <= '2019-08-16'
group by product_id) p2
on p1.product_id = p2.product_id
and p1.change_date = p2.change_date) p12
on p0.product_id = p12.product_id