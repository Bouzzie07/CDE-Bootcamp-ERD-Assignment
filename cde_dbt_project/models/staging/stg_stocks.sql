{{ config(
    materialized='view'
) }}

SELECT *
FROM {{ source('restaurant_data_sources', 'stocks') }}
