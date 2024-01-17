# Write your MySQL query statement below
select s.user_id, ROUND(AVG(IF(c.action='confirmed',1,0)),2) as confirmation_rate
from Signups s
LEFT JOIN Confirmations c
ON s.user_id = c.user_id
GROUP BY s.user_id