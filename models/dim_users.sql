{{ config(materialized='table') }}

SELECT 
    user_id,
    MIN(created_at) AS first_purchase_date,
    COUNT(DISTINCT purchase_id) AS total_purchases
FROM {{ ref('raw_purchases') }}
GROUP BY 1
