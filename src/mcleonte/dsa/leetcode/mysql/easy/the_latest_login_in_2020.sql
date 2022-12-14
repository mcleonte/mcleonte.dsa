-- https://leetcode.com/problems/the-latest-login-in-2020/
-- https://leetcode.com/problems/the-latest-login-in-2020/discuss/2828564/MySQL-or-greater96
SELECT
  user_id,
  MAX(time_stamp) AS last_stamp
FROM logins
WHERE YEAR(time_stamp) = 2020
GROUP BY user_id
