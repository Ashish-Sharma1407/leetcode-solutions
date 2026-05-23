############################################################
# Problem  : Big Countries
# ID       : 595
# Difficulty: Easy
# Tags     : Database
# Runtime  : 266
# Memory   : 0
# Language : MySQL
# Solved   : 2025-10-10 13:26
# URL      : https://leetcode.com/problems/big-countries/
############################################################
# Write your MySQL query statement below
Select name, population, area FROM World
WHERE area >= 3000000 or population >= 25000000;