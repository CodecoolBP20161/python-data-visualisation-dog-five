select name, budget_value, budget_currency, main_color from project
where name notnull;

--There are some project which don't have main_color
--TextSize: budget_value (with change)
--TextColor: main_color