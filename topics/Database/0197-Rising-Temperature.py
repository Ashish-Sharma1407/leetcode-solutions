############################################################
# Problem  : Rising Temperature
# ID       : 197
# Difficulty: Easy
# Tags     : Database
# Runtime  : 368
# Memory   : 0
# Language : MySQL
# Solved   : 2026-09-16 21:43
# URL      : https://leetcode.com/problems/rising-temperature/
############################################################
# Write your MySQL query statement below
SELECT id AS Id
FROM (SELECT *,
    LAG(temperature) OVER(ORDER BY recordDate) AS new_temp,
    LAG(recordDate) OVER(ORDER BY recordDate) AS prevDate
    FROM Weather) AS w
WHERE w.temperature > w.new_temp AND DATEDIFF(recordDate,prevDate) = 1;
