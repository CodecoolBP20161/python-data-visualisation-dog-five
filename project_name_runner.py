import db_helper

first = 'project-names.sql'
USD_to_EUR = 0.902580
GBP_to_EUR = 1.167715

for row in (db_helper.create_tables(first)):
    if row[2] == 'USD':
        usd = row[1]
        print(row[0], " ", float(usd)*USD_to_EUR, "U")
    elif row[2] == 'GBP':
        gbp = row[1]
        print(row[0], " ", float(gbp) * GBP_to_EUR, "G")
    else:
        eur = row[1]
        print(row[0], " ", eur, "EUR")