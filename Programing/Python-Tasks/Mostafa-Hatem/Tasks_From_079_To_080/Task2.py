

import datetime

# Today Is "2021, 8, 10"

print(datetime.datetime.now().date())
print(datetime.datetime.now().strftime("%b %d, %Y"))
print(datetime.datetime.now().strftime("%d - %b - %Y"))
print(datetime.datetime.now().strftime("%d - %b - %y"))
print(datetime.datetime.now().strftime("%d - %B - %Y"))
print(datetime.datetime.now().strftime("%a, %m %B  %Y"))


"2021-08-10"
"Aug 10, 2021"
"10 - Aug - 2021"
"10 / Aug / 21"
"10 / August / 2021"
"Tue, 10 August 2021"