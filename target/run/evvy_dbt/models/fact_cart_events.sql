
  create or replace   view EVVY_DB.TEST.fact_cart_events
  
   as (
    SELECT
    ID,
    USER_ID,
    PRODUCT_ID,
    TIMESTAMP
FROM TEST.CART_EVENT
  );

