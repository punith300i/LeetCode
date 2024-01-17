# Write your MySQL query statement below
select name from Employee E JOIN
(select managerId, count(*) as mgr_cnt 
from Employee where managerId is not null group by managerId) T ON E.id = T.managerId
WHERE T.mgr_cnt > 4