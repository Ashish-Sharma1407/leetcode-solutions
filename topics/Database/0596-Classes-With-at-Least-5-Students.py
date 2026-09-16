############################################################
# Problem  : Classes With at Least 5 Students
# ID       : 596
# Difficulty: Easy
# Tags     : Database
# Runtime  : 308
# Memory   : 0
# Language : MySQL
# Solved   : 2026-09-16 20:30
# URL      : https://leetcode.com/problems/classes-with-at-least-5-students/
############################################################
# Write your MySQL query statement below
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(class) >= 5;
