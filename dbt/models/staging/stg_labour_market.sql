with source as (

    select *
    from {{ ref('labour_market') }}

),

renamed as (

    select
        upper(country_code) as country_code_iso3,
        cast(year as integer) as year,
        cast(unemployment_rate as double) as unemployment_rate,
        cast(internet_users as integer) as internet_users,
        cast(gdp_per_capita as double) as gdp_per_capita,
        cast(tertiary_enrollment as double) as tertiary_enrollment

    from source

)

select *
from renamed
