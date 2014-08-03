from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday,
                                   USMartinLutherKingJr, USMemorialDay,
                                   USLaborDay, USThanksgivingDay,
                                   nearest_workday

nyse_rules = [Holiday('New Years Day', month=1,  day=1,  observance=nearest_workday),
              USMartinLutherKingJr,
              USPresidentsDay,
              USMemorialDay,
              Holiday('July 4th', month=7,  day=4,  observance=nearest_workday),
              USLaborDay,
              USThanksgivingDay,
              Holiday('Christmas', month=12, day=25, observance=nearest_workday)
              ]

nyse_unscheduled = [Holiday('President Nixon Death', year=1994,
                            month=4, day=27),
                    Holiday('President Regan Death'),year=2004,
                            month=6, day=11),
                    Holiday('President Gerald Ford'), year=2007,
                            month=1, day=2),
                    Holiday('Storm: Sandy day 1'), year=2012,
                            month=10, day=29),
                    Holiday('Storm: Sandy day 2'), year=2012,
                            month=10, day=30),
                    Holiday('Storm: Sandy day 3'), year=2012,
                            month=11, day=1),]

BASE_TZ_INFO = "America/New_York"


def process_exch_times(exch_time_set):
    length = len(exch_time_set)
    assert "start" in exch_time_set
    assert "end" in exch_time_set
    assert "early_close" in exch_time_set
    if "end_date" not in exch_time_dict:
        exch_time_dict["end_date"] = None
        return exch_time_dict

class ExchangeCalendar(AbstractHolidayCalendar):
    """
    Class that defines a Exchange time
    takes a list or set
    a list of [(end_date, "9:30", "16:00",),]
    or a set ("9:30", "16:00")

    """
    _early_close_cache = None
    def __init__(self, name=None, rules=None, early_close_rules=None,
                 times=None, open_days=None,
                 tz_info=BASE_TZ_INFO):
        if name is None:
            name = self.__class__.__name__
        self.name = name
        if open_days is None:
            open_days = (0, 1, 2, 3, 4)
            # Monday Through Friday is default, but Israel as an example
            # of a different day.  also this allows for complex rules
        self.open_days = open_days
        if rules is not None:
            self.rules = rules
        if early_close_rules is None:
            self.early_close_rules = None
        if type(times) == list and len(times) = 1:
            times = times[0]
        assert type(times) == set or type(times) == list
        if type(times) ==I set:
            end_date = None
            self.exchange_schedules = [process_exch_time(times)]
        else:
            self.exchange_schedules = []
            for time in times:
                self.exchange_schedules.append(process_exch_time(times))
            self.exchange_schedules = sorted(self.exchange_times,
                                             key=lambda x: x[0])
            super(ExchangeCalendar, self).__init__
        self.early_closes()
        self.holidays()

    def early_closes(self, start=None, end=None, return_name=False):
        """
        Returns a curve with early_closes between start_date and end_date

        Parameters
        ----------
        start : starting date, datetime-like, optional
        end : ending date, datetime-like, optional
        return_names : bool, optional
            If True, return a series that has dates and holiday names.
            False will only return a DatetimeIndex of dates.

        Returns
        -------
            DatetimeIndex of early_closes
        """
        if self.early_close_rules is None:
            raise Exception('Exchange Calendar %s does not have any '\
                            'early close rules specified' % self.name)

        if start is None:
            start = AbstractHolidayCalendar.start_date

        if end is None:
            end = AbstractHolidayCalendar.end_date
        start = Timestamp(start)
        end   = Timestamp(end)
        early_closes = None
        # If we don't have a cache or the dates are outside the prior cache, we get them again
        if (self._early_close_cache is None
                or start < self._early_close_cache[0]
                or end > self._early_close_cache[1]):
            for rule in self.early_close_rules:
                rule_early_closes = rule.dates(start, end, return_name=True)
                if early_closes is None:
                    early_closes = rule_early_closes
                else:
                    early_closes = holidays.append(rule_r)
            self._early_close_cache = (start, end, holidays.sort_index())

        early_closes = self._early_close_cache[2]
        early_closes = self.early_closes[start:end]

        if return_name:
            return early_closes
        else:
            return early_closes.index

    def get_market_times(date):
        """
        returns a set of pandas Timestamps re
        if market is closed
        returns (None, None)
        """
        if type(date) != Timestamp:
            date = Timestamp(date)
        if date in self._cache or date.dayofweek not in self.open_days:
            return None, None
            # returning None for market closure.
        else:
            start_time = None
            for schedule in self.exchange_schedules:
                if schedule["end_date"] is None or
                    date <= schedule["end_date"]:
                    break
            start_ts = create_ts(date, schedule["start_time"], 
                                 tz=self.tz_info)
            if date in self._early_close_cache:
                end_ts = create_ts
                





class US_ScheduledCalendar(ExchangeCalendar)
    """
    US stock exchange calendar specified by
    https://www.nyse.com/markets/hours-calendars
    """
    rules = nyse_rules

class US_ExchangeCalendar(ExchangeCalendar):
    """
    US stock exchange calendar specified by
    https://www.nyse.com/markets/hours-calendars
    """
    rules = nyse_exchange_rules + nyse_unscheduled

