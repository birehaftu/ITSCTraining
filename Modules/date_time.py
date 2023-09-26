# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 10:17:35 2023

@author: birhane
"""
import datetime as dt
from dateutil.relativedelta import relativedelta
d=dt.date(2023,9,25)
d2=dt.date.today()-dt.timedelta(days=-1)
d2=dt.date.today()-relativedelta(years=1)
print('d: ',d)
print('d2: ',d2)
# =============================================================================

# =============================================================================
print('d.year: ',d.year)
print('d.month: ',d.month)
print('d.day: ',d.day)