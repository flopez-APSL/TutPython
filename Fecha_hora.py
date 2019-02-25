# dates are easily constructed and formatted
from datetime import date
now = date.today()
print(now)

fecha = now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")

print(fecha)

# dates support calendar arithmetic
birthday = date(1973, 8, 14)
age = now - birthday

print(age.days)

