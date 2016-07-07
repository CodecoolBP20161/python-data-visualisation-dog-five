from db_helper import DataManager

first = 'project-names.sql'
USD_to_EUR = 0.902580
GBP_to_EUR = 1.167715


def valuta_change():
    for row in (DataManager.run_query('project-names.sql')):
        if row[2] == 'USD':
            usd = row[1]
            print(row[0], " ", float(usd)*USD_to_EUR, "U")
        elif row[2] == 'GBP':
            gbp = row[1]
            print(row[0], " ", float(gbp) * GBP_to_EUR, "G")
        else:
            eur = row[1]
            print(row[0], " ", eur, "EUR")


def convert_to_rgb():
    for row in (DataManager.run_query('project-names.sql')):
        try:
            value = row[3].lstrip('#')
            print(value)
            _NUMERALS = value
            RGB_list = [int(v, 16)*17 for v in (x for x in value)]
            print(RGB_list)
        except AttributeError:
            RGB_list = [255, 255, 255]
            print(RGB_list)


convert_to_rgb()