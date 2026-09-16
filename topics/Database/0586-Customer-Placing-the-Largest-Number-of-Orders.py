############################################################
# Problem  : Customer Placing the Largest Number of Orders
# ID       : 586
# Difficulty: Easy
# Tags     : Database
# Runtime  : 506
# Memory   : 0
# Language : MySQL
# Solved   : 2026-09-16 20:19
# URL      : https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/
############################################################
# Write your MySQL query statement below
SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(customer_number) DESC
LIMIT 1
