from pandas import Timestamp, DateOffset
from pandas.tseries.holiday import (after_nearest_workday,  Holiday,
                                    before_nearest_workday,
                                    nearest_workday, USLaborDay)
import datetime
from dateutil.relativedelta import MO


def calc_victoria_day(dt):
    date = datetime.date(dt.year, 5, 24)
    dow = date.weekday()
    date -= datetime.timedelta(dow)
    return Timestamp(date)


CAThanksgivingDay = Holiday('Thanksgiving', month=10, day=1,
                            offset=DateOffset(weekday=MO(2)))
New_Years = Holiday('New Years Day', month=1,  day=1,
                    observance=nearest_workday)
July_4th = Holiday('July 4th', month=7,  day=4, observance=nearest_workday)

CAFamilyDay = Holiday('CA Family Day(Ontario Obs)', month=2,  day=1,
                      offset=DateOffset(weekday=MO(3)), start=Timestamp(2008))
VictoriaDay = Holiday('Victoria Day', month=5,  day=1,
                      observance=calc_victoria_day)
Christmas = Holiday('Christmas', month=12, day=25, observance=nearest_workday)
BoxingDay = Holiday('Boxing Day', month=12, day=25,
                    observance=after_nearest_workday)
CanadaDay = Holiday('Canada Day', month=7, day=1, observance=nearest_workday)
CACivicHoliday = Holiday("CA Civic Holiday", month=8, day=1,
                         offset=DateOffset(weekday=MO(1)))
CALaborDay = USLaborDay
ChristmasEve = Holiday('Christmas', month=12, day=25,
                       observance=before_nearest_workday)

ca_tsx_rules = [CAThanksgivingDay, New_Years, CAFamilyDay, VictoriaDay,
                Christmas, BoxingDay, CanadaDay, CACivicHoliday, CALaborDay]
ca_tsx_early_close_rules = [ChristmasEve]
