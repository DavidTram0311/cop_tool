import pandas as pd
import numpy as np
import os
import filters
import ond
import functions
import time
import gspread
# Authenticate google sheet
from google.auth import default
creds, _ = default()
gs = gspread.authorize(creds)

# Start running time
start = time.time()
# Input sheet
def input_data(filename):
    namefile = os.path.basename(filename).split('.')[1]
    if namefile == 'xlsx':
        data = pd.read_excel(filename, )
    elif namefile == 'csv':
        data = pd.read_csv(filename)
    return data

# Import data
name = os.listdir('./raw_data')[0]
name_summary = name.split('.')[0]
filename = f'./raw_data/{name}'
# filename = './source_test.xlsx'
data = input_data(filename)

# Clean null
data = data.dropna(subset=['First Attempt Delivery DateTime','Picked DateTime'])

# Process data

# Type of province
data['type_o'] = data['Pickup Province'].apply(functions.filter_ond)
data['type_d'] = data['Delivery Province'].apply(functions.filter_ond)

# Zone
data['origin'] = [functions.region_o(province, district, services) for province, district, services in
                  zip(data['Pickup Province'], data['Pickup District'], data['type_o'])]

data['dest'] = [functions.region_d(province, district, services) for province, district, services in
                  zip(data['Delivery Province'], data['Delevery District'], data['type_d'])]

# Lanes
data['lanes'] = [functions.lanes(origin,dest) for origin, dest in zip(data['origin'], data['dest'])]

# Routes
data['routes'] = data['lanes'].apply(functions.routes)

# Week of year
data['completed'] = data['Actual Delivery DateTime'].apply(functions.week_of_year)
data['completed_w'] = data['Actual Delivery DateTime'].apply(functions.week_of_year)
data['rts'] = data['RTS Trigger DateTime'].apply(functions.week_of_year)
data['rts_w'] = data['RTS Trigger DateTime'].apply(functions.week_of_year)
data['1st attempt'] = data['First Attempt Delivery DateTime'].apply(functions.week_of_year)

# Leadtime
data['leadtime'] = [functions.leadtime(start,end) for start, end in zip(data['First Attempt Delivery DateTime'], data['Picked DateTime'])]

# Month of year
data['actual_deli_month'] = data['Actual Delivery DateTime'].apply(functions.month_of_year)
data['rts_month'] = data['RTS Trigger DateTime'].apply(functions.month_of_year)
data['actual'] = data['Actual Delivery DateTime'].apply(functions.month_of_year)
data['rts_m'] = data['RTS Trigger DateTime'].apply(functions.month_of_year)

# Monthly Success rate
# Group by 3pls and month
summary_actual = data.groupby(['Transporter','actual_deli_month'],as_index=False)['actual'].count()
summary_rts = data.groupby(['Transporter','rts_month'],as_index=False)['rts_m'].count()

#Calculate success rate
summary_month = functions.success_rate(summary_actual, summary_rts,'actual_deli_month', 'rts_month','actual', 'rts_m')

# Leadtime
# Group by 3pls and month
leadtime_lanes = data.groupby(['Transporter','routes','actual_deli_month'],as_index=False)['leadtime'].sum()
orders_lanes = data.groupby(['Transporter','routes','actual_deli_month'],as_index=False)['actual'].count()

# Calculate sum leadtimes of orders
leadtime_month = functions.leadtime_actual(leadtime_lanes, orders_lanes, 'actual_deli_month', 'actual','routes')
# leadtime_month

# Weekly success rate
summary_w_actual = data.groupby(['Transporter','completed_w'],as_index=False)['completed'].count()
summary_w_rts = data.groupby(['Transporter','rts_w'],as_index=False)['rts'].count()

summary_weekly = functions.success_rate(summary_w_actual, summary_w_rts,'completed_w', 'rts_w','completed', 'rts')

# Leadtime
leadtime_w_lanes = data.groupby(['Transporter','routes','completed_w'],as_index=False)['leadtime'].sum()
orders_w_lanes = data.groupby(['Transporter','routes','completed_w'],as_index=False)['completed'].count()

leadtime_weekly = functions.leadtime_actual(leadtime_w_lanes, orders_w_lanes, 'completed_w', 'completed','routes')

# MONTHLY SUCCESS RATE
months = len(summary_month['week/month'].unique())

# Create spreadsheet
sh = gs.create('summary_' + name_summary)

month_lst = []
if months >= 2:
  print(f"---1. There are {months} months---")
  for i in range(months):
    print(f"Month: {summary_month['week/month'].unique()[i]}")
  # Display text to input
  # number_of_month = int(input("$$$ Please input number of month (must = 1): "))
  # while number_of_month > 1:
  #   number_of_month = int(input("$$$ Type number 1, please: "))

  number_of_month = 1
  print(f"$$$ Please input month you want to display: ")
  for i in range(0,number_of_month):
    month = int(input())
    month_lst.append(month)

else:
  print(f"---1. There are {months} month: {summary_month['week/month'].unique()[0]}---")
  month_lst.append(summary_month['week/month'].unique()[0])

# update_values_m_sr(sh, month_lst, summary_month)
functions.update_values_wn_sr(sh, month_lst, summary_month,'monthly_sr')
time.sleep(20)
functions.leadtime_gsheet_route(sh, month_lst, leadtime_month, 'monthly_leadtime', 'Month')
# functions.leadtime_gsheet_region(sh,month_lst, leadtime_month_region, 'Month_reigon_leadtime', 'Month')


# WEEKLY SUCCESS RATE
weeks = len(summary_weekly['week/month'].unique())

week_lst = []
if weeks >= 2:
  print(f"---2. There are {weeks} weeks---")
  for i in range(len(summary_weekly['week/month'].unique())):
    print(f"Week: {summary_weekly['week/month'].unique()[i]}")

  # number_of_week = int(input("$$$ Please type number of week (must = 1): "))
  # while number_of_week > 1:
  #   number_of_week = int(input("$$$ Type number 1, please: "))

  number_of_week = 1
  print(f"$$$ Please input week you want to display: ")
  for i in range(0,number_of_week):
    week = int(input())
    week_lst.append(week)

else:
  print(f"---2. There are {weeks} weeks: {summary_weekly['week/month'].unique()[0]}")
  week_lst.append(summary_weekly['week/month'].unique()[0])

# update_values_w_sr(sh, week_lst, summary_weekly)
functions.update_values_wn_sr(sh, week_lst, summary_weekly, 'weekly_sr')
time.sleep(20)
functions.leadtime_gsheet_route(sh, week_lst, leadtime_weekly, 'weekly_leadtime', 'Week')
# functions.leadtime_gsheet_region(sh1, week_lst, leadtime_weekly_regions, 'weekly_region_leadtime', 'Week')

sh.share(send_result_to_email, perm_type='user', role='writer', notify = True)
print(f"---After {(time.time() - start) / 60}: mins, summary_{name_summary} report sent to email: {send_result_to_email}---")
print(f"---Please check mail inbox---")