CAThanksgivingDay = Holiday('Thanksgiving', month=10, day=1,
                            offset=DateOffset(weekday=MO(2)))
New_Years = Holiday('New Years Day', month=1,  day=1,
                    observance=nearest_workday)
July_4th = Holiday('July 4th', month=7,  day=4, observance=nearest_workday)                                                

CAFamilyDay = Holiday('CA Family Day(Ontario Obs)', month=2,  day=1, 
                      offset=DateOffset(weekday=MO(3))                                                
VictoriaDay = Holiday('Victoria Day', month=2,  day=1, 
                      offset=DateOffset(weekday=MO(3))               
Good Friday - April 18, 2014
Victoria Day - May 19, 2014
Canada Day - July 1, 2014
Civic Holiday - August 4, 2014
Labour Day - September 1, 2014
Thanksgiving Day - October 13, 2014
Christmas Day - December 25, 2014
Boxing Day - December 26, 2014
