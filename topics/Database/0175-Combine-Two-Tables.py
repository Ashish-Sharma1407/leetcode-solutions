############################################################
# Problem  : Combine Two Tables
# ID       : 175
# Difficulty: Easy
# Tags     : Database
# Runtime  : 537
# Memory   : 0
# Language : MySQL
# Solved   : 2026-09-16 17:45
# URL      : https://leetcode.com/problems/combine-two-tables/
############################################################
# Write your MySQL query statement below
SELECT p.firstName, p.lastName, a.city, a.state
FROM Person AS p
LEFT JOIN Address AS a
ON p.personID = a.personID;
