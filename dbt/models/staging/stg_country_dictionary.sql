with source as (

    select *
    from {{ ref('country_dictionary') }}

),

renamed as (

    select
<<<<<<< HEAD
        lower(country_name) as country_name,
        upper(iso2) as country_code_iso2,
        upper(iso3) as country_code_iso3
=======
        trim(lower(country_name)) as country_name,
        trim(upper(iso2)) as country_code_iso2,
        trim(upper(iso3)) as country_code_iso3
>>>>>>> 3160005 (schema.yml files for staging tables and mart tables.)

    from source

)

select *
from renamed