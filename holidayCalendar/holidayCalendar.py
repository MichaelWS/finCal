import pandas.tseries.holiday as pd_calendar


class US_ExchangeCalendar(pd_calendar.AbstractHolidayCalendar):
    """
    US Federal Government Holiday Calendar based on rules specified
    by: https://www.opm.gov/policy-data-oversight/snow-dismissal-procedures/federal-holidays/
    """
    rules = [
        pd._Holiday('New Years Day', month=1,  day=1,  observance=nearest_workday),
        USMartinLutherKingJr,
        USPresidentsDay,
        USMemorialDay,
        Holiday('July 4th', month=7,  day=4,  observance=nearest_workday),
        USLaborDay,
        USColumbusDay,
        Holiday('Veterans Day', month=11, day=11, observance=nearest_workday),
        USThanksgivingDay,
        Holiday('Christmas', month=12, day=25, observance=nearest_workday)
        ]


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

def half_days
