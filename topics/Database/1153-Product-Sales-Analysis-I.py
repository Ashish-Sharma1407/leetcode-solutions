############################################################
# Problem  : Product Sales Analysis I
# ID       : 1153
# Difficulty: Easy
# Tags     : Database
# Runtime  : 1393
# Memory   : 0
# Language : MySQL
# Solved   : 2026-09-15 21:11
# URL      : https://leetcode.com/problems/product-sales-analysis-i/
############################################################
# Write your MySQL query statement below
SELECT p.product_name, s.year, s.price
FROM Sales AS s
JOIN Product AS p
ON s.product_id = p.product_id;