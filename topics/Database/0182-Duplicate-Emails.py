############################################################
# Problem  : Duplicate Emails
# ID       : 182
# Difficulty: Easy
# Tags     : Database
# Runtime  : 484
# Memory   : 0
# Language : MySQL
# Solved   : 2026-09-16 17:59
# URL      : https://leetcode.com/problems/duplicate-emails/
############################################################
# Write your MySQL query statement below
SELECT email AS Email
FROM Person
GROUP BY email
HAVING count(id) > 1;