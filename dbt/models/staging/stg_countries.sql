with source as (

    select *
    from {{ ref('countries') }}

),

renamed as (

    select
        country_name,
        region,
        income_group,
        upper(country_code) as country_code_iso3

    from source

)

select *
from renamed
