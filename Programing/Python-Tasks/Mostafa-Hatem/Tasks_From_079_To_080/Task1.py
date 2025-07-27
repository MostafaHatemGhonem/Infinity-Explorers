

import datetime

# The Date Is "2021, 6, 25"
# Today Is "2021, 8, 10"

pastData = datetime.datetime(2021, 6, 25)
todayData = (datetime.datetime.now())


print(f"Days From {pastData.date()} To {todayData.date()} Is => {(todayData.date() - pastData.date()).days}")

# Message Will Be
"Days From 2021-06-25 To 2021-08-10 Is => 46"