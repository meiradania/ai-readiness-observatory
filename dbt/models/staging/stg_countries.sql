with source as (

    select *
    from {{ ref('countries') }}

),

renamed as (

    select
        trim(lower(country_name)) as country_name,
        region,
        income_group,
        trim(upper(country_code)) as country_code_iso3

    from source

)

select *
from renamed
