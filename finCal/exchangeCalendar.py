from pandas.tseries.holiday import (AbstractHolidayCalendar)
from pandas import Timestamp
import datetime
from finCal.exchangeInfo import (nyse_early_close_rules, nyse_exchange_rules,
                                 nyse_times, nyse_rules, ca_tsx_rules,
                                 ca_tsx_times, ca_tsx_early_close_rules,
                                 euronext_rules, eu_early_close_rules,
                                 euronext_times)

BASE_TZ_INFO = "America/New_York"


def _process_exch_time(exch_time_dict):
    try:
        assert "start" in exch_time_dict
        assert "close" in exch_time_dict
        assert "early_close" in exch_time_dict
        if "end_date" not in exch_time_dict:
            exch_time_dict["end_date"] = None
        return exch_time_dict
    except Exception:
        print("exchange info dicts need start, close, and early_close")
        raise


class ExchangeCalendar(AbstractHolidayCalendar):

    """
    Class that defines a Exchange time
    time_info is a dict or list of dicts
    example = {'early_close': datetime.time(13, 0),
               'end': datetime.time(16, 0),
               'end_date': None,
               'start': datetime.time(9, 30)}
    a list of [example,...]
    rules
    early_close_rules

    """
    rules = []
    start_date = Timestamp(datetime.datetime(1970, 1, 1))
    end_date = Timestamp(datetime.datetime(2030, 12, 31))
    _holiday_cache = None
    _early_close_cache = None
    early_close_rules = []
    time_info = None
    open_days = (0, 1, 2, 3, 4)

    def __init__(self, name=None, rules=None, early_close_rules=None,
                 open_days=None, time_info=None,
                 tz_info=BASE_TZ_INFO):
        super(ExchangeCalendar, self).__init__()
        if open_days is not None:
            self.open_days = open_days
            # Monday Through Friday is default, but Israel as an example
            # of a different day.  also this allows for complex rules
            # there are shifts of ays around the new year in most Asian
            # countries
        if rules is not None:
            self.rules = rules
        if early_close_rules is not None:
            self.early_close_rules = early_close_rules
        if time_info is not None:
            self.time_info = time_info
        assert type(self.time_info) == dict or type(self.time_info) == list
        if tz_info is not None:
            self.tz_info = tz_info
        time_info = self.time_info
        if type(time_info) == dict:
            self.exchange_schedules = [_process_exch_time(time_info)]
        else:
            self.exchange_schedules = []
            for info in time_info:
                self.exchange_schedules.append(_process_exch_time(info))
            self.exchange_schedules = sorted(self.exchange_times,
                                             key=lambda x: x["end_date"])
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
            raise Exception('Exchange Calendar %s does not have any ' +
                            'early close rules specified' % self.name)

        if start is None:
            start = AbstractHolidayCalendar.start_date

        if end is None:
            end = AbstractHolidayCalendar.end_date
        start = Timestamp(start)
        end = Timestamp(end)
        early_closes = None
        # If we don't have a cache or the dates are outside the prior cache,
        # we get them again
        if (self._early_close_cache is None
                or start < self._early_close_cache[0]
                or end > self._early_close_cache[1]):
            for rule in self.early_close_rules:
                rule_early_closes = rule.dates(start, end, return_name=True)
                if early_closes is None:
                    early_closes = rule_early_closes
                else:
                    early_closes = early_closes.append(rule_early_closes)
            self._early_close_cache = (start, end, early_closes.sort_index())

        early_closes = self._early_close_cache[2]
        early_closes = early_closes[start:end]

        if return_name:
            return early_closes
        else:
            return early_closes.index

    def get_market_times(self, date):
        """
        returns a set of pandas Timestamps re
        if market is closed
        returns (None, None)
        """
        if type(date) != Timestamp:
            date = Timestamp(date)
        if (date in self._cache[2].index
                or date.dayofweek not in self.open_days):
            return {"start": None,
                    "close": None}
            # returning None for market closure.
        else:
            for schedule in self.exchange_schedules:
                if (schedule["end_date"] is None or
                        date <= schedule["end_date"]):
                    break
            # done because some latin american markets have followed nyse
            # at some part of their history.
            if "tz_info" in schedule:
                set_tz = schedule["tz_info"]
            else:
                set_tz = self.tz_info
            start_ts = _create_ts(date, schedule["start"], set_tz)
            out_sch = {"start": start_ts}
            if date in self._early_close_cache[2].index:
                if "lunch_start" in schedule:
                    out_sch["close"] = _create_ts(date,
                                                  schedule["lunch_start"],
                                                  set_tz)
                else:
                    out_sch["close"] = _create_ts(date,
                                                  schedule["early_close"],
                                                  set_tz)

            else:
                if "lunch_start" in schedule:
                    out_sch["lunch"] = _create_ts(date,
                                                  schedule["lunch_start"],
                                                  set_tz)
                    lunch_ts_end = _create_ts(date, schedule["lunch_end"],
                                              set_tz)
                    out_sch["lunch_end"] = lunch_ts_end
                    out_sch["close"] = _create_ts(date, schedule["close"],
                                                  set_tz)
                else:
                    out_sch["close"] = _create_ts(date, schedule["close"],
                                                  set_tz)
            return out_sch


def _create_ts(date, time, tz):
    """ internal class for combining date time and tz_info
    """
    return Timestamp(datetime.datetime.combine(date.date(), time),
                     tz=tz)


class US_ScheduledCalendar(ExchangeCalendar):

    """
    US stock exchange calendar specified by
    https://www.nyse.com/markets/hours-calendars
    """
    rules = nyse_rules
    early_close_rules = nyse_early_close_rules


class US_StockExchangeCalendar(ExchangeCalendar):

    """
    US stock exchange calendar specified by
    https://www.nyse.com/markets/hours-calendars
    """
    rules = nyse_exchange_rules
    early_close_rules = nyse_early_close_rules
    tz_info = BASE_TZ_INFO
    time_info = nyse_times


class CA_StockExchangeCalendar(ExchangeCalendar):

    """
    CA stock exchange calendar
    """
    rules = ca_tsx_rules
    early_close_rules = ca_tsx_early_close_rules
    tz_info = "America/Toronto"
    time_info = ca_tsx_times


class EU_StockExchangeCalendar(ExchangeCalendar):

    """
    EU euronext stock exchange calendar
    """
    rules = euronext_rules
    early_close_rules = eu_early_close_rules
    tz_info = "Europe/Paris"
    time_info = euronext_times

country_to_stock_class = {"US": US_StockExchangeCalendar,
                          "CA": CA_StockExchangeCalendar,
                          "EU": EU_StockExchangeCalendar}


def get_stock_calendar(country):
    if country in country_to_stock_class:
        return country_to_stock_class[country]()
    else:
        print("%s not yet implemented" % country)


def list_calendars():
    print("currently implemented countries:" +
          repr(country_to_stock_class.keys()))
