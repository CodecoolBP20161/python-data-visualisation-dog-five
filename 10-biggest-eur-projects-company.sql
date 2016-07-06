select company_name, main_color from project
where budget_currency='EUR'
order by budget_value
Limit 10;

--it is sorted by budget value, the last one is the biggest
--TextSize: The location in the list(1-10)
--TextColor: main_color

