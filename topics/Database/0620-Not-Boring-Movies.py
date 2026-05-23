############################################################
# Problem  : Not Boring Movies
# ID       : 620
# Difficulty: Easy
# Tags     : Database
# Runtime  : 212
# Memory   : 0
# Language : MySQL
# Solved   : 2025-10-10 13:41
# URL      : https://leetcode.com/problems/not-boring-movies/
############################################################
# Write your MySQL query statement below
SELECT * FROM Cinema
WHERE MOD(id,2) = 1 and description != "boring"
ORDER BY rating DESC;