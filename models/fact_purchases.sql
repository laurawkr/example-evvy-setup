{{ config(materialized='table') }}

SELECT 
    purchase_id,
    user_id,
    product_id,
    purchase_date,
    amount,
    CASE 
        WHEN purchase_type = 'subscription' THEN 'Subscription'
        ELSE 'One-time'
    END AS purchase_category
FROM {{ ref('raw_purchases') }}
