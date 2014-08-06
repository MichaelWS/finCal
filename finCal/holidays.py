from pandas import Timestamp, DateOffset
from pandas.tseries.offsets import Day
from pandas.tseries.holiday import (after_nearest_workday,  Holiday,
                                    before_nearest_workday,
                                    nearest_workday, USLaborDay,
                                    weekend_to_monday)
import datetime
from dateutil.relativedelta import MO


def calc_victoria_day(dt):
    date = datetime.date(dt.year, 5, 24)
    dow = date.weekday()
    date -= datetime.timedelta(dow)
    return Timestamp(date)





CAThanksgivingDay = Holiday('Thanksgiving', month=10, day=1,
                            offset=DateOffset(weekday=MO(2)))
NewYears = Holiday('New Years Day', month=1,  day=1,
                   observance=nearest_workday)
NewYearsEve = Holiday('New Years Eve', month=1,  day=1,
                      observance=nearest_workday)
July4th = Holiday('July 4th', month=7,  day=4, observance=nearest_workday)
July4thEve = Holiday('July 4th', month=7,  day=4,
                     observance=before_nearest_workday)

CAFamilyDay = Holiday('CA Family Day(Ontario Obs)', month=2,  day=1,
                      offset=DateOffset(weekday=MO(3)),
                      start_date=Timestamp("2008-01-01"))
VictoriaDay = Holiday('Victoria Day', month=5,  day=1,
                      observance=calc_victoria_day)
Christmas = Holiday('Christmas', month=12, day=25, observance=nearest_workday)
BoxingDay = Holiday('Boxing Day', month=12, day=25,
                    observance=after_nearest_workday)
CanadaDay = Holiday('Canada Day', month=7, day=1, observance=nearest_workday)
CACivicHoliday = Holiday("CA Civic Holiday", month=8, day=1,
                         offset=DateOffset(weekday=MO(1)))
CALaborDay = USLaborDay
MayDay = Holiday('May Day (Labour Day)', month=5, day=1,
                 observance=before_nearest_workday)
ChristmasEve = Holiday('Christmas', month=12, day=25,
                       observance=before_nearest_workday)
ChristmasObsAfter = Holiday('Christmas', month=12, day=25, 
                            observance=weekend_to_monday)
BoxingDayObsAfter = Holiday('Boxing day after', month=12, day=25, 
                            observance=weekend_to_monday, offset=Day(1))
ChristmasEveObsAfter = Holiday('Christmas eve ', month=12, day=25, 
                               observance=weekend_to_monday, offset=Day(-1))



