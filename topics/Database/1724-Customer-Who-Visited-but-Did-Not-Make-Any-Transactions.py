############################################################
# Problem  : Customer Who Visited but Did Not Make Any Transactions
# ID       : 1724
# Difficulty: Easy
# Tags     : Database
# Runtime  : 1428
# Memory   : 0
# Language : MySQL
# Solved   : 2026-09-15 21:49
# URL      : https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/
############################################################
# Write your MySQL query statement below
SELECT v.customer_id, count(v.customer_id) AS count_no_trans
FROM Visits AS v
LEFT JOIN Transactions AS t
ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY customer_id;