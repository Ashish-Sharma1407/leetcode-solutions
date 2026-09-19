############################################################
# Problem  : Average Time of Process per Machine
# ID       : 1801
# Difficulty: Easy
# Tags     : Database
# Runtime  : 253
# Memory   : 0
# Language : MySQL
# Solved   : 2026-09-19 20:16
# URL      : https://leetcode.com/problems/average-time-of-process-per-machine/
############################################################
SELECT 
    a.machine_id,
    ROUND(AVG(b.timestamp - a.timestamp), 3) AS processing_time
FROM Activity a
JOIN Activity b
ON a.machine_id = b.machine_id
AND a.process_id = b.process_id
WHERE a.activity_type = 'start'
AND b.activity_type = 'end'
GROUP BY a.machine_id;