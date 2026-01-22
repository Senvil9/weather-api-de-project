{{ config(
    materialized='table',
    unique_key='id'
)}}

select 
    city,
    temperature,
    weather_description,
    wind_speed,
    weather_time_local
from {{ ref('stg_weather_data') }}
