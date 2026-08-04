with source as (

    select *
    from {{ ref('country_dictionary') }}

),

renamed as (

    select
        trim(lower(country_name)) as country_name,
        trim(upper(iso2)) as country_code_iso2,
        trim(upper(iso3)) as country_code_iso3

    from source

)

select *
from renamed