############################################################
# Problem  : Article Views I
# ID       : 1258
# Difficulty: Easy
# Tags     : Database
# Runtime  : 471
# Memory   : 0
# Language : MySQL
# Solved   : 2026-09-15 20:51
# URL      : https://leetcode.com/problems/article-views-i/
############################################################
# Write your MySQL query statement below
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id ASC