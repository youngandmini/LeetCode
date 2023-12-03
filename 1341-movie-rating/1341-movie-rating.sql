# Write your MySQL query statement below

(select u.name as results
from MovieRating mr
join Users u on mr.user_id = u.user_id
group by mr.user_id
order by count(*) desc, u.name
limit 1)
union all
(select m.title as results
from MovieRating mr
join Movies m on mr.movie_id = m.movie_id
where date_format(mr.created_at, '%Y-%m') = '2020-02'
group by mr.movie_id
order by avg(mr.rating) desc, m.title
limit 1)