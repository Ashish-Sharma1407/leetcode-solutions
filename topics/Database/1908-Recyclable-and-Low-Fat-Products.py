############################################################
# Problem  : Recyclable and Low Fat Products
# ID       : 1908
# Difficulty: Easy
# Tags     : Database
# Runtime  : 611
# Memory   : 0
# Language : MySQL
# Solved   : 2026-09-15 20:31
# URL      : https://leetcode.com/problems/recyclable-and-low-fat-products/
############################################################
# Write your MySQL query statement below
SELECT product_id FROM Products WHERE low_fats = "Y" AND recyclable = "Y";