select company_name, count(company_name) from project
where company_name=company_name
group by company_name;

--TextSize: repeats
--TextColor: IN THE all-client-at-once-color.sql