{{ config(
    materialized='table'
) }}

WITH date_series AS (
    SELECT
        DATEADD(day, seq4(), '2024-01-01') AS date
    FROM TABLE(GENERATOR(ROWCOUNT => 365))
)

SELECT
    date,
    DAYOFWEEK(date) AS day_of_week,
    MONTH(date) AS month,
    QUARTER(date) AS quarter
FROM date_series
