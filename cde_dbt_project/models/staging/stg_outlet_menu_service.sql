with raw_orders as (
    select *
    from {{ ref('orders') }}
)

select
    id,
    customer_id,
    restaurant_outlet_id as outlet_id,
    order_date,
    total_amount,
    status,
    payment_id,
    delivery_id,
    dining_option
from raw_orders
