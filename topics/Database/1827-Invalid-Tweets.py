############################################################
# Problem  : Invalid Tweets
# ID       : 1827
# Difficulty: Easy
# Tags     : Database
# Runtime  : 901
# Memory   : 0
# Language : MySQL
# Solved   : 2026-09-15 20:54
# URL      : https://leetcode.com/problems/invalid-tweets/
############################################################
# Write your MySQL query statement below
SELECT tweet_id FROM Tweets
WHERE LENGTH(content) > 15;
