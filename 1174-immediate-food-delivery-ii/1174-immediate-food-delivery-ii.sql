# Write your MySQL query statement below


select round(avg(if(d.order_date = d.customer_pref_delivery_date, 1, 0))*100, 2) as immediate_percentage 
from Delivery d
join (select customer_id, min(order_date) as order_date
from Delivery
group by customer_id) as j
on d.customer_id = j.customer_id and d.order_date = j.order_date
