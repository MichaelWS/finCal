
from datetime import datetime
import pandas.util.testing as tm
from pandas import Timestamp
import finCal
import nose


class TestCalendar(tm.TestCase):

    def setUp(self):
        self.start_date = datetime(2001, 1, 1)
        self.end_date = datetime(2012, 12, 31)

    def test_us_stock(self):
        us = finCal.get_stock_calendar("US")
        holidays = us.holidays(self.start_date, self.end_date)
        holidayList = [Timestamp('2001-01-01'),
                       Timestamp('2001-01-15'),
                       Timestamp('2001-02-19'),
                       Timestamp('2001-05-28'),
                       Timestamp('2001-07-04'),
                       Timestamp('2001-09-03'),
                       Timestamp('2001-09-11'),
                       Timestamp('2001-09-12'),
                       Timestamp('2001-09-13'),
                       Timestamp('2001-09-14'),
                       Timestamp('2001-11-22'),
                       Timestamp('2001-12-25'),
                       Timestamp('2002-01-01'),
                       Timestamp('2002-01-21'),
                       Timestamp('2002-02-18'),
                       Timestamp('2002-05-27'),
                       Timestamp('2002-07-04'),
                       Timestamp('2002-09-02'),
                       Timestamp('2002-11-28'),
                       Timestamp('2002-12-25'),
                       Timestamp('2003-01-01'),
                       Timestamp('2003-01-20'),
                       Timestamp('2003-02-17'),
                       Timestamp('2003-05-26'),
                       Timestamp('2003-07-04'),
                       Timestamp('2003-09-01'),
                       Timestamp('2003-11-27'),
                       Timestamp('2003-12-25'),
                       Timestamp('2004-01-01'),
                       Timestamp('2004-01-19'),
                       Timestamp('2004-02-16'),
                       Timestamp('2004-05-24'),
                       Timestamp('2004-06-11'),
                       Timestamp('2004-07-05'),
                       Timestamp('2004-09-06'),
                       Timestamp('2004-11-25'),
                       Timestamp('2004-12-24'),
                       Timestamp('2005-01-17'),
                       Timestamp('2005-02-21'),
                       Timestamp('2005-05-30'),
                       Timestamp('2005-07-04'),
                       Timestamp('2005-09-05'),
                       Timestamp('2005-11-24'),
                       Timestamp('2005-12-26'),
                       Timestamp('2006-01-02'),
                       Timestamp('2006-01-16'),
                       Timestamp('2006-02-20'),
                       Timestamp('2006-05-29'),
                       Timestamp('2006-07-04'),
                       Timestamp('2006-09-04'),
                       Timestamp('2006-11-23'),
                       Timestamp('2006-12-25'),
                       Timestamp('2007-01-01'),
                       Timestamp('2007-01-02'),
                       Timestamp('2007-01-15'),
                       Timestamp('2007-02-19'),
                       Timestamp('2007-05-28'),
                       Timestamp('2007-07-04'),
                       Timestamp('2007-09-03'),
                       Timestamp('2007-11-22'),
                       Timestamp('2007-12-25'),
                       Timestamp('2008-01-01'),
                       Timestamp('2008-01-21'),
                       Timestamp('2008-02-18'),
                       Timestamp('2008-05-26'),
                       Timestamp('2008-07-04'),
                       Timestamp('2008-09-01'),
                       Timestamp('2008-11-27'),
                       Timestamp('2008-12-25'),
                       Timestamp('2009-01-01'),
                       Timestamp('2009-01-19'),
                       Timestamp('2009-02-16'),
                       Timestamp('2009-05-25'),
                       Timestamp('2009-07-03'),
                       Timestamp('2009-09-07'),
                       Timestamp('2009-11-26'),
                       Timestamp('2009-12-25'),
                       Timestamp('2010-01-01'),
                       Timestamp('2010-01-18'),
                       Timestamp('2010-02-15'),
                       Timestamp('2010-05-24'),
                       Timestamp('2010-07-05'),
                       Timestamp('2010-09-06'),
                       Timestamp('2010-11-25'),
                       Timestamp('2010-12-24'),
                       Timestamp('2011-01-17'),
                       Timestamp('2011-02-21'),
                       Timestamp('2011-05-30'),
                       Timestamp('2011-07-04'),
                       Timestamp('2011-09-05'),
                       Timestamp('2011-11-24'),
                       Timestamp('2011-12-26'),
                       Timestamp('2012-01-02'),
                       Timestamp('2012-01-16'),
                       Timestamp('2012-02-20'),
                       Timestamp('2012-05-28'),
                       Timestamp('2012-07-04'),
                       Timestamp('2012-09-03'),
                       Timestamp('2012-10-29'),
                       Timestamp('2012-10-30'),
                       Timestamp('2012-11-01'),
                       Timestamp('2012-11-22'),
                       Timestamp('2012-12-25')]
        self.assertEqual(list(holidays), holidayList)
        result = us.get_market_times('2013-07-03')
        expected = {'close': Timestamp('2013-07-03 13:00:00',
                                       tz='America/New_York'),
                    'start': Timestamp('2013-07-03 09:30:00',
                                       tz='America/New_York')}
        self.assertEqual(expected, result)
        result = us.get_market_times('2013-07-04')
        expected = {'close': None, 'start': None}
        self.assertEqual(expected, result)
        # early_closes
        result = us.early_closes(self.start_date, self.end_date)
        expected = [Timestamp('2001-07-03 00:00:00'),
                    Timestamp('2001-11-23 00:00:00'),
                    Timestamp('2001-12-24 00:00:00'),
                    Timestamp('2002-07-03 00:00:00'),
                    Timestamp('2002-11-29 00:00:00'),
                    Timestamp('2002-12-24 00:00:00'),
                    Timestamp('2003-07-03 00:00:00'),
                    Timestamp('2003-11-28 00:00:00'),
                    Timestamp('2003-12-24 00:00:00'),
                    Timestamp('2004-11-26 00:00:00'),
                    Timestamp('2005-11-25 00:00:00'),
                    Timestamp('2006-07-03 00:00:00'),
                    Timestamp('2006-11-24 00:00:00'),
                    Timestamp('2007-07-03 00:00:00'),
                    Timestamp('2007-11-23 00:00:00'),
                    Timestamp('2007-12-24 00:00:00'),
                    Timestamp('2008-07-03 00:00:00'),
                    Timestamp('2008-11-28 00:00:00'),
                    Timestamp('2008-12-24 00:00:00'),
                    Timestamp('2009-11-27 00:00:00'),
                    Timestamp('2009-12-24 00:00:00'),
                    Timestamp('2010-11-26 00:00:00'),
                    Timestamp('2011-11-25 00:00:00'),
                    Timestamp('2012-07-03 00:00:00'),
                    Timestamp('2012-11-23 00:00:00'),
                    Timestamp('2012-12-24 00:00:00')]
        self.assertEqual(expected, list(result))


if __name__ == '__main__':
    nose.runmodule(argv=[__file__, '-vvs', '-x', '--pdb', '--pdb-failure'],
                   exit=False)
