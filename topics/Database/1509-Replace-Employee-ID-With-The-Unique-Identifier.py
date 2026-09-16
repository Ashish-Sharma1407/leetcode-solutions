############################################################
# Problem  : Replace Employee ID With The Unique Identifier
# ID       : 1509
# Difficulty: Easy
# Tags     : Database
# Runtime  : 1132
# Memory   : 0
# Language : MySQL
# Solved   : 2026-09-15 21:03
# URL      : https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/
############################################################
# Write your MySQL query statement below
SELECT unique_id, name
FROM Employees as e
LEFT JOIN EmployeeUNI as eu
ON e.id = eu.id;