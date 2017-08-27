#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 00:04:28 2017

@author: surjitdas
"""

import pandas as pd
import numpy as np
from datetime import datetime, date
df = pd.read_excel('/Users/surjitdas/Box Sync/Barclays Data Tower/Governance/Operations/Resource Master - IIT.xlsx','Base data')

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('/Users/surjitdas/Box Sync/Barclays Data Tower/Governance/Operations/Reports.xlsx', engine='xlsxwriter')

#1. Syam T&M Headcount
df2 = df.groupby(["Status","Scoped_vs_Non_Scoped","Line_Manager"])['Emp_Notes_ID'].count()
df2.to_excel(writer, sheet_name='Line_Manager')


# Close the Pandas Excel writer and output the Excel file.
writer.save()
print("Done")