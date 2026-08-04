with ai as (

    select *
    from {{ ref('stg_ai_readiness') }}

),

labour as (

    select *
    from {{ ref('stg_labour_market') }}

)

select
    labour.country_code_iso3,
    labour.year,

    ai.ranking,
    ai.ai_readiness_score,

    labour.unemployment_rate,
    labour.internet_users,
    labour.gdp_per_capita,
    labour.tertiary_enrollment,

    case
        when ai.ai_readiness_score >= 80 then 'High'
        when ai.ai_readiness_score >= 60 then 'Medium'
        else 'Low'
    end as ai_readiness_category,

    current_date as snapshot_date

from labour

left join ai
    on ai.country_code_iso3 = labour.country_code_iso3
    and ai.year = labour.year