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

    <Exclude date="20121029"/>
    <Exclude date="20121030"/>
    <Exclude date="20121122"/>
BASE_TZ_INFO = "America/New_York"

def get_time(time_str):
    split_str = time_str.split(":")
    return time.time(split_str[0], split_str[1])


class ExchangeTime(object):
    """
    Class that defines a Exchange time
    takes a list or set 
    a list of [("9:30", "16:00", end_date),]
    or a set ("9:30", "16:00")
    
    """
    def __init__(self, times,
                 tz_info=BASE_TZ_INFO):
        if type(times) == list and len(times) = 1:
            times = times[0]
        assert type(times) == set or type(times) == list
        if type(times) == set:
            end_time = None
            exch_times = end_date, get_time(times[0]), get_time(times[1])
            self.exchange_schedules = [times]
        else:
            self.exchange_schedules = []
            for time in times:
                exch_times = end_date, get_time(times[0]), get_time(times[1])
                self.exchange_schedules.append(exch_times)
            self.exchange_schedules = sorted(self.exchange_times, 
                                             key=lambda x: x[0])
            


    def __repr__(self):
        info = ''
        if self.year is not None:
            info += 'year=%s, ' % self.year
        info += 'month=%s, day=%s, ' % (self.month, self.day)

        if self.offset is not None:
            info += 'offset=%s' % self.offset

        if self.observance is not None:
            info += 'observance=%s' % self.observance

        repr = 'Holiday: %s (%s)' % (self.name, info)
        return repr

    def dates(self, start_date, end_date, return_name=False):
        """
        Calculate holidays between start date and end date

        Parameters
        ----------
        start_date : starting date, datetime-like, optional
        end_date : ending date, datetime-like, optional
        return_name : bool, optional, default=False
            If True, return a series that has dates and holiday names.
            False will only return dates.
        """
        if self.year is not None:
            dt = Timestamp(datetime(self.year, self.month, self.day))
            if return_name:
                return Series(self.name, index=[dt])
            else:
                return [dt]

        if self.start_date is not None:
            start_date = self.start_date

        if self.end_date is not None:
            end_date = self.end_date

        start_date = Timestamp(start_date)
        end_date   = Timestamp(end_date)

        year_offset = DateOffset(years=1)
        base_date = Timestamp(datetime(start_date.year, self.month, self.day))
        dates = DatetimeIndex(start=base_date, end=end_date, freq=year_offset)
        holiday_dates = list(self._apply_rule(dates))

        if return_name:
            return Series(self.name, index=holiday_dates)

        return holiday_dates


class ExchangeCalendar(AbstractHolidayCalendar):
    trading_times = [start]
    def get_market_times(date):
        

class US_ScheduledCalendar()
    """
    US stock exchange calendar specified by
    https://www.nyse.com/markets/hours-calendars
    """
    rules = nyse_rules

class US_ExchangeCalendar(AbstractHolidayCalendar):
    """
    US stock exchange calendar specified by
    https://www.nyse.com/markets/hours-calendars
    """
    rules = nyse_exchange_rules + nyse_unscheduled
        


class TestTradingCalendar(TestCase):

    @nottest
    def test_calendar_vs_environment(self):
        """
        test_calendar_vs_environment checks whether the
        historical data from yahoo matches our rule based system.
        handy, if not canonical, reference:
        http://www.chronos-st.org/NYSE_Observed_Holidays-1885-Present.html
        """

        env = TradingEnvironment()
        env_start_index = \
            env.trading_days.searchsorted(tradingcalendar.start)
        env_days = env.trading_days[env_start_index:]
        cal_days = tradingcalendar.trading_days
        self.check_days(env_days, cal_days)

    @nottest
    def test_lse_calendar_vs_environment(self):
        env = TradingEnvironment(
            bm_symbol='^FTSE',
            exchange_tz='Europe/London'
        )

        env_start_index = \
            env.trading_days.searchsorted(tradingcalendar_lse.start)
        env_days = env.trading_days[env_start_index:]
        cal_days = tradingcalendar_lse.trading_days
        self.check_days(env_days, cal_days)

    @nottest
    def test_tse_calendar_vs_environment(self):
        env = TradingEnvironment(
            bm_symbol='^GSPTSE',
            exchange_tz='US/Eastern'
        )

        env_start_index = \
            env.trading_days.searchsorted(tradingcalendar_tse.start)
        env_days = env.trading_days[env_start_index:]
        cal_days = tradingcalendar_tse.trading_days
        self.check_days(env_days, cal_days)

    @nottest
    def test_bmf_calendar_vs_environment(self):
        env = TradingEnvironment(
            bm_symbol='^BVSP',
            exchange_tz='America/Sao_Paulo'
        )

        env_start_index = \
            env.trading_days.searchsorted(tradingcalendar_bmf.start)
        env_days = env.trading_days[env_start_index:]
        cal_days = tradingcalendar_bmf.trading_days
        self.check_days(env_days, cal_days)

    def check_days(self, env_days, cal_days):
        diff = env_days - cal_days
        self.assertEqual(
            len(diff),
            0,
            "{diff} should be empty".format(diff=diff)
        )

        diff2 = cal_days - env_days
        self.assertEqual(
            len(diff2),
            0,
            "{diff} should be empty".format(diff=diff2)
        )

    def test_newyears(self):
        """
        Check whether tradingcalendar contains certain dates.
        """
        #     January 2012
        # Su Mo Tu We Th Fr Sa
        #  1  2  3  4  5  6  7
        #  8  9 10 11 12 13 14
        # 15 16 17 18 19 20 21
        # 22 23 24 25 26 27 28
        # 29 30 31

        day_after_new_years_sunday = datetime.datetime(
            2012, 1, 2, tzinfo=pytz.utc)

        self.assertNotIn(day_after_new_years_sunday,
                         tradingcalendar.trading_days,
                         """
If NYE falls on a weekend, {0} the Monday after is a holiday.
""".strip().format(day_after_new_years_sunday)
        )

        first_trading_day_after_new_years_sunday = datetime.datetime(
            2012, 1, 3, tzinfo=pytz.utc)

        self.assertIn(first_trading_day_after_new_years_sunday,
                      tradingcalendar.trading_days,
                      """
If NYE falls on a weekend, {0} the Tuesday after is the first trading day.
""".strip().format(first_trading_day_after_new_years_sunday)
        )

        #     January 2013
        # Su Mo Tu We Th Fr Sa
        #        1  2  3  4  5
        #  6  7  8  9 10 11 12
        # 13 14 15 16 17 18 19
        # 20 21 22 23 24 25 26
        # 27 28 29 30 31

        new_years_day = datetime.datetime(
            2013, 1, 1, tzinfo=pytz.utc)

        self.assertNotIn(new_years_day,
                         tradingcalendar.trading_days,
                         """
If NYE falls during the week, e.g. {0}, it is a holiday.
""".strip().format(new_years_day)
        )

        first_trading_day_after_new_years = datetime.datetime(
            2013, 1, 2, tzinfo=pytz.utc)

        self.assertIn(first_trading_day_after_new_years,
                      tradingcalendar.trading_days,
                      """
If the day after NYE falls during the week, {0} \
is the first trading day.
""".strip().format(first_trading_day_after_new_years)
        )

    def test_thanksgiving(self):
        """
        Check tradingcalendar Thanksgiving dates.
        """
        #     November 2005
        # Su Mo Tu We Th Fr Sa
        #        1  2  3  4  5
        #  6  7  8  9 10 11 12
        # 13 14 15 16 17 18 19
        # 20 21 22 23 24 25 26
        # 27 28 29 30
        thanksgiving_with_four_weeks = datetime.datetime(
            2005, 11, 24, tzinfo=pytz.utc)

        self.assertNotIn(thanksgiving_with_four_weeks,
                         tradingcalendar.trading_days,
                         """
If Nov has 4 Thursdays, {0} Thanksgiving is the last Thursady.
""".strip().format(thanksgiving_with_four_weeks)
        )

        #     November 2006
        # Su Mo Tu We Th Fr Sa
        #           1  2  3  4
        #  5  6  7  8  9 10 11
        # 12 13 14 15 16 17 18
        # 19 20 21 22 23 24 25
        # 26 27 28 29 30
        thanksgiving_with_five_weeks = datetime.datetime(
            2006, 11, 23, tzinfo=pytz.utc)

        self.assertNotIn(thanksgiving_with_five_weeks,
                         tradingcalendar.trading_days,
                         """
If Nov has 5 Thursdays, {0} Thanksgiving is not the last week.
""".strip().format(thanksgiving_with_five_weeks)
        )

        first_trading_day_after_new_years_sunday = datetime.datetime(
            2012, 1, 3, tzinfo=pytz.utc)

        self.assertIn(first_trading_day_after_new_years_sunday,
                      tradingcalendar.trading_days,
                      """
If NYE falls on a weekend, {0} the Tuesday after is the first trading day.
""".strip().format(first_trading_day_after_new_years_sunday)
        )

    def test_day_after_thanksgiving(self):
        early_closes = tradingcalendar.get_early_closes(
            tradingcalendar.start,
            tradingcalendar.end.replace(year=tradingcalendar.end.year + 1)
        )

        #    November 2012
        # Su Mo Tu We Th Fr Sa
        #              1  2  3
        #  4  5  6  7  8  9 10
        # 11 12 13 14 15 16 17
        # 18 19 20 21 22 23 24
        # 25 26 27 28 29 30
        fourth_friday = datetime.datetime(2012, 11, 23, tzinfo=pytz.utc)
        self.assertIn(fourth_friday, early_closes)

        #    November 2013
        # Su Mo Tu We Th Fr Sa
        #                 1  2
        #  3  4  5  6  7  8  9
        # 10 11 12 13 14 15 16
        # 17 18 19 20 21 22 23
        # 24 25 26 27 28 29 30
        fifth_friday = datetime.datetime(2013, 11, 29, tzinfo=pytz.utc)
        self.assertIn(fifth_friday, early_closes)

    def test_early_close_independence_day_thursday(self):
        """
        Until 2013, the market closed early the Friday after an
        Independence Day on Thursday.  Since then, the early close is on
        Wednesday.
        """
        early_closes = tradingcalendar.get_early_closes(
            tradingcalendar.start,
            tradingcalendar.end.replace(year=tradingcalendar.end.year + 1)
        )
        #      July 2002
        # Su Mo Tu We Th Fr Sa
        #     1  2  3  4  5  6
        #  7  8  9 10 11 12 13
        # 14 15 16 17 18 19 20
        # 21 22 23 24 25 26 27
        # 28 29 30 31
        wednesday_before = datetime.datetime(2002, 7, 3, tzinfo=pytz.utc)
        friday_after = datetime.datetime(2002, 7, 5, tzinfo=pytz.utc)
        self.assertNotIn(wednesday_before, early_closes)
        self.assertIn(friday_after, early_closes)

        #      July 2013
        # Su Mo Tu We Th Fr Sa
        #     1  2  3  4  5  6
        #  7  8  9 10 11 12 13
        # 14 15 16 17 18 19 20
        # 21 22 23 24 25 26 27
        # 28 29 30 31
        wednesday_before = datetime.datetime(2013, 7, 3, tzinfo=pytz.utc)
        friday_after = datetime.datetime(2013, 7, 5, tzinfo=pytz.utc)
        self.assertIn(wednesday_before, early_closes)
        self.assertNotIn(friday_after, early_closes)

def ea

def get_non_trading_days(start, end):
    non_trading_rules = []

    start = canonicalize_datetime(start)
    end = canonicalize_datetime(end)

    weekends = rrule.rrule(
        rrule.YEARLY,
        byweekday=(rrule.SA, rrule.SU),
        cache=True,
        dtstart=start,
        until=end
    )
    non_trading_rules.append(weekends)

    new_years = rrule.rrule(
        rrule.MONTHLY,
        byyearday=1,
        cache=True,
        dtstart=start,
        until=end
    )
    non_trading_rules.append(new_years)

    non_trading_days = non_trading_ruleset.between(start, end, inc=True)

    # Add September 11th closings
    # http://en.wikipedia.org/wiki/Aftermath_of_the_September_11_attacks
    # Due to the terrorist attacks, the stock market did not open on 9/11/2001
    # It did not open again until 9/17/2001.
    #
    #    September 2001
    # Su Mo Tu We Th Fr Sa
    #                    1
    #  2  3  4  5  6  7  8
    #  9 10 11 12 13 14 15
    # 16 17 18 19 20 21 22
    # 23 24 25 26 27 28 29
    # 30

    for day_num in range(11, 17):
        non_trading_days.append(
            datetime(2001, 9, day_num, tzinfo=pytz.utc))

    # Add closings due to Hurricane Sandy in 2012
    # http://en.wikipedia.org/wiki/Hurricane_sandy
    #
    # The stock exchange was closed due to Hurricane Sandy's
    # impact on New York.
    # It closed on 10/29 and 10/30, reopening on 10/31
    #     October 2012
    # Su Mo Tu We Th Fr Sa
    #     1  2  3  4  5  6
    #  7  8  9 10 11 12 13
    # 14 15 16 17 18 19 20
    # 21 22 23 24 25 26 27
    # 28 29 30 31

    for day_num in range(29, 31):
        non_trading_days.append(
            datetime(2012, 10, day_num, tzinfo=pytz.utc))

    # Misc closings from NYSE listing.
    # http://www.nyse.com/pdfs/closings.pdf
    #
    # National Days of Mourning
    # - President Richard Nixon
    non_trading_days.append(datetime(1994, 4, 27, tzinfo=pytz.utc))
    # - President Ronald W. Reagan - June 11, 2004
    non_trading_days.append(datetime(2004, 6, 11, tzinfo=pytz.utc))
    # - President Gerald R. Ford - Jan 2, 2007
    non_trading_days.append(datetime(2007, 1, 2, tzinfo=pytz.utc))

    non_trading_days.sort()
    return pd.DatetimeIndex(non_trading_days)

non_trading_days = get_non_trading_days(start, end)
trading_day = pd.tseries.offsets.CDay(holidays=non_trading_days)


def get_trading_days(start, end, trading_day=trading_day):
    return pd.date_range(start=start.date(),
                         end=end.date(),
                         freq=trading_day).tz_localize('UTC')

trading_days = get_trading_days(start, end)


def get_early_closes(start, end):
    # 1:00 PM close rules based on
    # http://quant.stackexchange.com/questions/4083/nyse-early-close-rules-july-4th-and-dec-25th # noqa
    # and verified against http://www.nyse.com/pdfs/closings.pdf

    # These rules are valid starting in 1993

    start = canonicalize_datetime(start)
    end = canonicalize_datetime(end)

    start = max(start, datetime(1993, 1, 1, tzinfo=pytz.utc))
    end = max(end, datetime(1993, 1, 1, tzinfo=pytz.utc))

    # Not included here are early closes prior to 1993
    # or unplanned early closes

    early_close_rules = []

    day_after_thanksgiving = rrule.rrule(
        rrule.MONTHLY,
        bymonth=11,
        # 4th Friday isn't correct if month starts on Friday, so restrict to
        # day range:
        byweekday=(rrule.FR),
        bymonthday=range(23, 30),
        cache=True,
        dtstart=start,
        until=end
    )
    early_close_rules.append(day_after_thanksgiving)

    christmas_eve = rrule.rrule(
        rrule.MONTHLY,
        bymonth=12,
        bymonthday=24,
        byweekday=(rrule.MO, rrule.TU, rrule.WE, rrule.TH),
        cache=True,
        dtstart=start,
        until=end
    )
    early_close_rules.append(christmas_eve)

    friday_after_christmas = rrule.rrule(
        rrule.MONTHLY,
        bymonth=12,
        bymonthday=26,
        byweekday=rrule.FR,
        cache=True,
        dtstart=start,
        # valid 1993-2007
        until=min(end, datetime(2007, 12, 31, tzinfo=pytz.utc))
    )
    early_close_rules.append(friday_after_christmas)

    day_before_independence_day = rrule.rrule(
        rrule.MONTHLY,
        bymonth=7,
        bymonthday=3,
        byweekday=(rrule.MO, rrule.TU, rrule.TH),
        cache=True,
        dtstart=start,
        until=end
    )
    early_close_rules.append(day_before_independence_day)

    day_after_independence_day = rrule.rrule(
        rrule.MONTHLY,
        bymonth=7,
        bymonthday=5,
        byweekday=rrule.FR,
        cache=True,
        dtstart=start,
        # starting in 2013: wednesday before independence day
        until=min(end, datetime(2012, 12, 31, tzinfo=pytz.utc))
    )
    early_close_rules.append(day_after_independence_day)

    wednesday_before_independence_day = rrule.rrule(
        rrule.MONTHLY,
        bymonth=7,
        bymonthday=3,
        byweekday=rrule.WE,
        cache=True,
        # starting in 2013
        dtstart=max(start, datetime(2013, 1, 1, tzinfo=pytz.utc)),
        until=max(end, datetime(2013, 1, 1, tzinfo=pytz.utc))
    )
    early_close_rules.append(wednesday_before_independence_day)

    early_close_ruleset = rrule.rruleset()

    for rule in early_close_rules:
        early_close_ruleset.rrule(rule)
    early_closes = early_close_ruleset.between(start, end, inc=True)

    # Misc early closings from NYSE listing.
    # http://www.nyse.com/pdfs/closings.pdf
    #
    # New Year's Eve
    nye_1999 = datetime(1999, 12, 31, tzinfo=pytz.utc)
    if start <= nye_1999 and nye_1999 <= end:
        early_closes.append(nye_1999)

    early_closes.sort()
    return pd.DatetimeIndex(early_closes)

early_closes = get_early_closes(start, end)
