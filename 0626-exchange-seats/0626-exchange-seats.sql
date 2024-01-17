# Write your MySQL query statement below

select id, CASE 
                when id%2=1 then coalesce(lead(student) over (order by id),student)
                when id%2=0 then coalesce(lag(student) over (order by id),student)
                Else student
            END as student
from Seat