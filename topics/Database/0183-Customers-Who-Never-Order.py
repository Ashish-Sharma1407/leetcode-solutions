############################################################
# Problem  : Customers Who Never Order
# ID       : 183
# Difficulty: Easy
# Tags     : Database
# Runtime  : 639
# Memory   : 0
# Language : MySQL
# Solved   : 2026-09-16 18:02
# URL      : https://leetcode.com/problems/customers-who-never-order/
############################################################
# Write your MySQL query statement below
SELECT c.name AS Customers
FROM Customers AS c
LEFT JOIN Orders AS o
ON c.id = o.customerID
WHERE o.customerID IS NULL
