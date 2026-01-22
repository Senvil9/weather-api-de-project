{{ config(
    materialized='table',
    unique_key='id'
)}}

with source as (
    select *
from {{ source('dev', 'raw_weather_data')}}
),

de_dup as (
    select
        *,
        row_number() over (partition by time order by inserted_at) as rn
    from source
)



select
    id,
    city,
    temperature,
    weather_description,
    wind_speed,
    time as weather_time_local,
    (inserted_at + (utc_offset || ' hours')::interval) as inserted_at_local
from de_dup
where rn = 1