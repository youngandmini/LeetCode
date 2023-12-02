# Write your MySQL query statement below

select *
from Users 
where mail REGEXP ('^[A-Za-z][0-9A-Za-z_.-]*@leetcode\\.com')