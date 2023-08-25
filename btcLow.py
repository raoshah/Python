import datetime

def btc_low(date):
    y, m, d = date
    days = datetime.datetime.now() - datetime.datetime(y, m, d)
    return days

def low_gap(low1, low2):
    r = low1 - low2
    return r

btc_2011 = (2011, 11, 18)
btc_2015 = (2015, 8, 25)
btc_2018 = (2018, 12, 12)
btc_2022 = (2022, 12, 29)

days = [btc_low(btc_2011).days, btc_low(btc_2015).days, btc_low(btc_2018).days, btc_low(btc_2022).days]

gap_2011 = low_gap(days[0], days[1])
gap_2015 = low_gap(days[1], days[2])
gap_2018 = low_gap(days[2], days[3])

print(f"2011-2015 = {gap_2011}, 2015-2018 = {gap_2015}, 2018-2022 = {gap_2018} From last low {days[3]}")

