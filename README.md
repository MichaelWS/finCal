finCal
===============

This is a calendar class for financial exchanges in python.

It will be extended to include futures and roll dates 

```python
us = finCal.get_stock_cal("US")
In [1]: import finCal
In [2]: us = finCal.get_stock_calendar("US")
In [3]: us.holidays()

Out[3]: 
<class 'pandas.tseries.index.DatetimeIndex'>
[1970-01-01, ..., 2030-12-25]
Length: 494, Freq: None, Timezone: None

In [4]: us.early_closes()

Out[4]: 
<class 'pandas.tseries.index.DatetimeIndex'>
[1970-07-02, ..., 2030-12-24]
Length: 122, Freq: None, Timezone: None


In [5]: us.get_market_times(pd.Timestamp("2015-07-03"))

Out[5]: {'close': None, 'start': None}


In [6]: us.get_market_times(pd.Timestamp("2015-07-02"))

Out[6]: 
{'close': Timestamp('2015-07-02 13:00:00-0400', tz='America/New_York'),
 'start': Timestamp('2015-07-02 09:30:00-0400', tz='America/New_York')}

In [7]: us.get_market_times(pd.Timestamp("2015-07-01"))

Out[7]: 
{'close': Timestamp('2015-07-01 16:00:00-0400', tz='America/New_York'),
 'start': Timestamp('2015-07-01 09:30:00-0400', tz='America/New_York')}
```
