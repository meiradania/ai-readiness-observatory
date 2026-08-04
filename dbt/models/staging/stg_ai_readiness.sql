with ai as (

    select
        cast(ranking as integer) as ranking,
        country_name,
        cast(year as integer) as year,
        cast(ai_readiness_index as double) as ai_readiness_score

    from {{ ref('ai_readiness') }}

),

countries as (

    select
        country_name,
        country_code_iso3

    from {{ ref('stg_countries') }}

),

final as (

    select
        ai.ranking,
        lower(ai.country_name) as country_name,
        countries.country_code_iso3,
        ai.ai_readiness_score

    from ai

    left join countries
        on ai.country_name = countries.country_name

)

select *
from final