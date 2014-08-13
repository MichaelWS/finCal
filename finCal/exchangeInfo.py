from finCal.holidays import (NewYears, Christmas, July4th, ChristmasEve,
                             July4thEve, CAThanksgivingDay, CAFamilyDay,
                             VictoriaDay, CanadaDay, CACivicHoliday,
                             CALaborDay, NewYearsEve, MayDay,
                             ChristmasObsAfter, BoxingDayObsAfter,
                             ChristmasEveObsAfter, AfterUSThanksgiving,
                             JPMarineDay, JPRespectForAgedDay, Jan1st,
                             Jan2nd, Jan3rd, Dec31st, JPChildrensDay,
                             JPAutumnalEquinox, JPVernalEquinox,
                             JPLaborThanksgivingDay, JPComingOfAgeDay,
                             JPHealthSportsDay, JPConstitutionDay,
                             JPShowaDay, JPNationalFoundingDay, JPCultureDay,
                             JPEmperorsBirthday, GBSummerBankHoliday,
                             GBWilliamKateWedding, QueensDiamondJubilee,
                             GBSpringBankHoliday, GBEarlyMayBankHoliday)

import datetime
from pandas.tseries.holiday import (Holiday, USMartinLutherKingJr,
                                    USMemorialDay,
                                    USLaborDay, USThanksgivingDay,
                                    USPresidentsDay, EasterMonday, GoodFriday)
from pandas import Timestamp

# us_nyse_info
# specified by https://www.nyse.com/markets/hours-calendars
# zipline has sandy and president holidays as well.

nyse_rules = [NewYears,
              USMartinLutherKingJr,
              USPresidentsDay,
              USMemorialDay,
              July4th,
              USLaborDay,
              USThanksgivingDay,
              Christmas]


nyse_unscheduled = [Holiday('President Nixon Death', year=1994,
                            month=4, day=27),
                    Holiday('President Regan Death', year=2004,
                            month=6, day=11),
                    Holiday('Sept 11 day 1', year=2001,
                            month=9, day=11),
                    Holiday('Sept 11 day 2', year=2001,
                            month=9, day=12),
                    Holiday('Sept 11 day 3', year=2001,
                            month=9, day=13),
                    Holiday('Sept 11 day 4', year=2001,
                            month=9, day=14),
                    Holiday('President Gerald Ford', year=2007,
                            month=1, day=2),
                    Holiday('Storm: Sandy day 1', year=2012,
                            month=10, day=29),
                    Holiday('Storm: Sandy day 2', year=2012,
                            month=10, day=30),
                    Holiday('Storm: Sandy day 3', year=2012,
                            month=11, day=1)]

nyse_times = {"start": datetime.time(9, 30),
              "close": datetime.time(16, 00),
              "early_close": datetime.time(13, 00),
              "end_date": None,
              "tz_info": "America/New_York"}

nyse_exchange_rules = nyse_rules + nyse_unscheduled


nyse_early_close_rules = [July4thEve, ChristmasEve,
                          AfterUSThanksgiving]

# ca_tsx_info
ca_tsx_rules = [CAThanksgivingDay, NewYears, CAFamilyDay, VictoriaDay,
                ChristmasObsAfter, BoxingDayObsAfter, CanadaDay,
                CACivicHoliday, CALaborDay, GoodFriday]
ca_tsx_early_close_rules = [ChristmasEveObsAfter]

ca_tsx_times = nyse_times.copy()
ca_tsx_times["tz_info"] = "America/Toronto"

# euronext info
euronext_rules = [EasterMonday, GoodFriday, NewYears, MayDay,
                  ChristmasObsAfter, BoxingDayObsAfter]
eu_early_close_rules = [ChristmasEve, NewYearsEve]

euronext_times = {"start": datetime.time(9, 0),
                  "close": datetime.time(17, 30),
                  "early_close": datetime.time(14, 00),
                  "end_date": None,
                  "tz_info": "Europe/Paris"}

# tokyo info
# http://en.wikipedia.org/wiki/Tokyo_Stock_Exchange
jp_tse_times = [{"start": datetime.time(9, 0),
                 "close": datetime.time(15, 00),
                 "early_close": datetime.time(11, 00),
                 "lunch_start": datetime.time(11, 0),
                 "lunch_end": datetime.time(13, 00),
                 "end_date": Timestamp("2006-04-24"),
                 "tz_info": "Asia/Tokyo"},
                {"start": datetime.time(9, 0),
                 "close": datetime.time(15, 00),
                 "early_close": datetime.time(11, 30),
                 "lunch_start": datetime.time(11, 30),
                 "lunch_end": datetime.time(12, 30),
                 "end_date": Timestamp(datetime.datetime.now()),
                 "tz_info": "Asia/Tokyo"}]
jp_rules = [JPComingOfAgeDay, JPNationalFoundingDay, Dec31st,
            Jan1st, Jan2nd, Jan3rd, JPVernalEquinox, JPShowaDay,
            JPConstitutionDay, JPChildrensDay, JPMarineDay,
            JPRespectForAgedDay, JPAutumnalEquinox, JPHealthSportsDay,
            JPCultureDay, JPLaborThanksgivingDay, JPEmperorsBirthday]

# lse info
lse_rules = [NewYears, GBSummerBankHoliday, ChristmasObsAfter,
             BoxingDayObsAfter, GBWilliamKateWedding, GoodFriday,
             EasterMonday, QueensDiamondJubilee, GBSpringBankHoliday,
             GBEarlyMayBankHoliday]


lse_early_close_rules = [ChristmasEve, NewYearsEve]

lse_times = {"start": datetime.time(8, 0),
             "close": datetime.time(16, 30),
             "early_close": datetime.time(12, 30),
             "end_date": None,
             "tz_info": "Europe/London"}
