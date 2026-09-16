############################################################
# Problem  : Big Countries
# ID       : 595
# Difficulty: Easy
# Tags     : Database
# Runtime  : 286
# Memory   : 0
# Language : MySQL
# Solved   : 2026-09-15 20:46
# URL      : https://leetcode.com/problems/big-countries/
############################################################
# Write your MySQL query statement below
SELECT name, population, area
FROM World
WHERE area >= 3000000 
    OR population >= 25000000;