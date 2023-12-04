# Write your MySQL query statement below

# select round(count(agg_table.event_date)/count(*), 2) as fraction
# from (
    select round(count(join_table.event_date)/count(*), 2) as fraction
    from (select player_id, min(event_date) as event_date from Activity group by player_id) base_table
    left join Activity join_table
    on base_table.player_id = join_table.player_id
    and datediff(join_table.event_date, base_table.event_date) = 1
# ) as agg_table