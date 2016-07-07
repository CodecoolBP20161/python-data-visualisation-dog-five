SELECT company_name, main_color, budget_value FROM project
WHERE budget_currency='EUR'
ORDER BY budget_value DESC
LIMIT 10;

--it is sorted by budget value, the last one is the biggest
--TextSize: The location in the list(1-10)
--TextColor: main_color
