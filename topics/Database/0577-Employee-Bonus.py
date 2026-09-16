############################################################
# Problem  : Employee Bonus
# ID       : 577
# Difficulty: Easy
# Tags     : Database
# Runtime  : 1154
# Memory   : 0
# Language : MySQL
# Solved   : 2026-09-16 20:02
# URL      : https://leetcode.com/problems/employee-bonus/
############################################################
# Write your MySQL query statement below
SELECT e.name, b.bonus
FROM Employee as e
LEFT JOIN Bonus as b
ON e.empId = b.empId
WHERE b.empId IS NULL OR bonus < 1000;