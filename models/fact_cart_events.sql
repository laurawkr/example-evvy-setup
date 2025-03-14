{{ config(materialized='table') }}

SELECT 
    user_id,
    COUNT(DISTINCT session_id) AS cart_sessions,
    COUNT(DISTINCT purchase_id) AS completed_purchases,
    (COUNT(DISTINCT session_id) - COUNT(DISTINCT purchase_id)) AS cart_abandonment_count
FROM {{ ref('cart_event') }}
GROUP BY 1
