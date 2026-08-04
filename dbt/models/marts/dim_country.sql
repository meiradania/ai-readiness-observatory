select
    c.country_code_iso3,
    c.country_name,
    c.region,
    c.income_group,
from {{ ref('stg_countries') }} as c