############################################################
# Problem  : Find Customer Referee
# ID       : 584
# Difficulty: Easy
# Tags     : Database
# Runtime  : 513
# Memory   : 0
# Language : MySQL
# Solved   : 2026-09-15 20:39
# URL      : https://leetcode.com/problems/find-customer-referee/
############################################################
# Write your MySQL query statement below
SELECT name FROM Customer
WHERE referee_id != 2
    OR referee_id IS null;