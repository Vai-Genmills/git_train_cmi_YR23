select r.* from
`cmi-cat-fcst-dna-dev-75ee21.model.cat_fcst_model_strat_two_forecast_us` r 
inner join (
    select  max(r.forecast_time) as MaxDate
    from `cmi-cat-fcst-dna-dev-75ee21.model.cat_fcst_model_strat_two_forecast_us` r 
) m  on r.forecast_time = m.MaxDate
order by subcategory,months