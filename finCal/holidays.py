from pandas import Timestamp, DateOffset
from pandas.tseries.offsets import Day, BDay
from pandas.tseries.holiday import (after_nearest_workday,  Holiday,
                                    before_nearest_workday,
                                    nearest_workday, USLaborDay,
                                    weekend_to_monday, sunday_to_monday,
                                    next_monday_or_tuesday)
import datetime
from dateutil.relativedelta import MO, TH
import ephem


def calc_victoria_day(dt):
    date = datetime.date(dt.year, 5, 24)
    dow = date.weekday()
    date -= datetime.timedelta(dow)
    return Timestamp(date)


def compute_vernal_equinox_obs(dt):
    """ computes vernal equinox and observes using weekend_to_monday
    """
    equinox = ephem.next_spring_equinox(str(dt.year)).datetime().date()
    return sunday_to_monday(Timestamp(equinox))


def compute_autumnal_equinox_obs(dt):
    """ computes autumnal equinox and observes using weekend_to_monday
    """
    equinox = ephem.next_autumnal_equinox(str(dt.year)).datetime().date()
    return sunday_to_monday(Timestamp(equinox))

AfterUSThanksgiving = Holiday('Thanksgiving', month=11, day=1,
                              offset=[DateOffset(weekday=TH(4)), Day(1)])


CAThanksgivingDay = Holiday('Thanksgiving', month=10, day=1,
                            offset=DateOffset(weekday=MO(2)))
NewYears = Holiday('New Years Day', month=1,  day=1,
                   observance=sunday_to_monday)
NewYearsEve = Holiday('New Years Eve', month=1,  day=1,
                      observance=sunday_to_monday, offset=BDay(-1))
July4th = Holiday('July 4th', month=7,  day=4, observance=nearest_workday)
July4thEve = Holiday('July 4th Eve', month=7,  day=3)

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
# JP Holidays
JPComingOfAgeDay = Holiday("Japan Coming of Age", month=1, day=1,
                           offset=DateOffset(weekday=MO(2)))
JPNationalFoundingDay = Holiday("Japan Founding Day ", month=2, day=11)
JPVernalEquinox = Holiday("Vernal equinox obs ", month=3, day=1,
                          observance=compute_vernal_equinox_obs)
JPShowaDay = Holiday("Showa Day ", month=4, day=29,
                     observance=sunday_to_monday)
JPConstitutionDay = Holiday("Constitution Day", month=5, day=3,
                            observance=sunday_to_monday)
# http://en.wikipedia.org/wiki/Greenery_Day
JPGreeneryDay = Holiday("Greenery Day (changed name 2007)", month=5, day=4,
                        observance=next_monday_or_tuesday,
                        start_date=Timestamp("2007-01-01"))
JPDayOfRest = Holiday("Day of rest", month=5, day=4,
                      observance=sunday_to_monday,
                      end_date=Timestamp("2007-01-01"))
# http://en.wikipedia.org/wiki/Children's_Day_(Japan)
JPChildrensDay = Holiday("Children's day", month=5, day=5,
                         observance=sunday_to_monday,
                         start_date=Timestamp("1985-01-01"))
# http://en.wikipedia.org/wiki/Marine_Day
JPMarineDay = Holiday("Marine Day", month=7, day=1,
                      offset=DateOffset(weekday=MO(3)),
                      start_date=Timestamp("2003-01-01"))
# http://en.wikipedia.org/wiki/Respect_for_the_Aged_Day
JPRespectForAgedDay = Holiday("Respect for the Aged Day", month=9, day=1,
                              offset=DateOffset(weekday=MO(3)))
JPAutumnalEquinox = Holiday("Autumnal Equinox", month=9, day=1,
                            observance=compute_autumnal_equinox_obs)
# http://en.wikipedia.org/wiki/Health_and_Sports_Day
JPHealthSportsDay = Holiday("Health and Sports Day", month=10, day=1,
                            offset=DateOffset(weekday=MO(2)))
# http://en.wikipedia.org/wiki/Culture_Day
JPCultureDay = Holiday("Culture Day", month=11, day=3,
                       observance=sunday_to_monday)
# http://en.wikipedia.org/wiki/Labour_Thanksgiving_Day
JPLaborThanksgivingDay = Holiday("Labuor Thanksgiving  Day", month=11, day=3,
                                 observance=sunday_to_monday)

JPEmperorsBirthday = Holiday("Emperor Birthday", month=12, day=23,
                             observance=sunday_to_monday)
# http://en.wikipedia.org/wiki/Bank_holiday#In_the_United_Kingdom
# last Monday
GBSummerBankHoliday = Holiday("Summer Bank Holiday", month=8, day=24,
                              offset=DateOffset(weekday=MO(1)))
GBEarlyMayBankHoliday = Holiday("Early May Bank Holiday", month=5, day=1,
                                offset=DateOffset(weekday=MO(1)))
GBWilliamKateWedding = Holiday("Royal Wedding", month=4, day=29, year=2011)
QueensDiamondJubilee = Holiday("Queen's Diamond Jubilee", month=6,
                               day=5, year=2012)
GBSpringBankHoliday = Holiday("Spring Bank Holiday", month=5, day=24,
                              offset=DateOffset(weekday=MO(1)))
# not observed
Jan3rd = Holiday("New Year's holiday not observed", month=1, day=3)
Jan1st = Holiday("New Year's holiday not observed", month=1, day=1)
Jan2nd = Holiday("New Year's holiday not observed", month=1, day=2)
Dec31st = Holiday("New Year's holiday not observed", month=12, day=31)
ChristmasEveNotObserved = Holiday("Christmas Eve", month=12, day=24)
