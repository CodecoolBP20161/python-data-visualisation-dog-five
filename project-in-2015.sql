select manager, budget_value, budget_currency, main_color from project
where duedate between '2014-12-31' and '2015-12-31'
order by name_length;

--It is sorted by manager. There are the budget values and currencies.

--TextSize: Here have to change the budget_value and to examine the biggest
--TextColor: main_color