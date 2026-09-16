############################################################
# Problem  : Triangle Judgement
# ID       : 610
# Difficulty: Easy
# Tags     : Database
# Runtime  : 379
# Memory   : 0
# Language : MySQL
# Solved   : 2026-09-16 20:37
# URL      : https://leetcode.com/problems/triangle-judgement/
############################################################
# Write your MySQL query statement below
SELECT *, CASE WHEN x+y>z AND y+z>x AND x+z>y THEN 'Yes'
ELSE 'No' END AS triangle
FROM Triangle